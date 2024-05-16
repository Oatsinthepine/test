import sys
from dog import bark
bark()
print(sys.argv)

def multiply(x,y):
    return x*y
print(multiply(2,4))
abstract_multiply = lambda x, y: x * y
print(abstract_multiply(1,3))

lists = [1,2,3,4,5]
for i in range (len(lists)):
    lists[i] = 2 * lists[i]
print (lists)

i = 0
while i < len(lists):
    lists [i] = 2* lists [i]
    i = i + 1
print (lists)

number = [3,4,5]
result = map(lambda a: a * 2, number)
print(list(result))

try:
    result = 3/0
except:
    print ('can not divide zero ! ')
finally:
    result = 1
print (result)

numbers = [1,2,3,4,5]
number_power = []
for i in numbers:
    number_power.append(i**2)
print (number_power)

#list comprehension:
numbers = [1,2,3,4,5]
number_power = [i**2 for i in numbers]
print(number_power)

class dog:
    def eat (self):
        print ('eat the dog food')
class cat:
    def eat (self):
        print ('eat the cat food')
animal_1 = dog()
animal_2 = cat()

animal_1.eat()

mylist = ['a', 'b', 'c']
print(list(mylist.pop()))

#decorator fucnction:
import functools
def repeat_func (num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper (*args, **kwargs):
            for i in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat_func(num_times=3)
def greeting_func(name):
    print(f"Hello, {name}.")

greeting_func('Alex')

def make_shirt(size = "large", pattern = "i love python"):
    print(f"This shirt is {size}, and it has {pattern}.")
make_shirt("mid_size")

def describe_city(name ='Reykjavik', country="Iceland"):
    print(f"{name} is in {country}.")
describe_city('Xian', "China")
describe_city()

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def get_formatted_name(first_name, last_name, middle_name= ""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('Tom',"jack")
print(musician)

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#while True:
    #print("Please tell me your name:")
    #print("(enter q or quit to stop)")
    #f_name = input ("first name: ")
    #if f_name == "q" or "quit":
        #break
   # l_name = input("last_name: ")
   # if l_name =="q" or "quit":
    #    break
   # formatted_name = get_formatted_name(f_name, l_name)
    #print(f"Hello, {formatted_name}")


def greet_users(names):
    for name in names:
        print(f"Hello, {name.title()}")
usernames = ['a','b','c']
greet_users(usernames)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)

import pizza
from pizza import make_pizza as mp
mp(16, 'mushroom','tomato','cheese')

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last'] = last
    return user_info

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.dish_price = 30
        self.number_served = 0

    def service_number(self):
        print(f"this restaurant serves {self.number_served} people.")

    def describe_restaurant(self):
        print(f"This is {self.name} restaurant.")
        print(f"{self.name} restaurtant provides {self.type} food.")
        long_name = f"{self.name} {self.type}"
        return long_name.title()

    def open_restaurant(self):
        print(f"{self.name} is now opening.")

    def get_price(self):
        print(f"{self.name} 's food is {self.dish_price} dollar per dish.")

    def update_price(self, new_dish_price):
        if new_dish_price >= self.dish_price:
            self.dish_price = new_dish_price
        else:
            print("You can't sell a dish lower than before")
        #self.dish_price = new_dish_price

    def increment_price(self, increased_price):
        self.dish_price += increased_price

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, falvors):
        super().__init__(restaurant_name, 'Ice Cream')
        self.falvors = falvors

    def display_flavors(self):
        print(f"the available flavors at {self.name} are:")
        for flavor in self.falvors:
            print(flavor)

restaurant = Restaurant('Chinese love', 'spicy')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.get_price()
restaurant.number_served = 20
restaurant.service_number()
restaurant.update_price(50)
restaurant.get_price()
restaurant.increment_price(70)
restaurant.get_price()

my_ice_cream_stand = IceCreamStand("Cool Ice Cream", ['Vanilla', 'Chocolate', 'Strawberry'])
my_ice_cream_stand.open_restaurant()
my_ice_cream_stand.display_flavors()






class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(f"User Information:\nFirst Name:{self.first_name}\nLast Name:{self.last_name}\nAge:{self.age}")

    def greet_user(self):
        print(f"Hello,{self.first_name} {self.last_name} nice to meet you!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(["Can add post", "Can delete post", "Can ban user"])

# Create instances of the User class
user1 = User('John', 'Doe', 30)
user2 = User('Alice', 'Smith', 25)

# Call methods on each instance
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

# Increment login attempts multiple times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print the value of login_attempts
print(f"Login Attempts: {user1.login_attempts}")

# Reset login attempts
user1.reset_login_attempts()

# Print the value of login_attempts after reset
print(f"After resetting, Login Attempts: {user1.login_attempts}")

# Create an instance of the Admin class
admin1 = Admin('Admin', 'User', 40)

# Call the show_privileges() method through the Privileges instance
admin1.privileges.show_privileges()

from random import choice
class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        play = choice(range(1, self.sides + 1))
        print(play)
# Create a 6-sided die
die_1 = Die()
# Roll the die 10 times
for i in range(10):
    die_1.roll_die()


for i in range(1, 21):
    print (i)

list_1 = list(range(1, 1000001))
for i in list_1:
    print(min(list_1))
    print(max(list_1))
    print(sum(list_1))
    break

list_2 = range(1, 20, 2)
for i in list_2:
    print(i)

list_3 = range(3, 30)
for i in list_3:
    if i % 3 == 0:
        print(i)

list_4 = list(range(1, 10))
for i in list_4:
    i = i**3
    print(i)



import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)

my_die = MSDie(6)
for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)

