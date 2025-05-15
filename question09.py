#a) class Customer(Person) creates a child class Customer under the parent class Person.
#a) The child class Customer will have all the attributes of the Person class plus any unique attributes.
#b) This method creates attributes for the class, in this case, it is creating a field for information to
#b) be stored that is associated with that specific class. When you later go to instantiate
#b) an object, you need to use these attributes to create an object or instance of a class.
"""c"""
class  Person():
    def __init__(self, eye_color):
        self.eye_color = eye_color
"""d"""
#set up a list to append customer instance too
customer_list = []
#create Customer class and set its attribute in this case I chose what currency the customer pays in
class Customer():
    def __init__(self, currency_paid):
        self.currency_paid = currency_paid
#creates an instance of a customer under the Customer class. It is being different than when
#I went to append objects to a list in my game as the parameters would come right up
#and here they did not.
customer_one = Customer("USD")
customer_list.append(customer_one)


