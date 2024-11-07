import time
import requests

from .config import BASE_URL, HEADERS, REQUEST_DELAY, RETRY_ATTEMPTS, RETRY_BACKOFF

def fetch_page(url):
    """Fetch a page with retries and delay."""
    attempt = 0
    while attempt < RETRY_ATTEMPTS:
        try:
            response = requests.get(f"{BASE_URL}{url}", headers=HEADERS)
            response.raise_for_status()
            time.sleep(REQUEST_DELAY)  # Respect the rate limit
            return response.text
        except requests.exceptions.RequestException as e:
            attempt += 1
            time.sleep(RETRY_BACKOFF ** attempt)
            if attempt == RETRY_ATTEMPTS:
                print(f"Failed to fetch page after {RETRY_ATTEMPTS} attempts.")
                raise e