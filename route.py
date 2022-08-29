import urllib.parse

from fastapi import FastAPI, Query
from starlette.responses import RedirectResponse

from poerty import *

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "hello fastapi"}


@app.get("/poetry/random")
async def random_poetry():
    return get_random_poetry_dict()


@app.get("/poetry/naming/")
async def random_name_from_poetry(
        family_name: str = Query(max_length=5, min_length=1, title="姓氏", description="传入姓氏",
                                 regex="[\u4E00-\u9FFF]+")):
    return family_name + get_random_two_words_from_poetry(get_random_poetry())[1]


@app.get("/word")
def get_word_explanation(word: str):
    redirect_response = RedirectResponse(
        url="https://hanyuapp.baidu.com/dictapp/word/detail_getworddetail?wd=%s" % urllib.parse.quote_plus(word)
    )
    return redirect_response
