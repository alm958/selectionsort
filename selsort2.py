import random
import time
arr = []
for k in range(0,100):
    arr.append(int(round(random.random()*10000)))


#arr = [9,8,7,6,6,7,8,9,9,8,7,6,0,2,4,3]
minimum = arr[0]
min_index = 0
print arr
start_time = time.time()
for j in range(0, len(arr)):
    minimum = arr[j]
    min_index = j
    for i in range(j, len(arr)):
        if arr[i] < minimum :
            minimum = arr[i]
            min_index = i
    (arr[j],arr[min_index]) = (arr[min_index],arr[j])
    #print (str(arr)),
    #print ("; swapped indicies :"+str(j)+" ,"+str(min_index)+"; swapped values :"+str(arr[j])+", "+str(arr[min_index]))
end_time = time.time()
print 'sort execution time (miliseconds):'+str((end_time - start_time)*1000)
