import re


def slugify(text: str) -> str:
    text = re.sub(r"[éèë]", "e", text)
    text = re.sub(r"ï", "i", text)
    text = re.sub(r" ", "_", text)
    return text.lower()
