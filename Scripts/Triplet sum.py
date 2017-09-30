#http://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

def triplet_sum(array: list, req_sum: int):
    triplets = []

    if len(array) < 3:
        return None

    array = sorted(array)

    #First loop takes the center value among the triplet
    for mid in range(1,len(array)):
        low = 0
        high = len(array) - 1

        while low<mid and high>mid :

            #if required sum triplet
            if array[low]+array[mid]+array[high] == req_sum:
                triplets.append([array[low], array[mid], array[high]])
                break

            #if present sum is greater than required sum, decrease high
            elif array[low]+array[mid]+array[high] > req_sum :
                high = high - 1
                continue


            # if present sum is lower than required sum, increase low
            else :
                low = low + 1
                continue

    #if atleast 1 triplet found
    if len(triplets) > 0 :
        return triplets
    else :
        return None

#main
if __name__=="__main__":
    array = list(map(int,input().split()))
    req_sum = int(input())

    triplets = triplet_sum(array, req_sum)

    if triplets is None :
        print("No Triplet exist for sum :", req_sum)
    else :
        print("Triplet for the sum", req_sum)
        for triple in triplets:
            print(' '.join(str(x) for x in triple))

"""
Input Explanation :
 - list of numbers
 - required sum

Input :
0 -1 1 2 3 4 -3 -2
3

Output :
Triplet for the sum 3
-1 0 4
-2 1 4
-3 2 4

"""

'''
<GeeksforGeeks page content>
'''