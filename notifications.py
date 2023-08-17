import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def sendPush(title, msg,topic="test"):
    message = messaging.Message(
    notification=messaging.Notification(
        title=title,
        body=msg
    ),
    topic="live"  # Replace with your app's topic
)

# Send the notification
    response = messaging.send(message)
    print("Successfully sent message:", response)