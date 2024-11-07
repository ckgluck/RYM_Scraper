# rym_scraper/url_builder.py

from urllib.parse import urlencode


class URLBuilder:
    BASE_URL = "https://rateyourmusic.com"

    def __init__(self):
        self.endpoint = "/charts/top/album"
        self.params = {}

    def set_genre(self, genre):
        """Set a genre for filtering (e.g., 'rock', 'jazz')."""
        self.params["lg"] = genre
        return self

    def set_year(self, year):
        """Set a specific year to filter results (e.g., '2023')."""
        if isinstance(year, int):
            self.endpoint += f"/{year}"
        return self

    def set_decade(self, decade):
        """Set a decade to filter results (e.g., '1980s')."""
        if isinstance(decade, int) and 1900 <= decade <= 2020:
            self.endpoint += f"/{decade}s"
        return self

    def set_descriptor(self, descriptor):
        """Add a descriptor to filter results (e.g., 'moody', 'energetic')."""
        # Multiple descriptors can be chained by adding more `descriptor` parameters
        if "desc" in self.params:
            self.params["desc"] += f",{descriptor}"
        else:
            self.params["desc"] = descriptor
        return self

    def set_sort_by(self, sort_option):
        """Sort results by rating or popularity (e.g., 'rating' or 'popularity')."""
        if sort_option in ["rating", "popularity"]:
            self.params["sort"] = sort_option
        return self

    def build(self):
        """Construct the full URL with the base URL, endpoint, and parameters."""
        url = f"{self.BASE_URL}{self.endpoint}"
        if self.params:
            url += "?" + urlencode(self.params)
        return url


# FOR TESTING
def main():
    # Example URL for top rock albums in 2020, sorted by rating
    builder = URLBuilder()
    url_2020_rock = (builder
        .set_genre("rock")
        .set_year(2020)
        .set_sort_by("rating")
        .build())
    print("Top Rock Albums in 2020 (Rating):", url_2020_rock)

    # Example URL for jazz albums in the 1980s with a 'moody' descriptor, sorted by popularity
    builder = URLBuilder()
    url_jazz_1980s_moody = (builder
        .set_genre("jazz")
        .set_decade(1980)
        .set_descriptor("moody")
        .set_sort_by("popularity")
        .build())
    print("Jazz Albums in 1980s (Moody, Popularity):", url_jazz_1980s_moody)


if __name__ == "__main__":
    main()