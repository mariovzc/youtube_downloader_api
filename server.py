from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import FileResponse
from file_handler import FileHandler
from schema import Item


app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}


@app.post("/downloads")
def download_file(item: Item):
    try:
        youtube = FileHandler(item.url)
        path = youtube.down_load_file()
        return FileResponse(path)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error Procesando la Peticion. Detalle - {repr(e)}"
        )
