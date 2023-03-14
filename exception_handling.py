import sys

try:
    # if x>5:
    # raise Exception("x should not exceed 5, the value of x was: {}",format(x))
    assert 'linux' in sys.platform, "only run in linux"
# print("doing something")

except Exception as e:
    print("linux function was not executed because", e)