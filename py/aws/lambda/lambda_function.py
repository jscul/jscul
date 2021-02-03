""""""


import sys
from io import BytesIO
import base64
import urllib.parse

# import dependencies from './package'
from package.PIL import Image, ImageDraw, ImageFont


def handler(event, context):
    """"""

    text = event["queryStringParameters"].get("t", "?")
    size = int(event["queryStringParameters"].get("s", "512"))

    img = Image.new("RGBA", (size, size), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("fonts/UbuntuMono-B.ttf", 80)
    draw.multiline_text((0, 0), text, (255, 255, 255), font, spacing=8)

    foreground = img.crop(img.getbbox())
    f_width, f_height = foreground.size

    img = Image.new("RGB", (size, size), color=(52, 52, 52))
    img.paste(
        foreground,
        (int(0.5 * size - 0.5 * f_width), int(0.5 * size - 0.5 * f_height)),
        foreground,
    )

    bytes_io = BytesIO()
    img.save(bytes_io, format="PNG")

    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {"content-type": "image/png"},
        "body": base64.b64encode(bytes_io.getvalue()).decode("utf-8"),
    }


if __name__ == "__main__":

    import os

    ret = handler({"queryStringParameters": {"s": 512, "t": "Test"}}, "")

    img = Image.open(BytesIO(base64.b64decode(ret["body"])))
    img.save("/home/jscul/Software/common.py/aws/lambda/out/out.png")

    if True:
        os.system(
            "xdg-open /home/jscul/Software/common.py/aws/lambda/out/out.png"
        )
