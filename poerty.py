import json
import os
import random
import re

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List, Any

from itertools import chain

poetry_files: list[str] = os.listdir("./res")


class Poetry:
    source: str
    author: str
    title: str
    chapter: str
    section: str
    content: List[str]

    def __init__(
            self,
            **kwargs
            # source: str,
            # title: str,
            # content: List[str],
            # author: str = "佚名",
            # chapter: str = "",
            # section: str = "",
    ) -> None:
        self.source = kwargs.get("source", "")
        self.author = kwargs.get("author", "佚名")
        self.title = kwargs.get("title", "")
        self.chapter = kwargs.get("chapter", "")
        self.section = kwargs.get("section", "")
        self.content = kwargs.get("content", kwargs.get("paragraphs", []))

    @staticmethod
    def new_poetry(d: dict) -> "Poetry":
        return Poetry(**d)

    def to_dict(self) -> "dict":
        return {"title": self.title, "chapter": self.chapter, "section": self.section, "content": self.content}

    def __str__(self):
        d = self.to_dict()
        return str(d)


def get_random_poetry_dict() -> "dict":
    return get_random_poetry().to_dict()


def get_random_poetry() -> Poetry:
    return random.choice(poetries)


def init_poetries():
    poetry_json: list[Poetry] = []
    for json_file_path in poetry_files:
        with open("./res/%s" % json_file_path, "rb") as f:
            poetry_json_list = [set_default_source_to_poetry_dict(dd, json_file_path.removesuffix(".json"))
                                for dd in json.load(f)]
            poetry_json.extend([Poetry.new_poetry(ii) for ii in poetry_json_list])
    return poetry_json


def set_default_source_to_poetry_dict(d: dict, source: str) -> dict:
    d["source"] = source
    return d


def get_random_two_words_from_poetry(poetry: Poetry) -> List[str]:
    lines = list(chain(*[ii.split("。") for ii in poetry.content]))
    lines = remove_empty_str(lines)
    line: str = random.choice(lines)
    return [line, "".join(random.choices(purify_poetry_line(line), k=2))]


def remove_empty_str(str_list: List[str]):
    return [ii for ii in str_list if len(ii) > 0]


purify_pattern = "[,，?？！!死屎尸]"


def purify_poetry_line(line: str):
    return re.sub(purify_pattern, "", line)


poetries: list[Poetry] = init_poetries()
