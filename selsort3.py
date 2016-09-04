import random
import time
sssum = 0
ssruntimedist = []
def dblselsort():
    arr = []
    for k in range(0,1000):
        arr.append(int(round(random.random()*10000)))
    #arr = [4,3,2,1,0,0,1,2,3,4,4,3,2,1,0]
    minimum = arr[0]
    maximum = arr[0]
    min_index = 0
    max_index = 0
    j = 0
    #print arr
    start_time = time.time()
    while j < len(arr)/2:
        minimum = arr[j]
        maximum = arr[j]
        min_index = j
        max_index = j
        for i in range(j, len(arr)-j):
            if arr[i] < minimum :
                minimum = arr[i]
                min_index = i
            if arr[i] > maximum :
                maximum = arr[i]
                max_index = i
        if max_index == j and min_index == len(arr)-1-j:
            (arr[max_index], arr[min_index]) = (arr[min_index],arr[max_index])
        elif max_index == j :
            (arr[max_index], arr[len(arr)-1-j]) = (arr[len(arr)-1-j], arr[max_index])
            (arr[min_index], arr[j]) = (arr[j], arr[min_index])
        elif min_index == len(arr)-1-j:
            (arr[min_index], arr[j]) = (arr[j], arr[min_index])
            (arr[max_index], arr[len(arr)-1-j]) = (arr[len(arr)-1-j], arr[max_index])
        else:
            (arr[j], arr[len(arr) - j-1] ,arr[min_index], arr[max_index] ) = (arr[min_index], arr[max_index] ,arr[j], arr[len(arr) - j-1])
        #print str(arr)+', j:'+str(j)+', minimum'+str(minimum)+', maximum'+str(maximum)+',min/max_index:'+str(min_index)+', '+str(max_index)
        j += 1
    end_time = time.time()
    run_time = (end_time - start_time)*1000
    #print run_time
    return run_time

dblselsort()

def dblselsortdist():
    sssum = 0
    for l in range(0,50):
        run_time= dblselsort()
        sssum +=run_time
    meansstime = sssum/50
    print "mean double selectionsort time (msec) :" + str(meansstime)

dblselsortdist()
