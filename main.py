import random
import requests
import time


counter = 0

url = "https://www.panerabread.com/en-us/legal/fine-print/free-faves-thru-end-of-year-giveaway/free-faves-alternative-entry-form/_jcr_content/root/panera_form_copy.paneraForm"
data = {
    "name": "Andrew Kim",
    "emailAddress": "andrewhkim3@gmail.com",
    "MypaneraMemberNumber": "622071712765"
}

try:
    while (True):
        delay = random.randint(10, 30)

        response = requests.post(url, data=data)

        if response.status_code == 200:
            print("Form submitted successfully (counter: " + str(counter) + ")")
            counter += 1
        else:
            print("Form submission failed (status code: " +
                  str(response.status_code) + ")")

        # Delay for a random amount of time
        for i in range(delay):
            print("Delay: ", end="")
            print(delay - i, end=" seconds remaining... \r")
            time.sleep(1)
except KeyboardInterrupt:
    print("    Program terminated             ")
