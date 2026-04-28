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
v=Rating(44,55,2,3,"good")
v.submit_rating(self)
