num_array = [1, 2, 3, 4, 5, 6, 7, 1, 7, 8, 4]
pairsum = 10
pairlist = []
num_array.sort()
# print num_array
for i in range(len(num_array)):
    for j in range(i+1, len(num_array)):
        if num_array[i] + num_array[j] == pairsum:
            temp = (num_array[i], num_array[j])
            if temp not in pairlist:
                pairlist.append(temp)
print("Pairs which adds up to {} In This Array Are {}".format(pairsum, pairlist))
