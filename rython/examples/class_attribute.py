class MyClass:
    myClassVariable = ["Hello"]

    def __init__(self):
        self.myInstancevariable = [1,2,3]

objectOne = MyClass()
objectTwo = MyClass()

# objectOne.myClassVariable = ["Hello", "World"]
# print(objectOne.myClassVariable) # ["Hello", "World"]
# print(objectTwo.myClassVariable) # ["Hello"]
# print(MyClass.myClassVariable) # ["Hello"]

# objectOne.myClassVariable.append("World")
# print(objectOne.myClassVariable) # ["Hello", "World"]
# print(objectTwo.myClassVariable)  # ["Hello", "World"]
# print(MyClass.myClassVariable)  # ["Hello", "World"]

# MyClass.myClassVariable = ["Hello", "World"]
# print(objectOne.myClassVariable) # ["Hello", "World"]
# print(objectTwo.myClassVariable)  # ["Hello", "World"]
# print(MyClass.myClassVariable)  # ["Hello", "World"]

objectOne.myInstancevariable.append(4)
print(objectOne.myInstancevariable)  # [1, 2, 3, 4]
print(objectTwo.myInstancevariable)  # [1, 2, 3]