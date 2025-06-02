
'''
def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)
add(10, 20, 30, 40, 50,60,70,80,90,100)
def calculate(n,**kwargs): 
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
calculate(2,add=3,multiply=5)
'''
class Car: 
    def __init__(self,**kw): 
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')

my_car = Car(make='Nissan',model='GT_R',colour='green',seats='4')
print(my_car)
print(my_car.model)
print(my_car.make)
print(my_car.colour)
print(my_car.seats)

