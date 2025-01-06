#Conditions >>>>
# def myFunction():
#     return False
#
# if myFunction():
#     print("Yes")
# else:
#     print("No")


#PythonList
mylist = ["apple","11","33.00"]
print(len(mylist), type(mylist))
thislist = list(("apple","55","243hf43"))
print(thislist)

wishList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
wishList[1:3] = ["blackcurrant", ""]
print(wishList)
wishList.insert(2,"Latte")
print(wishList)