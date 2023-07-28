import pyrebase as pb
config={"apiKey": "AIzaSyB4s-zOO50DyIduVkWWYb9c6c1DT97VBqg",
    "authDomain": "myshop-76cba.firebaseapp.com",
    "databaseURL": "https://myshop-76cba.firebaseio.com",
    "projectId": "myshop-76cba",
    "storageBucket": "",
    "messagingSenderId": "187498078910",
    "appId": "1:187498078910:web:29abd27a8f762f6b0174ef"
      }
i=0
while i<50:
    i=i+1
    firebase=pb.initialize_app(config)
    x=firebase.database().child("College").get()
    y=firebase.database().child("College")
    cc=[]
    for u in x.each():
        cc.append(u.val())
    print(cc[2])
    if cc[2]==1:
        y.child("id").set(0)
        db=firebase.database().child("College")
        ans={"ans":cc[0]/2}
        db.child("ans").set(cc[0]/2)
        print(cc[0]/2)
    if cc[2]==99:
        break

