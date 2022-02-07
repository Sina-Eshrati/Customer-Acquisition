import requests

print("Welcome to Sina's Flight Club.")
print("We find the best flight deals and email you.")

first_name = (input("What is your first name?\n")).title()
last_name = (input("What is your last name?\n")).title()
email = input("What is your email?\n")

is_email_correct = False
while not is_email_correct:
    retype_email = input("Type your email again.\n")
    if email == retype_email:
        print("Success your email has been added! You are now in the club!")
        is_email_correct = True

sheety_endpoint = "https://api.sheety.co/42590b54a1ac71c7ac63510780eea096/flightDeals/users"
user_data = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}
response = requests.post(sheety_endpoint, json=user_data)