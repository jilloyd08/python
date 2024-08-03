from twilio.rest import Client

account_sid = ' ' #enter twilio account sid
auth_token = ' ' #enter twilio auth token
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=' ', # enter sender's number
  body='Wow this works!', # type any message you like.
  to=' '# enter recipent's number
)

print(message.sid)