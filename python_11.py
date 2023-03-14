print("Enter 1st number : ")
a = input()  # 1
print("Enter 2nd number : ")
b = input()  # q
# print("the sum of a and b is", int(a)+int(b)) Error occur if we provide string


# Try and Except Block
# Try Block - enclose the code that might throw an exception.
# Except Block - excuted when error occured
try:
    print("the sum of a and b is", int(a)+int(b))
    print('addition completed')
except:
    print("error find")


# Print the Exception Occur
try:
    print("the sum of a and b is", int(a)+int(b))
    print('addition completed')
except Exception as e:
    print(e)


# Handling Multiple Exception
try:
    print("the sum of a and b is", int(a)/int(b))
    print('addition completed')
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("denominator is 0")
except NameError:
    print("denominator is 0")
except Exception as e:
    print(e)


# Raise Block - raises an error and stops the control flow of the program.
try:
    print("the sum of a and b is", int(a)/int(b))
    if a > b:
        raise Exception("ww")
    else:
        raise ZeroDivisionError("ww")
except ZeroDivisionError:
    print("denominator is 0")
except Exception as e:
    print(e)


# Else Block - excuted when no error occured
try:
    print("the sum of a and b is", int(a)/int(b))
except Exception as e:
    print(e)
else:
    print("no error found")


# Finally Block - excuted when error occured / no error occured
try:
    print("the sum of a and b is", int(a)/int(b))
except Exception as e:
    print(e)
else:
    print("no error found")
finally:
    print("error finding done")


# Assertion Error
try:
    # assert - excuted the condition is false and throw an error
    assert int(b) != 0, "denominator is zero"
    print("the sum of a and b is", int(a)/int(b))
except AssertionError as arr:
    print(arr)
