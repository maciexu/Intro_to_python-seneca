help(int)

class Person:
    pass

user1 = Person()
print(user1)


class Vehicle:
    pass

car = Vehicle()
boat = Vehicle()


class User:
    def __init__(self):
        print("I just run")
        print("Run again")

user1 = User()

class Person1:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        print(f'{first}  {last} is {age} old. ')
person1 = Person1("macie", "xu", 29)


class Vehicle1:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f'{make}, {model}, {year}')

car1 = Vehicle1("Honda", "Civic", 2017)

class Comment:
    def __init__(self, who, what, likes=0):
        self.who = who
        self.what = what
        self.likes = likes
test1 = Comment("macie", "i like u")
print(test1.who, test1.what, test1.likes)







