# hello everyone, today we will be learning things through a code
# difficulty level : medium
'''
The following program will make use of:

- py math knowledge (python math)
- chatbot functions
- defining functions
- casting (int, str, float) 
    but we will not be using float, we will be using str and int (int is used most common in this case)
- if, elif, else
- print statement
- simple math knowledge


'''



#define the variable values_3d
def values_3D(shape):
  if shape == "Cube":
    length = int(input("length of cube you want:"))
    volume = length ** 3
    area1 = 6 * length ** 2
    print("area of cube is", area1)

    #we have learnt the above information in the previous tutorials. pyMATH * = x times and broadcast a message
    #that wikk change according to the text you entered
  elif shape == "Cuboid":
    length = int(input("length of rec you want:"))
    breadth = int(input("breadth of rec you want:"))
    height = int(input("height of rec you want:"))
    vol = length*breadth*height
    area1 = 2*length*breadth + 2*length*height+ 2*breadth*height
    print("area of cuboid is", area1)
  else:
    print("ERROR-404: SHAPE ENTERED INVALID, PLEASE RESTART THE PROGRAM")
    print("Volume =", vol, " Area =", area1)

#define variable values_2d
def values_2D(shape):

  #if user types in square, this happpenes
  if shape == "Square":
    length=int(input("length of square is"))
    perimeter = length + length + length + length
    area2 = length ** 2
    print("area of square is", area2)


    # if user types in rectangle, this happenes
  elif shape == "Rectangle":
    length=int(input("length of rectangle is"))
    width=int(input("width of rectangle is "))
    perimeter = length + length + width + width
    area2 = length * width
    print("area of the rectangle is", area2)

    # if user types in circle, this happens
  elif shape == "Circle":
    radius=int(input("radius of circle is"))
    perimeter = 2 * 3.14 * radius
    area2 = 3.14 * radius ** 2
    # PYMATH KNOWLEDGE!
    print("the area of the circle is", area2)


    # the message error will be broadcasted when not entered circle rectangle square
  else:
    print("ERROR-404: SHAPE ENTERED INVALID, PLEASE RESTART THE PROGRAM")
    return ""
  return "Perimeter = " + str(perimeter) + ", Area = " + str(area2)


print("welcome to the shapes calculator! may i know your name?")
name = input("what is your name? :-)")
dimension = input("cool name,  what shapes do you want? (2D OR 3D)")


#if user entered 3D, the following will be broadcasted (below)
if dimension == "3D":
  shape = input("choose one of the following \n(Cube / Cuboid:)")
  values_3D(shape)
elif dimension == "2D":
  shape = input("choose one of the following \n(Square / Rectangle / Circle:)")
  values_2D(shape)

  #this will be broadcasted if the text entered is not square, rectangle, circle
else:
  print("ERROR-404: DIMENSION ENTERED INVALID, PLEASE RESTART THE PROGRAM")
 

 #main index but this is nonsensical lmao#
