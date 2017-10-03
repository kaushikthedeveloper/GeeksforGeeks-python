#http://www.geeksforgeeks.org/knapsack-problem/

def knapsack(v: list, w: list, max_weight: int):

    rows = len(v)+1
    cols = max_weight+1

    #adding dummy values as later on we consider these values as indexed from 1 for convinence
    v=[0]+v[:]
    w=[0]+w[:]

    #row : values , #col : weights
    dp_array = [ [0 for i in range(cols)] for j in range(rows)]

    #0th row and 0th column have value 0

    #values
    for i in range(1, rows):
        #weights
        for j in range(1, cols):
            #if this weight exceeds max_weight at that point
            if j-w[i] < 0 :
                dp_array[i][j] = dp_array[i-1][j]

            #max of -> last ele taken | this ele taken + max of previous values possible
            else :
                dp_array[i][j] = max(dp_array[i-1][j] , v[i] + dp_array[i-1][j-w[i]])

    #return dp_array[rows][cols]  : will have the max value possible for given wieghts

    temp_max_weight = max_weight
    values_chosen = []
    i=rows-1; j=cols-1;

    #Get the items to be picked
    while i>0 and j>0 :

        #ith element is added
        if dp_array[i][j] != dp_array[i-1][j] :
            #add the value
            values_chosen.append(v[i])
            #decrease the weight possible (j)
            j=j-w[i]
            #go to previous row
            i=i-1

        else :
            i=i-1

    #print the DP array
    # for i in range(rows):
    #     print()
    #     for j in range(cols):
    #         print(dp_array[i][j],end=' ')

    return dp_array[rows-1][cols-1] , values_chosen


#main
if __name__=="__main__":

    values = list(map(int,input().split()))
    weights = list(map(int,input().split()))
    max_weight = int(input())

    max_value , values_chosen =  knapsack(values, weights, max_weight)

    print("The max value possible is")
    print(max_value)

    print("The values chosen for these are")
    print(' '.join(str(x) for x in values_chosen))


"""
Input Explanation :
 - List of values for the elements in order (ith)
 - List of their respective weights
 - Max weight possible

Input :
25 20 15 40 50
3 2 1 4 5
6

Output :
The max value possible is
65
The values chosen for these are


"""

'''
<GeeksforGeeks page content>
'''