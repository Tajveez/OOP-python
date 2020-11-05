class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    def update_membership(self, new_membership):
        self.membership_type = new_membership

c = Customer("Tajveez", "Premium")
# print(c.name, c.membership_type)

c2 = Customer("Hamza", "SuperPremium")
# print(c2.name, c2.membership_type)

customers = [c, c2]
print(customers[0].name)
customers[0].update_membership("Gold")
print(customers[0].membership_type)


# # Dynamic attributes adding
# customers[1].verified = True
# print(customers[1].verified)
