# Dictionary :  build in data structure that is used to store data in a key - value pairs

#creating a dictionary
student = {"Name" : "Ali" , "Age" : 18 , "grade" : "A"}
print(student["Name"])
print(student.get("Age"))#it returns none if "age" doesn't exist

#adding/updating values
student["city"] = "Karachi" #add

student["Age"] = 19 #update

#removing
student.pop("grade") #removes specific key
student.clear() # removes all items
print(student.get("age"))
