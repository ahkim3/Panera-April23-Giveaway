import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import requests
import time


# Define Google Sheets credentials
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

url = "https://www.panerabread.com/content/panerabread_com/en-us/legal/fine-print/free-faves-thru-end-of-year-giveaway/free-faves-alternative-entry-form/_jcr_content/root/panera_form_copy_cop.paneraForm"
data = {
    "name": "Andrew Kim",
    "emailAddress": "andrewhkim3@gmail.com",
    "MypaneraMemberNumber": "622071712765",
}


sheet = client.open("Panera-April23-Giveaway-Counter").sheet1


# Read counter from file
try:
    with open("counter.txt", "r") as f:
        counter = int(f.read())
except FileNotFoundError:
    print("Counter file not found. Creating new counter file...")
    counter = 0
    with open("counter.txt", "w") as f:
        f.write(str(counter))


# Main loop
try:
    while True:
        delay = random.randint(4, 12)

        # Submit form
        response = requests.post(url, data=data)

        # Check if form was submitted successfully
        if (
            response.status_code == 200
            and "<h4>Your submission was successful!</h4>" in response.text
        ):
            counter += 1

            print("Form submitted successfully (counter: " + str(counter) + ")")
            with open("counter.txt", "w") as f:
                f.write(str(counter))

            # Update every 75 submissions
            if counter % 75 == 0:
                # Get the current date and time and format it as a string
                now = datetime.datetime.now()
                date_str = now.strftime("%m/%d/%Y")
                time_str = now.strftime("%I:%M:%S %p")

                # Update Google Sheets
                try:
                    row = [date_str, time_str, counter]
                    sheet.update_cell(2, 1, date_str)  # Update date in cell A2
                    sheet.update_cell(2, 2, time_str)  # Update time in cell B2
                    sheet.update_cell(2, 3, counter)  # Update counter in cell C2
                    print("Google Sheets updated successfully")
                except gspread.exceptions.APIError as e:
                    print("Google Sheets API Error:", e)
                except Exception as e:
                    print("Error when updating Google Sheets:", e)

        else:
            print(
                "Form submission failed (status code: "
                + str(response.status_code)
                + ")"
            )

        # Delay for a random amount of time
        for i in range(delay):
            print("Delay: ", end="")
            print(delay - i, end=" seconds remaining... \r")
            time.sleep(1)
except KeyboardInterrupt:
    print("    Program terminated             ")
