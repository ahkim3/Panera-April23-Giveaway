import random
import requests
import time


url = "https://www.panerabread.com/content/panerabread_com/en-us/legal/fine-print/free-faves-thru-end-of-year-giveaway/free-faves-alternative-entry-form/_jcr_content/root/panera_form_copy_cop.paneraForm"
data = {
    "name": "Andrew Kim",
    "emailAddress": "andrewhkim3@gmail.com",
    "MypaneraMemberNumber": "622071712765",
}


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
        delay = random.randint(3, 12)

        # Submit form
        response = requests.post(url, data=data)

        # Check if form was submitted successfully
        if (
            response.status_code == 200
            and "<h4>Your submission was successful!</h4>" in response.text
        ):
            print("Form submitted successfully (counter: " + str(counter) + ")")
            with open("counter.txt", "w") as f:
                f.write(str(counter))

            counter += 1
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
