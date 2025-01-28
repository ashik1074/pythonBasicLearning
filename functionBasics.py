def myFunction(food):
    # return food[2]
    pass

fruits = ["Banana","Apples", "Cherry"]
print(myFunction(fruits))

# def demoFunction(a):
#     return lambda a:a+n
#
# adder = demoFunction(5)
# print(demoFunction(2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))