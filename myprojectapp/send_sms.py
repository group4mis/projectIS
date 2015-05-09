from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC0dbe984e7ecafdde289771dd8cca4907"
auth_token  = "{{AC0dbe984e7ecafdde289771dd8cca4907}}"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="A new notification from Student portfolio website!",
    to="+96566422661",    # Replace with your phone number
    from_="+1 (205) 791-7808") # Replace with your Twilio number
print message.sid
