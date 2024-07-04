import streamlit as st
from st_pages import hide_pages
from time import sleep

# Class definitions
class User:
    def __init__(self, name, password, phoneNumber, email, age):
        self.name = name
        self.password = password
        self.phoneNumber = phoneNumber
        self.email = email
        self.age = age
        self.signedIn = False
        self.cart = Cart()

    def signIn(self, email, password):
        self.signedIn = (self.email == email) & (self.password == password)
        return self.signedIn

    def signOut(self):
        self.signedIn = False


class Restaurant:
    def __init__(self, name, rating , logo):
        self.logo = logo
        self.name = name
        self.rating = rating
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)

    def remove_item(self, item):
        self.menu.remove(item)

    def get_menu(self):
        return self.menu


class Item:
    def __init__(self, name, price, calorie):
        self.name = name
        self.price = price
        self.calorie = calorie


class Cart:
    def __init__(self):
        self.items = {}  # {"item obj 1": 1, "item obj 2:" 4}
        self.num_of_items = 0
        self.total_price = 0.0

    def add_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name] += quantity
        else:
            self.items[item.name] = quantity

        self.num_of_items += quantity
        self.total_price += item.price * quantity

    def remove_item(self, item, quantity=1):
        if item.name in self.items:
            if self.items[item.name] > quantity:
                self.items[item.name] -= quantity
                self.num_of_items -= quantity
                self.total_price -= item.price * quantity
            elif self.items[item.name] == quantity:
                self.num_of_items -= quantity
                self.total_price -= item.price * quantity
                del self.items[item.name]

    def display_cart(self):
        total = 0
        if not self.items:
            return "Your cart is empty."
        else:
            cart_contents = "Your cart:\n"
            for item_name, quantity in self.items.items():
                cart_contents += f"Item: {item_name}, Quantity: {quantity}, Total Price: ${self.items[item_name] * quantity:.2f}\n"
            return cart_contents


class Tracking:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "Preparing"

    def update_status(self, new_status):
        self.status = new_status
        return f"Order {self.order_id} status updated to {self.status}"


# Initialize some objects for demonstration
user = User("John Doe", "admin1234", "123-456-7890", "john@example.com", 22)

Mac = Restaurant("McDonalds", 5.7 , "C:\\Users\\abdul\\Downloads\\mc.jpeg")
Albaik = Restaurant("Albaik", 7.3,"C:\\Users\\abdul\\Downloads\\albaik.jpeg")
PizzaHut = Restaurant("PizzaHat", 9.3,"C:\\Users\\abdul\\Downloads\\Pizzhut.jpeg")

restaurant = [Mac,Albaik,PizzaHut]


item1 = Item("BigMac", 12.99, 500)
item2 = Item("Double Cheese Burger", 15.99, 600)
item3 = Item ("CokaCoal" , 7.99 , 200)

Mac.add_item(item1)
Mac.add_item(item2)
Mac.add_item(item3)

item4 = Item("Nugget", 14.99, 500)
item5 = Item("Fried Chicken ", 13.99, 600)
item6 = Item ("CocaCoal" , 7.99 , 200)

Albaik.add_item(item4)
Albaik.add_item(item5)
Albaik.add_item(item6)

item7 = Item("Margherita Pizza", 24.99, 500)
item8 = Item("Pepperoni Pizza", 23.99, 600)
item9 = Item ("Supreme Pizza" , 30.99 , 200)

PizzaHut.add_item(item7)
PizzaHut.add_item(item8)
PizzaHut.add_item(item9)


# Streamlit app


st.title("Food Ordering Application")


# Sidebar for navigation
# st.sidebar.title("Navigation")

hide_pages(["User","Restaurant","Menu","Cart","Order Tracking","main"])

markdown = """
Project Members :\n
1- Abdulrahman \n
2- Alaa \n
3- Summyah\n
4- Asmaa\n
5- Azzam \n
6- Hassan
"""

logo = "C:\\Users\\abdul\\Downloads\\WhatsApp Image 2024-07-03 at 15.31.11_342ea33f.jpg"
st.sidebar.image(logo)
st.sidebar.info(markdown)
page = st.sidebar.radio("Go to", ["User", "Restaurant", "Menu", "Cart", "Order Tracking"])
if page == "User":
    st.header("User Management")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        signed_in = user.signIn(email, password)
        if signed_in:
            st.success("Logged in successfully!")
            sleep(2)
        else:
            st.error("Invalid username or password")
    # if st.button("Sign Out"):
    #     user.signOut()
    #     st.write("Signed Out")

menu_restaurant = 0

if page == "Restaurant":
    c1, c2 = st.columns([3, 5])
    for idx , i in enumerate(restaurant):
        with c1:
            st.header(i.name)
            st.write(f"Restaurant Rating: {i.rating}")
            if st.button(f"Go to {i.name}"):
                menu_restaurant = idx
        with c2:
            st.image(i.logo)


if page == "Menu":
    st.header(f"Menu {restaurant[menu_restaurant].name}")
    menu_items = restaurant[menu_restaurant].get_menu()
    st.divider()
    for item in menu_items:
        st.write(f"Item  : {item.name}")
        st.write(f"Price  : {item.price}")
        st.write(f"Cal  : {item.calorie}")
        st.button("Add to Cart",item.name)
        st.divider()

if page == "Cart":
    st.header("Cart")
    st.write(user.cart.display_cart())
    if st.button("Add Spaghetti to Cart"):
        user.cart.add_item(item1)
    if st.button("Add Lasagna to Cart"):
        user.cart.add_item(item2)
    if st.button("Remove Spaghetti from Cart"):
        user.cart.remove_item(item1)
    if st.button("Remove Lasagna from Cart"):
        user.cart.remove_item(item2)
    st.write(user.cart.display_cart())

if page == "Order Tracking":
    st.header("Order Tracking")
    tracking = Tracking(order_id=1)
    st.write(f"Order Status: {tracking.status}")
    if st.button("Update Status to 'Shipped'"):
        st.write(tracking.update_status("Shipped"))
    if st.button("Update Status to 'Delivered'"):
        st.write(tracking.update_status("Delivered"))
