class Restaurant:
    def __init__(self, restaurant_id, name, cuisine, menu, rating, is_open):
        self.restaurant_id = restaurant_id
        self.name = name
        self.cuisine = cuisine
        self.menu = menu 
        self.rating = rating
        self.is_open = is_open

    def add_menu_item(self, item_name, price):
        self.menu[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.menu:
            del self.menu[item_name]
            print("item is deleted")

    def accept_order(self, order):
        if self.is_open:
            print(f"Order accepted: {order}")
        else:
            print("Sorry, we are currently closed.")

    def reject_order(self, order):
        print(f"Order rejected: {order}")


class MenuItem:
    def __init__(self, itemid, name, price, category, is_available, preparationtime):
        self.itemid = itemid
        self.name = name
        self.price = price
        self.category = category
        self.is_available = is_available
        self.preparationtime = preparationtime
    def update_price(self, new_price):
        self.price = new_price
        print(f"Price of {self.name} updated to {self.price}")
    def mark_unavailable(self):
        self.is_available = False
        print(f"{self.name} is unavailable")
class Order:
    def __init__(self, orderid, customerid, restaurantid, items, totalprice, status):
        self.orderid = orderid
        self.customerid = customerid
        self.restaurant_id = restaurantid
        self.items = items
        self.totalprice = totalprice
        self.status = status  
        def place_order(self):
            self.status = "Placed"
            print(f"Order {self.orderid} placed successfully")
        def cancel_order(self):
            self.status = "Cancelled"
            print(f"Order {self.orderid} cancelled")
        def update_status(self, new_status):
            self.status = new_status
            print(f"Order {self.orderid} status updated to {self.status}")
        def getETA(self):
            print(f"Estimated time of arrival for order {self.order_id} is 30 minutes")
class DeliveryPartner:
    def __init__(self, partner_id, name, phone, location, is_available, rating):
        self.partner_id = partner_id
        self.name = name
        self.phone = phone
        self.location = location
        self.is_available = is_available
        self.rating = rating
        def accept_delivery(self, order_id):
            if self.is_available:
                print(f"Delivery partner {self.name} accepted")
            else:
                print(f"Delivery partner {self.name} is not available")
        def update_location(self, new_location):
            self.location = new_location
            print(f"Delivery partner {self.name} location updated to {self.location}")
        def markdelivered(self, order_id):
            print(f"Order {order_id} marked as delivered by {self.name}")
class Cart:
    def __init__(self, cartid, customer_id, items, promocode):
        self.cartid = cartid
        self.customer_id = customer_id
        self.items = items
        self.promocode = promocode
        def add_item(self, item_name, price):
            self.items[item_name] = price
            print(f"Added {item_name} to cart")
        def remove_item(self, item_name):
            if item_name in self.items:
                del self.items[item_name]
                print(f"Removed {item_name} from cart")
            else:
                print(f"{item_name} not found in cart")
        def applypromocode(self, code):
            self.promocode = code
            print(f"Applied promocode: {code}")
        def checkout(self):
            total_price = sum(self.items.values())
            print(f"Total price: {total_price}")
class Rating:
    def __init__(self, rating_id, order_id, restaurantrating, deliveryrating, review):
        self.rating_id = rating_id
        self.order_id = order_id
        self.restaurantrating = restaurantrating
        self.deliveryrating = deliveryrating
        self.review = review
        def submit_rating(self):
            print(f"Rating submitted for order {self.order_id}")
        def validate_rating(self):
            if 1 <= self.restaurantrating <= 5 and 1 <= self.deliveryrating <= 5:
                print("Rating is valid")
            else:
                print("Rating must be between 1 and 5")
class deliveryFee:
    def __init__(self, fee_id, restaurant_id, distance, fee_amount):
        self.fee_id = fee_id
        self.restaurant_id = restaurant_id
        self.distance = distance
        self.fee_amount = fee_amount
        def calculate_fee(self):
            if distance>=0 and distance<=3:
                self.fee_amount+= 20
            elif distance>3 and distance<=8:
                self.fee_amount+= 40 
            elif distance>8 and distance<=15:
                self.fee_amount+= 70
            else:
                print("not serviceable")
            print(self.fee_amount)
c = Restaurant(19, "Hotel ABC", "South Indian", {}, 4.5, True)
c.add_menu_item("Idli", 20)
c.remove_item("Idli")

