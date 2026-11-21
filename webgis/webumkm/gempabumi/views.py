
import json
from urllib.request import Request, urlopen
from django.shortcuts import render


def gempaterkini(request):
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"

    gempa = []
    error = None

    try:
        req = Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8",
                "Referer": "https://data.bmkg.go.id/",
            }
        )

        with urlopen(req, timeout=20) as response:
            data = json.loads(
                response.read().decode("utf-8")
            )

        gempa = data.get(
            "Infogempa", {}
        ).get("gempa", [])[:15]

    except Exception as e:
        error = f"Gagal mengambil data BMKG: {e}"

    return render(
        request,
        "gempabumi/gempabumi.html",
        {
            "gempa": gempa,
            "error": error
        }
    )
