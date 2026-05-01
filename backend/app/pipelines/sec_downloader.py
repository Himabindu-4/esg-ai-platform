from sec_edgar_downloader import Downloader
from pathlib import Path


BASE_DIR = Path("app/data/raw/sec_filings")

BASE_DIR.mkdir(parents=True, exist_ok=True)


def download_10k(ticker: str):

    print(f"\nDownloading 10-K filings for {ticker}...\n")

    dl = Downloader(
        company_name="ESG AI Research",
        email_address="research@esgai.com",
        download_folder=str(BASE_DIR)
    )

    # OLD LIBRARY VERSION
    dl.get(
        "10-K",
        ticker
    )

    print(f"\nDownload completed for {ticker}\n")


if __name__ == "__main__":
    download_10k("AAPL")