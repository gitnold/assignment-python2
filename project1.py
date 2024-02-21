#Creating a calculator using functions
def values():
    global num1
    global num2
    num1 = float(input("Enter first value : "))
    num2 = float(input("Enter second value : "))
    prompt()#Calls the second task in function prompt
def prompt():
    prompt = int(input("Enter mathematical operation number'1.add, 2.subtract, 3.divide, 4.multiply : "))
    if prompt == 1:
        add()
    elif prompt == 2:
        subtract()  
    elif prompt == 3:
        divide()  
    elif prompt == 4:
        multiply() 
    else:
        print("Wrong sign!!\nEnter the no before operation name!") #error message is to tell the user their mistake for clarity
        values()#the program then starts all over again for the user to input correct values          
def add():        
        result = num1 + num2
        print (result)
def subtract():
    result = num1 - num2
    print(result)        
def divide():
    result = num1/num2
    print(result) 
def multiply():
    result = num1 * num2
    print(result)            

values()


import math
def areacircle():
    radius = float(input("\n\nEnter radius : "))
    area = math.pi * radius ** 2
    result = "Area of a circle of radius {}m is {} square metres"#a string has been used to allow string formatting for clear and self explanatory answer statements
    print(result.format(radius, area))


def volumecylinder():
    #since values were there was no need for prompting the user for inputs ; this necessiated a formatted string with the values for the user to understand where the 
    #value of the volume comes from
    pi = 3.14
    radius = 140 
    height = 9
    volume = pi * radius ** 2 * height
    result2 = "\n\nVolume of cylinder of radius {}m and height {}m is {} cubic metres "#refer to omment on line 41
    print(result2.format(radius, height, volume))

def areatrapezium():
    a = 10
    b = 7
    h = 12
    c = a + b
    areatrp = 1/2 *c * h
    area2 = "\n\nArea of a trapezium of sides {} and {} metres and height {}m is {} square metres"
    print(area2.format(a, b, h, areatrp))


areacircle()
volumecylinder()
areatrapezium()