# Panera Bread April 23 Giveaway Counter

![Successful Submissions](https://shields.io/endpoint?url=https%3A%2F%2Fcellshield.info%2Fgs%3FspreadSheetId%3D1unWHFP-te-WIohFQgvvgmygrP2HV3clMSX-ZcG28iyg%26cellRange%3DC2&label=Successful%20Submissions&color=success&style=for-the-badge&logoWidth=150&logoHeight=40?)

This script automatically submits an alternative entry form for the Panera Bread April 23 Giveaway every few minutes, and keeps track of the number of successful submissions in a Google Sheets document, as well as locally.

## Requirements

-   Python 3.6 or higher
-   Required Python packages: requests, gspread, oauth2client

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/username/panera-giveaway-counter.git
    ```

2. Install the required packages using pip:

    ```bash
    pip install requests gspread oauth2client
    ```

3. Follow the instructions in the [gspread](https://gspread.readthedocs.io/en/latest/oauth2.html) documentation to create a `credentials.json` file that contains your Google Sheets API credentials.

4. Share the Google Sheets document with the email address associated with the `client_email` field in your `credentials.json` file.

## Usage

1. Run the script using the following command:

    ```bash
    python main.py
    ```

2. The script will submit the form every few minutes and update the counter in the Google Sheets document.

3. To view the counter, open the Google Sheets document and look at the value in cell A1.
