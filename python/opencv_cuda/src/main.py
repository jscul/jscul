import shutil
import subprocess
import tempfile
from os import closerange
from pathlib import Path

from fastapi import FastAPI, File, Header, UploadFile
from fastapi.responses import FileResponse, Response, StreamingResponse

app = FastAPI()
tempfile.tempdir = "temp"

CHUNK_SIZE = 1024 * 1024


@app.get("/")
def ffmpeg():
    command = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)

    if command.returncode == 0:
        return {"ffmpeg": command.stdout}
    else:
        return {"ffmpeg": command.stderr}


@app.post("/files")
async def create_file(file: UploadFile = File(...)):
    """
    Test Comment
    """

    file_name = f"temp/{file.filename}"
    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file


def read_in_chunks(file_object, chunk_size=CHUNK_SIZE):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


# https://medium.com/@radhian.amri/video-streaming-using-http-206-partial-content-in-go-4e89d96abdd0
@app.get("/files")
async def video_endpoint(filename: str, range: str = Header(None)):

    file_name = Path(f"temp/{filename}")

    start, end = range.replace("bytes=", "").split("-")
    start = int(start) if not end else end
    end = start + CHUNK_SIZE

    with open(file_name, "rb") as video:
        video.seek(start)
        data = video.read(CHUNK_SIZE)
        filesize = file_name.stat().st_size
        headers = {
            "Content-Range": f"bytes {str(start)}-{str(filesize - 1)}/{str(filesize)}",
            "Content-Length": f"{len(data)}",
            "Accept-Ranges": "bytes",
        }
        return Response(content=data, status_code=206, headers=headers, media_type="video/mp4")


@app.post("/process")
async def video_endpoint(filename: str):

    file_name = Path(f"temp/{filename}")

    command = subprocess.run(
        [
            "ffmpeg",
            "-i",
            file_name,
            "-vf",
            "vidstabdetect=shakiness=10:accuracy=15:result=temp/mytransforms.trf",
            "-f",
            "null",
            "-",
        ],
        capture_output=True,
        text=True,
    )

    # RUN
    # RUN ffmpeg -i input.mp4 -vf vidstabtransform=smoothing=30:input="mytransforms.trf" out_stabilized.mp4

    if command.returncode != 0:
        return {"ffmpeg": command.stderr}

    command = subprocess.run(
        [
            "ffmpeg",
            "-i",
            file_name,
            "-vf",
            "vidstabtransform=smoothing=30:input=temp/mytransforms.trf",
            "temp/out_stabilized.mp4",
        ],
        capture_output=True,
        text=True,
    )

    if command.returncode != 0:
        return {"ffmpeg": command.stderr}

    return {}


@app.get("/download")
async def create_file(filename: str):

    file_name = f"temp/{filename}"
    return FileResponse(file_name)


# if __name__ == "__main__":
#     uvicorn.run("app", host="0.0.0.0", port=8000, workers=2, debug=True, reload=True)
