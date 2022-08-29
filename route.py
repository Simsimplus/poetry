from fastapi import FastAPI
from poerty import *

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "hello fastapi"}


@app.get("/poetry/random")
async def random_poetry():
    return get_random_poetry_dict()


@app.get("/poetry/naming/")
async def random_name_from_poetry(family_name: str):
    return family_name + get_random_two_words_from_poetry(get_random_poetry())[1]
