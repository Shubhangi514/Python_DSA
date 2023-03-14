def foo(array):
    sum = 0
    product = 1

    for i in array :
        sum += i

    for i in array :
        product *= i
    print("Sum = "+str(sum)+",Product = "+str(product))

array = [19,18,17,65,90,23,67,69,34]