import re

def find_authors(text: str) -> list[str]:
    authors = []
    match = re.search(r"Autor:in\s+(.*?)\s+Lesezeit", text)
    if match:
        authors = [match.group(1).strip()]
    else:
        match1 = re.search(r"Autor:innen\s+([\s\S]*?)\s+Lesezeit", text)
        if match1:
            authors = re.split(r'\s\s+', match1.group(1).strip())
    return authors   
    
def find_publish_date(text: str) -> str:
    date = ""
    pattern = r"(\d{2}\.\d{2}\.\d{4})\s+(.*?)\s+Autor:in"
    match = re.search(pattern, text)
    if match:
        date = match.group(1)
    return date
    
def find_title(text: str) -> str:
    title = ""
    pattern = r"\d{2}\.\d{2}\.\d{4}\s+(.*?)\s+Autor:in"
    match = re.search(pattern, text)
    if match:
        title = match.group(1)
    return title
    
def find_start(text: str, title: str) -> int:
    path = f"Home / Blog / {title}"
    return text.index(path) + len(path)
    
def find_end(text: str) -> int:
    pattern = r"Tags:\s+(.*?)\s+Share:"
    match = re.search(pattern, text)
    if match:
        t = match.group(0)
        return text.index(t)
    else:
        return len(text)
