# rym_scraper/config.py

# Base URL of RateYourMusic (RYM) for constructing requests
BASE_URL = "https://rateyourmusic.com"

# Headers for HTTP requests to mimic a real browser request
# These are important to avoid being blocked or flagged by anti-bot systems.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Rate limiting settings (in seconds)
# This helps avoid overwhelming the server by limiting how frequently requests are made.
REQUEST_DELAY = 1.0  # Time in seconds to wait between requests

# Retry settings
# Helps manage failed requests due to temporary network issues or server responses.
RETRY_ATTEMPTS = 3      # Number of retry attempts for failed requests
RETRY_BACKOFF = 2       # Backoff multiplier for retries (exponential backoff)

# Parsing settings
# Customize based on RYM's HTML structure if needed
ALBUM_SELECTOR = "div.album_title"  # Example CSS selector for album titles
GENRE_SELECTOR = "div.genre"        # Example CSS selector for genre tags

# Logging settings
# Enable logging for debugging purposes if desired.
LOGGING_ENABLED = True
LOG_FILE_PATH = "logs/rym_scraper.log"
