""""""


import requests
import os.path


def download_file(filename, url, force=False):
    """
    Download a URL to a file.
    """

    if force or not os.path.exists(filename):
        with open(filename, "wb") as fout:
            print(f"Downloading file {filename} from {url}")
            response = requests.get(url, stream=True)
            response.raise_for_status()
            for block in response.iter_content(4096):
                fout.write(block)

        return True

    return False
