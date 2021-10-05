import random


def rand_arr():
    arr = []
    for i in range(10):
        arr.append(random.randint(1, 20))
    smallest = arr[0]
    sum = 0
    for a in arr:
        sum = a + sum
        if a <= smallest:
            smallest = a
            smallindex = arr.index(smallest)
    mean = sum / 10
    print(arr)
    print("the mean is :,", mean)
    print("the smallest number is : ", smallest)
    print("the index is at : ", smallindex)


print(rand_arr())


def int_to_array(n):
    array1 = []
    while n > 0:
        array1.append(n % 10)
        n = n // 10
        array1 = array1[::-1]
    print(array1)


print(int_to_array(123))
