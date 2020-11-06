class User:
    def log(self):
        print(self)
class Teacher(User):
    def log(self):
        print('I am a Teacher')

class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        return self.name +" "+ self.membership_type

c = Customer("Tajveez", "Premium")
# print(c.name, c.membership_type)

c2 = Customer("Hamza", "SuperPremium")
# print(c2.name, c2.membership_type)

customers = [c, c2]
# print(customers[0].name)
customers[0].update_membership("Gold")
# print(customers[0].membership_type)
# print(customers[0].log())

users = [Customer('Awais', 'Diamond'), Teacher()]

for user in users:
    user.log()

# # Dynamic attributes adding
# customers[1].verified = True
# print(customers[1].verified)
