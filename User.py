class User:
  
    def __init__(self, name, password, phoneNumber, email, age):
        self.name = name 
        self.password = password 
        self.phoneNumber = phoneNumber
        self.email = email
        self.age = age
        self.signedIn = False
      

    def signIn(self, email, password):
        self.signedIn = (self.email == email) & (self.password == password)
        print(self.signedIn)
        if not (self.signedIn):
            print("Wrong password. Try again.")
    
    def signOut(self): 
        self.signedIn = False

    def getUserName(self):
        return self.name

    def getEmail(self):
        return self.email
    
    def getPhoneNumber(self): 
        return self.phoneNumber 
    
    def getSignedIn(self):
        return self.signedIn
