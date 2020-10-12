from typing import Optional
from fastapi import HTTPException

from fastapi import FastAPI
from pydantic import BaseModel, validator
from tools import valid_url


class Item(BaseModel):
    url: str

    @validator('url')
    def check_url(cls, v):
        if not valid_url(v):
            raise HTTPException(status_code=400, detail="invalid url")
        return v
