marks=0
year= 1

while (marks<=500):
     marks= marks + int(input("enter " + str(year) +  "st year's marks"))
     print(" total marks are " + str(marks))
     year = year+1
else:
     print(" you cleared the exam")
