import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

def fetch(url: str):

    r = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    r.raise_for_status()

    return r.text
