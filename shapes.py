'''
shapes.py
a simple programme to consolidate my oop knowledge:
this programm functions as a 'gemoetric shapes' calculator ie calculates basic gemoetric
operations of shapes such as area and perimater.
-intended functionality:
starts off with basic 2d shapes, the goal is to extend this to 3d and more complicated shapes.
end result will be performin other analytical geomerey operations ie midpoint distance exc.
-hopefully a graphic UI.
-I also fully intend to extend this programme to euclidean gemoetry (only once the graphic user interface has been assempled
to allow it to function as a 'geometric proof' theorem calculator for euclidean gemoetry)
if possible, i would also like to extend this project to triginometry, particularly 3d trigonomtry
-- ie sine rule, cosine rule eetc.
---- the end goal will be to have this programme tackle 4 dimmensional shapes (gonna have to review some maths, cause ive forgotten most of this)

'''

'''
basic outline for the 2d version:
define an abstract shape class (all other shape classes will inherit from this class)
-in the planning stage , i began with a functional approach, ie i divided this program into its most simple problems,
and designed functions to solve each problem. based on these atomistic functions, i was able to ascertain, what arguments would be common
to the various functions. The commonality of arguments, determines the creation of the class objects:
aobstract shape class: 
-has abstract (undefined methods for area and perimeter)
-actual shape classes (all inherit from parent shape class)

ie, triangle class: has methods, are and perimeter
- takes as inputs 3 points (3 tuples corresponding to three sets of x and y coordinates.)
-> these three tuples are used to derive the actual length of the triangles sides:
--> from the length of these sides, we can directly compute perimeter,
--> from the length of these sided we can infer base and height for area calculations

quadrelateral class: abstrac class for square and rectangle
from this class, sqare and rectangle will inherit methods
square class, doesnt need to overid emethods, because both methods (2l +2h, for sq, 2s + 2s, perimeter), (l *h, s*s)
will yield the same results for square (ie the case of the sqare class is just an extension of the case for rectangles)
required inputs, length and height. from the (4 sets of tuples) these can be computed directly

NOTE: will need some sort of logic to ensure that thae coordinates are entered in a specific sequence ieleft->
bottom-> right -> top for sqr/rectangle, left -> base -> right fpr triangle

circle class: (will require imprting maths library)
- only takes one parameter, radius
-> two methods, one for calculating the circumference
-> the other for calculating the area of the given circle.


two be considered: edge cases
-what user inputs could cause the programme the break down? 
(too depressing for now, will come back to this later)

nb! something else to be considered: I at present, want to extend this to 3d. so, should i start with complexity or simplicity?
ie start with 3d or start with 2d?
---response: ive given it a little bit of thought. I think it would be better to move from the simple to the complex ie
:- considering what OOP is all about, starting with 2d (actually a semi abstract 'shape' class) seems more in line with its philosophy. 
(as an aside, I am curious as to whether it is better in certain cases to go the other way, initial thought is that this make sense when the 'complex' is the norm and simplicity is a rarity )
   Furthermore, if i wanted to focus on 3d shapes, starting with 4 dimmensional shapes would be a headache if ever i did see one ()
-- also, conceptually, makes more sense to see 3d as an extension of 2d, rather than 2d as an instanciation (in the predicate calculus sense) of 3d.
---> another note on utility, 3d (inheriting from 2d) means that it can recyle properties from the latter

-essential attributes 
-> attribute should be wide enough to cover a variety of shapes, whilst still rettaining enough utility
for use in inheritence


-possible attributes to be considered
name, (str) stores shapes name
num_si (int) represents number of sides
si_len (list/tuple) to contain lengths of sides

methods:
-shape class to provide method place holders (implemented by subclass)
describe(), basic facts about the shape
-area(), what its name is
perimeter() ditto


note to self! Just became aware of the 'liskov subsititution principle', (without harming functionality, a subclass should be substitutable for its superclass)
need to learnmore, a quote does not a skill make, and my understanding so far is peasant level.
'''
import math #because i need pi for circle subclass

#class construction section

class Shape():
    '''
    the 'template' base shape class
    '''
    def __init__(self, name):
        self.name = name

    def area(self):
        raise
    NotImplementedError("Subclasses MUST implement area calculation")
    
    
    def perimeter(self):
        raise
    NotImplementedError("Subclasses MUST implement perimetera calculation")
    
    
    def describe(self):
        return f"{self.name}: Area {self.area()}, Perimeter =  {self.perimeter()} "
    

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    
    def area(self):
        return self.length * self.width
    
    
    def perimeter(self):
        return 2*(self.width + self.width)
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius 

    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2*math.pi * self.radius 
    
class Triangle(Shape):
    def __init__(self, radius, a, b, c):
        super().__init__("Triangle")
        radius.self = radius
        a.self = a
        b.self = b
        c.self = c

    def area(self):
        '''
        using herons formula
        '''
        semi_peri = (self.a + self.b + self.c)/2
        return math.sqrt(semi_peri * (semi_peri-self.a)*(semi_peri-self.b)*(semi_peri-self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c


#user input section

def get_users_shape():
    print("Kindly choose a shape\n1 Rectangle \n2 Circle \n3 Triangle")
    choice = input("What shape has set a fire in your loins today?(enter 1, 2 or 3)")
    if choice== "1":
       length = float(int(input("Kidnly enter the length")))
       width = float(int(input("Kindly enter the width")))
       return Rectangle(length, width) 
    elif choice == "2":
        radius = float(int(input("Kindly enter the radius")))
        return Circle(radius)

    elif choice == "3":
        a = float(int(input("Kindly enter side a ")))
        b = float(int(input("Kindly enter side b ")))
        c = float(int(input("Kindly enter side c")))
        #line below tests whther the triangle inequality holds
        if a+b <= c or a+c <= b or b+c <= a:
            print("Invalid triangle sides")
            return None
        return Triangle(a,b,c)

    else:
        print("Invalid choice :( \nPathetic)")
        return None

shape = get_users_shape()
if shape:
        print(shape.describe())