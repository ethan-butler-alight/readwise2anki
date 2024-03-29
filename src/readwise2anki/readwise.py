"""Readwise module which is used for retrieving a user's Readwise highlights"""

import datetime
import pprint
import requests
from aqt import mw

class Readwise:
    def __init__(self):
        config = mw.addonManager.getConfig(__name__)
        self.token = config["API_KEY"]
        self.data = None
        self.highlights = None
        self.current_highlight = None
        self.current_book = None
        self.total_books = 0
        self.total_highlights = 0
        self.fetch_from_export_api()
        self.calc_num_highlights()

    def fetch_from_export_api(self, updated_after=None) -> None:
        """Retrieve all highlights from the user's Readwise account. This is based off the example code given at: https://readwise.io/api_deets"""
        full_data = []
        next_page_cursor = None
        while True:
            params = {}
            if next_page_cursor:
                params["pageCursor"] = next_page_cursor
            if updated_after:
                params["updatedAfter"] = updated_after
            print("Making export api request with params " + str(params) + "...")
            response = requests.get(
                url="https://readwise.io/api/v2/export/",
                params=params,
                headers={"Authorization": f"Token {self.token}"},
                verify=True,
                timeout=20,
            )

            full_data.extend(response.json()["results"])
            next_page_cursor = response.json().get("nextPageCursor")
            if not next_page_cursor:
                break

        # Save only books with highlights
        self.data = [book for book in full_data if book["highlights"]]

    def calc_num_highlights(self):
        # """Calculate the total number of highlights from the data/"""
        books = []
        if self.data is not None:
            # print highlights
            for book in self.data:
                if book["highlights"]:
                    # print(book["title"])
                    self.total_books += 1
                    # if book["book_tags"] != []:
                    #     print(book["book_tags"])

                    books.append(book["title"])
                    for highlight in book["highlights"]:
                        self.total_highlights += 1
                        # print(f"\t {highlight['text']} \n")
                        # if highlight["tags"] != []:
                        # print(highlight["tags"])

                    print("\n\n\n")

        else:
            print("You need to retrieve highlights from the API first")

    def get_source_and_highlight(self, highlight_number):
        """Given a highlight number, return the source's title and highlight
        A highlight number is the ID which represents the current highlight in the collection of all highlights.
        """
        if self.data is not None:
            highlight_count = 0
            source_count = 0
            source_highlight_count = 0

            for source in self.data:
                if source["highlights"]:
                    if highlight_count == highlight_number:
                        title = source["title"]
                        highlight = source["highlights"][source_highlight_count]["text"]
                        return title, highlight

                    highlight_count += 1
                    source_highlight_count += 1

                source_highlight_count = 0
                source_count += 1

    def get_source(self, source_number):
        """Given a source number, return the source's title"""
        return self.data[source_number]["title"]

    def get_highlight(self, source_number, source_highlight_number):
        """Given a source number and a source highlight number, return the highlight"""

        return self.data[source_number]["highlights"][source_highlight_number]["text"]


def main():
    """Main function used for testing"""
    # Get all of a user's books/highlights from all time
    account = Readwise()

    # Pretty print data
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(account.data)
    print(account.get_source(0))
    print(account.get_highlight(0, 0))

    # TODO: Implement this after you properly create cards from all data
    # # Later, if you want to get new highlights updated since your last fetch of allData, do this.
    # last_fetch_was_at = datetime.datetime.now() - datetime.timedelta(
    #     days=1
    # )  # use your own stored date

    # new_data = fetch_from_export_api(last_fetch_was_at.isoformat())


if __name__ == "__main__":
    main()
