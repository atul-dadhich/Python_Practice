array = [1 ,2 ,3 ,4 ,5 ,6]

left = 0
right = len(array)-1

print array[left]
print array[right]

for i in array:
    if array[left] >= array[right]:
        print array[left]



    #else:
     #   print array[right]
