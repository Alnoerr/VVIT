def greet(name):
    print(f"Привет, {name}!")

def square(number):
    return number**2

def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

greet("Олег")
print(square(4))
print(max_of_two(5, 10))