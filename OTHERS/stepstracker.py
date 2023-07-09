


Q1 = ""
Q2 = ""
Q3 = ""

OPTION1 = []
OPTION2 = []
OPTION3 = []
OPTION4 = []
anomynous_noob_zz = 0


ANS = []
qnsLIST =[]

print("")
print("Hello, welcome! these are the rules:")
print(" - for each question, enter the number for option you choose")
print(" - please do not enter any alphabets (a, g, r, etc.), or there will be an error")
print(" - do this quiz by yourself without the help of your parents or teachers or friends, or GOD")
print(" - KEY NOTE | have fun and smile! :)")
print("")

#just now is the starting code. This is now..... THE PROPER CODE!

game = True
print("How many percent of a banana is water?")
print("1. 75%\n2. 93%\n3. 97%\n4. 27%")
answer = int(input("your answer is:"))
print("")
if answer == 1:
  print("that is the correct answer, good job! (this science question difficulty is level 5)")
else:
  print("you answered incorrect, try again! (this science question difficulty is level 5)")

print("")

print("what is a onmivore?")
print("1. food eater\n2. plant eater\n3. both food and plant eater\n4. none of the above")
answer = int(input("your answer is:"))
print("")
if answer == 3:
  print("that is the correct answer, good job! (this science question difficulty is level 2)")
else:
  print("you answered incorrect, try again! (this science question difficulty is level 2)")

























import matplotlib.pyplot as plt
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
listofSTEPS = []
listofCOLORS = []
totalSTEPS = 0
BCBCBCBCBCBunder10K = []

i = 0
while i < 7:
  numofSTEPS = int(input("How many steps did u walk on " + days[i] + "? "))
  listofSTEPS.append(numofSTEPS)
  totalSTEPS += numofSTEPS

  if numofSTEPS >= 15000:
   listofCOLORS.append("green")
  else:
   listofCOLORS.append("red")
   BCBCBCBCBCBunder10K.append(days[i])
  i += 1

averageSTEPS = totalSTEPS / 7
print("Hi, you have walked an average of " + str(averageSTEPS) + "this week")

if averageSTEPS >= 15000:
  print("Keep up the good work BOIII")
else:
  print("walk more to stay healthy lah BOIII")

print("this are the days you walked lesser than 15000 steps BOIII: ")
for i in BCBCBCBCBCBunder10K:
  print(i)

plt.bar(days,listofSTEPS,color = listofCOLORS)
plt.xticks(days,('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'))
plt.title("Number of steps you took thiz week BOIII")
plt.show()
