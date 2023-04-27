"""Readwise module which is used for retrieving a user's Readwise highlights"""

import datetime
import pprint
import requests
from decouple import config  # type: ignore

token = config("API_KEY")


def fetch_from_export_api(updated_after=None):
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
            headers={"Authorization": f"Token {token}"},
            verify=True,
            timeout=20,
        )
        full_data.extend(response.json()["results"])
        next_page_cursor = response.json().get("nextPageCursor")
        if not next_page_cursor:
            break
    return full_data


def main():
    """Main function used for testing"""
    # Get all of a user's books/highlights from all time
    all_data = fetch_from_export_api()

    # Pretty print data
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(all_data)

    # TODO: Implement this after you properly create cards from all data
    # # Later, if you want to get new highlights updated since your last fetch of allData, do this.
    # last_fetch_was_at = datetime.datetime.now() - datetime.timedelta(
    #     days=1
    # )  # use your own stored date

    # new_data = fetch_from_export_api(last_fetch_was_at.isoformat())


if __name__ == "__main__":
    main()
