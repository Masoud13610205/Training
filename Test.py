import time

print("Hello")
name = input("What is your name?")
age = input("Your age?")
age = int(age)
if age < 18:
    print("not allowed")
elif 18 <= age < 40:
    print("it's ok")
else:
    print("you are too old")
  
#print ("Hello %s. your age is %i" % (name, age))
# while age < 18:
#     print("too young")
#     age += 1
# while 18 <= age <= 50:
#     print("it's ok")
#     time.sleep(1)
#     age += 1 
# if age > 50:
#     print("you are too old")