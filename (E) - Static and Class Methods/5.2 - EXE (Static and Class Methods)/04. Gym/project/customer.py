class Customer:
    id: int = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        Customer.id += 1

    @staticmethod
    def get_next_id():
        next_id = Customer.id
        return next_id

    def __repr__(self) -> str:
        customer_id = self.id
        name = self.name
        address = self.address
        email = self.email
        return f"Customer <{customer_id}> {name}; Address: {address}; Email: {email}"


# from project.class_id_mixin import ClassIdMixin
#
#
# class Customer(ClassIdMixin):
#     id: int = 0
#
#     def __init__(self, name: str, address: str, email: str):
#         self.name = name
#         self.address = address
#         self.email = email
#         self.id = self.get_next_id()
#         Customer.id += 1
#
#     def __repr__(self) -> str:
#         customer_id = self.id
#         name = self.name
#         address = self.address
#         email = self.email
#         return f"Customer <{customer_id}> {name}; Address: {address}; Email: {email}"
