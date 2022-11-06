"""
Exceptions that may happen in Spoticry module
"""


class FunctionNeedsInput(TypeError):
    print("Wrong input")
    pass


class WrongInput(NameError):
    print("Function input should be link and accounts should be loaded first...")
