num_array = [1, 2, 3, 4, 5, 6, 7, 1, 7, 8, 4]
pairsum = 8

def find_pairsum(num_array, pairsum):

    num_array.sort()
    pairlist = []

    # Defining the starting position from left and right
    left = 0
    right = len(num_array)-1

    while left < right:
        currentsum = num_array[left] + num_array[right]
        if currentsum == pairsum:
            temp = (num_array[left], num_array[right])
            if temp not in pairlist:
                pairlist.append(temp)
            right -= 1
        elif currentsum < pairsum:
            left += 1
        else:
            right -= 1
    print("Pairs which adds up to {} In This Array Are {}".format(pairsum, pairlist))

# Calling the Function
find_pairsum(num_array, pairsum)
