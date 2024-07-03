class Tracking:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "Preparing"  

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order {self.order_id} status updated to {self.status}")
