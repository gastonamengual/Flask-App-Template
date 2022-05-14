# Flask-App-Template

Code for a Flask App.

# Firebase initialization

1. Create an app in Firebase in Firebase -> Project Settings -> General.
2. In Firebase -> Project Settings -> Service Account, generate new private key.
3. Copy the content to credentials.json.
4. Create a firestore database in the firebase UI.
5. Create an empty collection to be deleted later (otherwise it throws 400 The Cloud Firestore API is not available for Datastore Mode projects).
6. Start the app.