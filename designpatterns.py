"""
Creational - create objects
Structural - organize objects
Behavioral - communication between objects
"""

""" 
Factory Method

Use when uncertain about type of objects you will produce.
We can create a factory to return any kind of pet we want, and 
we can add classes to support new pets.
"""

class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat: 
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

def get_pet(pet):
    """ The factory method. """

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]

# Implementation
get_pet("dog")

""" 
Abstract Factory Method

User expects many related objects, but don't know type.

We want to create a factory like before, but we can have many similar factories. 
We will create an abstract factory so that we can interact with different 
factories in the same way. 
"""

class Dog:
    def speak(self):
        return "woof"

class DogFactory:
    """ Concrete Factory""" 

    def get_pet(self):
        """ Factory method. """

        return Dog()

class PetStore:
    """ Abstract Factory """

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory
    
    def show_pet(self):
        """ Factory method. """ 
        
        pet = self._pet_factory.get_pet()

# Implementation
factory = DogFactory()
shop = PetStore(factory)
shop.show_pet()

"""
Singleton Method

Allow only one object to be created from a class. 
Good for an information cache shared by many. 
"""

"""
Builder Pattern

Solves for having too many constructors. 
(ex) we want to build a car. We will need to create a constructor for each 
part b/c each car is different and then assmble. 

Instead, we will have an Abstract Builder class to generalize the process of 
creating a car and a Director that will use the Builder class to MAKE the car. 
"""

class Director():
    def __init__(self, builder):
        self._builder = builder
    
    def constructor_car(self):
        self.builder.create_new_car() # Making the Car
        self.builder.add_model()
        self.builder.add_tires()
    
    def get_car(self):
        return self.builder.car

class Builder():
    """ Abstract Builder """
    def __init__(self):
        self.car = None
    
    def create_new_car(self):
        self.car = Car()
    
class SkyLarkBuilder(Builder):
    """ Concrete Builder - add specifics to Builder """
    
    def add_model(self):
        self.car.model = "Skylark"
    
    def add_tires(self):
        self.car.tires = "Regular tires"

class Car():
    """ Product """

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

# Implementation
builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

"""
Prototype Design Pattern

Creating many instances of same object is expensive. We can clone instead.
"""

import copy

class Prototype:
    """ Holds the different objects you may want to copy. """

    def __init__(self):
        self.objects = dict()
    
    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def clone(self, name):
        obj = copy.deepcopy(self._objects.get(name))
        return obj
   
class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"

# Implementation  
c = Car()
prototype = Prototype()
prototype.register_object("skylark", c)

c1 = prototype.clone('skylark')

"""
Decorator Pattern

Add additional features to an existing object.
"""

def make_blink(function):
    def decorator():
        ret = function()
        return "<blink>" + ret + "</blink"
    return decorator

@make_blink
def hello_world():
    return "Hello World"

# Implementation
hello_world()

"""
Proxy Pattern

Producer object is expensive to instantiate. We instead have one, and use a Proxy to 
instantiating Producers, and tell clients when the Producer is ready for use again instead
of making a new Producer.
"""

class Producer:
    def produce(self):
        print("Producer is working hard!")
    
    def meet(self):
        print("Producer has time to meet you now.")

class Proxy:
    def __init__(self):
        self.occupied = 'No'
        self.producer = None 

    def produce(self):
        if self.occupried == 'No':
            self.producer = Producer()
            self.producer.meet()
        else:
            print("Producer is busy")

# Implementation
p = Proxy()
p.produce() # -> "Producer has time to meet you now."
p.occupied = 'Yes' # Make as many producers as you feel is necessary before "Yes"
p.produce() # -> "Producer is busy!"

"""
Adapter Pattern

Interfaces are incompatible between client and server (client expects to interact in
one way, but server recieves interactions differently.)

(ex) We have Korean class that can speak_korean, and English class that can speak_english
but client only wants to use speak().
"""

class Korean:
    def __init__(self):
        self.name = "Korean"
    
    def speak_korean(self):
        return "An-neyong"
    
class British:
    def __init__(self):
        self.name = "British"
    
    def speak_english(self):
        return "Hello"

class Adapter:
    def __init__(self, object, **adapted_method):
        self._object = object
        """ Dict. mapping between speak() and korean_speak() """ 
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """ Get other attributes from the object. """ 
        return getattr(self._object, attr)

# Implementation
objects = []
korean, british = Korean(), British()
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))
print(objects[0].name, objects[0].speak())
print(objects[1].name, objects[1].speak())

"""
Composite Design Pattern

Tree data structure. Run a function on each node in tree.
"""

class Component(object):
    """Abstract class."""
    def __init__(self, *args, **kwargs):
        pass
    
    def component_function(self):
        pass

class Child(Component):
    """Concrete class and maintains node value."""
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
    
    def component_function(self):
        print(self.name)

class Composite(Component):
    """Concrete class and maintains branches of node."""
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []
    
    def append_child(self, child):
        self.children.append(child)
    
    def remove_child(self, child):
        self.children.remove(child)
    
    def component_function(self):
        print(self.name)
        for i in self.children:
            i.component_function()

# Implementation
sub1 = Composite("submenu1")
sub11 = Child("sub_submenu 11")
sub12 = Child("sub_submenu 12")
sub1.append_child(sub11)
sub1.append_child(sub12)
sub1.component_function()

"""
Bridge Design Pattern

1 Class to Initialize Attributes, 1 Class to Implement the Specific functions.
Call class 2 implemented functions in class 1 functions. 
"""

class DrawingAPIOne(object):
    """ Implementation specific. """
    def draw_circle(self, x, y, radius):
        print("API 1 drawing circle.")

class DrawingAPITwo(object):
    def draw_circle(self, x, y, radius):
        print("API 2 drawing circle.")

class Circle(object):
    """ Implementation independent (contains only necessary attributes). """
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y 
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """ Implementation specifics taken care of by API. """
        self._drawing_api.draw_circle(self._x, self._y, self._radius)
    
    def scale(self, percent):
        self._radius *= percent
    
# Implementation
circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()

"""
Observer Design Pattern

Observers will monitor subject, and observers will be notified when subject are funky.
1 Subject to Many Observers.

(ex) Subject is temperature at power plant and many observers / monitors.
"""

class Subject(object):
    """ Abstract Subject."""

    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observer.remove(observer)
        except ValueError:
            pass
    
    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):
    """Concrete Subject.""" 

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property #Getter
    def temp(self):
        return self._temp
    
    @temp.setter #Setter
    def temp(self, temp):
        self._temp = temp

class TempViewer:
    """ Observer. """

    def update(self, subject):
        print(subject._name, subject._temp)

# Implementation
c1 = Core("Core 1")
c2 = Core("Core 2")
v1 = TempViewer()
v2 = TempViewer()
c1.attach(v1)
c1.attach(v2)
c1.temp = 80 # Each observer will print out message.
c1.temp = 90 # Each observer will print out message.

"""
Visitor Design Pattern

Allow other objects to edit current object. Unlike decorator, we aren't modifying our function
everytime, but only editing it when we invoke a visitor. 
"""

class House(object):
    def accept(self, visitor):
        visitor.visit(self)
    
    def work_on_ac(self, ac_specialist):
        print(self, "worked on by", ac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)

class Visitor(object):
    """ Abstract visitor class. """
    def __str__(self):
        return self.__class__.__name__
    
class AcSpecialist(Visitor):
    """ Concrete visitor class."""
    def visit(self, house):
        house.work_on_ac(self)
    
class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)

# Implementation 
ac = AcSpecialist()
e = Electrician
home = House()
home.accept(ac)
home.accept(e)

"""
Iterator Design Pattern

Use generators to allow client to choose how many values they want to iterate through.
"""

"""
Strategy Design Pattern

When you need to have dif. func./algorithms for dif. scenarios. If conditions are not good 
because you have to go back and change the code (if statement) for the class. 
Use strategy to dynamically add as many func. as you want without changing code. 
"""

import types
class Strategy:
    def __init__(self, function=None):
        self.name = "Default strategy"

        if function:
            self.execute = types.MethodType(function, self) # rebinds method properly

        def execute(self):
            print(self.name)

def strategy_one(self):
    print("strategy 1")

def strategy_two(self):
    print("strategy 2")

# Implementation
s0 = Strategy()
s0.execute() # "Default strat"
s1 = Strategy(strategy_one)
s1.execute() # "strat 1"

"""
Chain of Responsibility Design Pattern

Pass request down a chain/tree until some node/handler can handle it.
"""

class Handler:
    """ Abstract Handler."""
    def __init__(self, successor):
        self._successor = successor
    
    def handle(self, request):
        handled = self._handle(request)
        if not handled:
            self._successor.handle(request)
    
    def _handle(self, request):
        raise NotImplementedError

class ConcreteHandler1(Handler):
    """ Concrete Handler."""
    def _handle(self, request):
        if 0 < request <= 10:
            print('Request processed')
            return True

class DefaultHandler(Handler):
    def _handle(self, request):
        print('End of chain.')
        return True 

class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))
    
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

# Implementation
c = Client()
requests = [2, 5, 30]
c.delegate(requests) # => Request processed, Request Processed, End of Chain

"""
Facade Design Pattern (Structural)

Instead of creating and calling methods from each object, you call one that triggers all.
(ex) when you turn on a car, you press button, you don't need to individually turn on engines etc.
"""

class SubSystemA:
    def method1(self):
        print("1a")
    def method2(self):
        print("2a")

class SubSystemB:
    def method1(self):
        print("1b")
    def method2(self):
        print("2b")

class Facade:
    def __init__(self):
        self._subsystemA = SubSystemA()
        self._subsystemB = SubSystemB()

    def method(self):
        self._subsystemA.method1()
        self._subsystemA.method2()
        self._subsystemB.method1()
        self._subsystemB.method2()

# Implementation 
facade = Facade()
facade.method()

""" 
Command Design Pattern: Behavioral

1) Encapsulates functions into Command classes. 
2) We use a Macro to queue up these objects and run functions.
"""

class Command:
    """ Abstract command class. """
    def execute(self):
        pass

class Copy(Command):
    """ Concrete encapsulated Command. """
    def execute(self):
        print("Copying")

class Paste(Command):
    def execute(self):
        print("Pasting")

class Save(Command):
    def execute(self):
        print("Saving")

class Macro:
    def __init__(self):
        self.commands = []
    
    def add(self, command):
        self.commands.append(command)
    
    def run(self):
        for o in self.commands:
            o.execute()
    
# Implementation
macro = Macro()
macro.add(Copy())
macro.add(Paste())
macro.add(Save())
macro.run()

""" 
Mediator Design Patter: Behavioral 

Problem: Tight coupling between objects. Loosen coupling 
by having a mediator like a load balancer. 
"""

class Colleague(object):
    """ Abstract Object. """
    def __init__(self, mediator, id):
        self._mediator = mediator
        self._id = id
    
    def send(self, msg):
        pass

    def receive(self, msg):
        pass

class ConcreteColleague(Colleague):
    def __init__(self, mediator, id):
        super().__init__(mediator, id)

    def send(self, msg):
        print(msg, "sent by", self._id)
        self._mediator.distribute(self, msg) # distribute message here
    
    def receive(self, msg):
        print(msg, "received by", self._id)

class Mediator:
    """ Abstract mediator class. """
    def add(self, colleague):
        pass

    def distribute(self, sender, msg):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        Mediator.__init__(self)
        self._colleague = []
    
    def add(self, colleague):
        self._colleague.append(colleague)
    
    def distribute(self, sender, msg):
        for colleague in self._colleague:
            if colleague._id != sender._id:
                colleague.receive(msg)

# Implementation
mediator = ConcreteMediator()
c1 = ConcreteColleague(mediator, 1)
c2 = ConcreteColleague(mediator, 2)
c3 = ConcreteColleague(mediator, 3)
mediator.add(c1)
mediator.add(c2)
mediator.add(c3)
c1.send("Good morning") # -> all other colleagues receive message.

"""
Memento Design Pattern: Behavioral

Saving an past instance of an object. Helpful for restoring.
Basically, serialize object.
"""

import pickle

class Originator:
    def __init__(self):
        self._state = None

    def create_memento(self):
        return pickle.dumps(vars(self))
    
    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

# Implementation
originator = Originator()
memento = originator.create_memento() # -> state = none
originator._state = True # -> state = True
originator.set_memento(memento) # -> state = None

