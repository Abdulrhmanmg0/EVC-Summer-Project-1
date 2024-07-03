from Cart import Cart


class User:
    """ 
    A class to represent a User.
    ...
    Attributes
    ----------
    name : string 
    password : int 
    phoneNumber : int 
    email : str 
    age : int 
    signedIn : boolean
    cart : Cart object

    Methods
    -------
    signIn : makes signedIn = True in if password is correct, else prints false
    signOut : makes signedIn = False
    """
    def __init__(self, name, password, phoneNumber, email, age):
        self.name = name 
        self.password = password 
        self.phoneNumber = phoneNumber
        self.email = email
        self.age = age
        self.signedIn = False
        # TODO: INITIALIZE CART OBJECT BASED ON CART CLASS
        self.cart = Cart()


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
    
    def getCart(self):
        return self.cart
