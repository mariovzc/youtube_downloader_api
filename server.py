from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import FileResponse
from file_handler import FileHandler


def valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url) and "youtube.com" in url

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}


@app.post("/download")
def download_file(url: str = Body(..., embed=True, alias="url")):
    if not valid_url(url):
        raise HTTPException(status_code=400, detail="invalid url")

    youtube = FileHandler(url)

    path = youtube.down_load_file()

    return FileResponse(path)
