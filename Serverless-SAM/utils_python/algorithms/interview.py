# https://www.youtube.com/watch?v=QVdf0LgmICw
# Scopes in Python - LEGB: 
# Local:        Local to the function
# Enclosing:    Enclosing function's scope
# Global        Global scope
# Built-in      Built-in scope

# import builtins
# print(dir(builtins))

# def min():
#     pass
# print(min([5, 3, 10])) # Error - built-in functions can be overridden

# var = 0 # global

def modify(arr):
    arr[0] = 1
    global var # no need to define globally first
    var = 1
    var2 = 2        # enclosing
    def _inner():     
        nonlocal var2   
        var2 = 3
        var3 = 4        # local
    _inner()
    print("var2:", var2)
    # print(var3) # error

def main():
    arr = [0, 0, 0]
    modify(arr)
    print(arr) # [1, 0, 0]
    print("var:", var) # 0

if __name__ == '__main__':
    main()