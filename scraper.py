import os
import requests
from bs4 import BeautifulSoup


def get_site_context():
    """Intenta obtener contenido relevante del sitio web de Amandarina.
    Si falla, devuelve un resumen seguro por defecto.
    """
    url = os.getenv("SITE_URL", "https://amandarina.com")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        fragments = []
        h1 = soup.find("h1")
        if h1 and h1.get_text(strip=True):
            fragments.append(h1.get_text(strip=True))

        paragraphs = soup.find_all("p")
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:
                fragments.append(text)
            if len(fragments) >= 3:
                break

        site_text = " ".join(fragments).strip()
        if site_text:
            return site_text

    except Exception as exc:
        print(f"Warning: No se pudo obtener contexto del sitio {url}: {exc}")

    return (
        "Amandarina es una agencia digital especializada en desarrollo de aplicaciones móviles, "
        "software a medida y soluciones de IA en Bucaramanga, Colombia."
    )
