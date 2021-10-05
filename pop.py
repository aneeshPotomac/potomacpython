import random

arr=[]
# Press the green button in the gutter to run the script.
for i in range(10):
    arr.append( random.randint(1,20) )
smallest = arr[0]
sum = 0
for a in arr:
    sum = a + sum
    if a <= smallest:
        smallest = a
        smallindex = arr.index(smallest)
mean = sum/10
print(arr)
print("the mean is :,", mean)
print("the smallest number is : ", smallest)
print("the index is at : ", smallindex)
array1 = []




num = int(input())
for i < :

    array1.append(elements)  # adding the element

print(array1)