 #return values
def myName():
        name ="leticia"
        return name
myName()
#view output
name = 'leticia'
print(name)
    
def myNamepara(name):
        return name
myNamepara('leticia')

def myAge():
        age= 23
        return age
print(f"my name is {myName()} and i am {myAge()} years")

# create a function that calculates  the area of a triangle and the base and the height must be function parameters
def areaOfTriangle( base , height):
        area = (1/2) *base* height
        return area
print(f" the area of a traiangle is base:{base} and height{height} is :{area}")
        
#approach two
def area_of_triangle_two():
        base = int (input("enter the base:"))
        height= int(input( " enter the height"))
        area = int((1/2)*base*height)
        print(f" the area of a triangl is base:{base} and height:{height} is :{area}")