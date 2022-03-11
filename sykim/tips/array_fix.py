# global에서는 당연히..
def fix_array(arr):
    arr[3] += 100

arr = list(range(10))
print(arr)
fix_array(arr)
print(arr)

# test안에서도 마찬가지!
def test_arr():
    arr = list(range(10))
    print(arr)
    fix_array(arr)
    print(arr)
test_arr()
