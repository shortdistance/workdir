from firebase import firebase
firebase = firebase.FirebaseApplication('https://share-time-new.firebaseio.com/', None)
result = firebase.get('/users')
print result