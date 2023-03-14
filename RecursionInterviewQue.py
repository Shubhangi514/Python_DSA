#-how to find the sum of digits of a positive integer number using recursion-#
def SumOfDigits(n):
    assert n >= 0 or int(n) == n , 'Sum Digits must be Positive and Integer Numbers.'
    if n == 0 :
        return 0
    else:
        return int(n%10) + SumOfDigits(int(n/10))
print(SumOfDigits(459))

# -how to calculate  power of a number using recursion-#
def PowerNum(base,exp):
    assert exp >= 0 and int(exp) == exp , 'powers cannot be non integer or negative'
    if exp == 1 :
        return base
    if exp == 0 :
        return 1
    else:
        return base * PowerNum(base, exp-1)
print(PowerNum(4,4 ))

#-how to find greatest common divisor of two numbers using rcursion-#
def GrCoDi(num1,num2):
    assert int(num1) == num1 and int(num2) == num2 , 'the numbers must be integer only'
    if num1 < 0:
        num1 = -1 * num1
    if num2 < 0:
        num2 = -1 * num2
    if num2 == 0:
        return num1
    else:
        return GrCoDi(num2, num1%num2)
print(GrCoDi(576,64))

#-how to convert decimal number to binary number using recursion-#
def DecToBin(n):
    if n == 0 :
        return 0
    
    else:
        return n % 2 + 10*DecToBin(int(n/2))
print(DecToBin(24))


def upper1(str,i):
    if len(str)>i:
        return i + 1
        if str[i]==0:
           return upper1(str,i+1)
    else:
        str[i]=str[i]+65
        upper1(str,i+1)
str = "hello world"
upper1(str,0)
print(str)

#-how to capitalize function using recurtion-#
def upper1(str1, i):
    if len(str1) > i:
        if str1[i] == " " or ord(str1[i]) < 92:
           return upper1(str1, i+1)
        else:
            str1[i] = (chr(ord(str1[i])-32))
            return upper1(str1, i+1)


str1 = list("hello world")
upper1(str1, 0)
print("".join(str1))

#-how to capatalize functions first letter of a string using recurtion-#
def FirstUpper(str,i):
    if len(str) <= i:
        return str
    else:
        str.append(str[0][0].upper()+str[0][1:])
        return FirstUpper(str[1:], i+1)
print(FirstUpper(['hi','i','am','shubhi'],0))

#-how can we collect string using recursion-#
def CollectStr(obj):
    result = []
    for key in obj: 
        if type(obj[key]) is str:
             result.append(obj[key])
        if type(obj[key]) is dict:
             result = result + CollectStr(obj[key])
    return result

obj = {
  "stuff": 'you gotta do it',
  "data": {
    "val": {
      "thing": {
        "info": 'asap',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'for yourself'
          }
        }
      }
    }
  }
}
print(CollectStr(obj))

#-how to find factorial of any number using recursion-#
def fact(num):
    if num <= 1:
        return 1 
    else:
        return num * fact(num - 1)
print(fact(5))

#-find the fibonacci numbers using recursion-#
def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2)
print(fib(28)) 

#-write the flatten code using recursion-#
def flatten(arr) :
    resultArr = []
    for custItem in arr :
        if type(custItem) is list :
             resultArr.extend(flatten(custItem)) #ek bar me pura list push karega ye 
        else :
             resultArr.append(custItem)#ek bar me ek hi element push krega stack me 
    return resultArr

print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]

#-how to write code for palindrome in recursion-#
def palindrom(x) :
    if len(x) == 0 :        #-because empty string is called a palindrome 
        return True
    if x[0] != x[len(x)- 1] :
        return False
    return palindrom(x[1 : -1])

print(palindrom('aaabbbaaa'))
print(palindrom('Shubhihbuhs'))