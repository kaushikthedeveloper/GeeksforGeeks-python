#http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

def find_subset(weight, req_sum):
    l=len(weight)

    #ROWS : array
    #COL : range(sum)
    row=l
    col=req_sum+1

    #2d array storing Sum
    dp_array=[[0]*col for i in range(row)]

    for i in range(row):
        for j in range(1,col):
            #Row 0
            if i==0:
                if j>=weight[i]:
                    dp_array[i][j]=weight[i]
                else:
                    continue
            else:
                if j-weight[i]>=0:
                    dp_array[i][j]=max(dp_array[i-1][j], (weight[i]+dp_array[i-1][j-weight[i]]) )
                elif j>=weight[i]:
                    #take from row above it
                    dp_array[i][j]=max(dp_array[i-1][j],weight[i])
                else:
                    dp_array[i][j]=dp_array[i-1][j]
    '''
    #print the DP Array
    for i in range(row):
        for j in range(col):
            print(dp_array[i][j], end=" ")
        print()
    '''

    print("Subset for sum",req_sum,' :')

    #Find out which Numbers should be in the subset
    #give from index 0
    row-=1
    col-=1
    while col>=0 and row>=0 and req_sum>0:
        #First Row
        if(row==0):
            print(weight[row])
            break

        #Bottom-Right most ele
        if(dp_array[row][col]!=dp_array[row-1][col]):
            # print(req_sum,' : ',dp_array[row][col],dp_array[row-1][col],' : ',weight[row])
            print(weight[row])
            req_sum-=weight[row]
            col-=weight[row]
            row-=1
        else:
            row-=1

#main
array=list(map(int,input().split()))
req_sum=int(input())
find_subset(array,req_sum)
