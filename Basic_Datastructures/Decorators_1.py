#Python decorator tutorial
#How to convert lower case to upper case using decorators
'''
Python Decorators Tutorial
    A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
    Decorators are typically applied to functions, and they play a crucial role in enhancing or modifying the behavior of functions.
'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return 'hello world'

#decorate = uppercase_decorator(say_hi)
#print("Normal function call ",decorate())


print("Using decoratore @:",say_hi())