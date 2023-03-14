def add(a,b):
    return a + b , a * b
result = add(3,4)
print(result)
def greet(name,greeting="Hello"):
    return f"{greeting},{name}"
print(greet("Shubhi"))
print(greet("Shaanu","Hey"))
def add_all(*args):
    result = 0
    for arg in args:
        result += arg
    return result
print(add_all(1,2,3,4))
def printt_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")
printt_kwargs(a=1,b=2,c=3)
def make_adder(x):
    def adder(y):
        return x + y
    return adder
add5 = make_adder(5)
print(add5(3))