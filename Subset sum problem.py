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
if __name__=="__main__":
    array=list(map(int,input().split()))
    req_sum=int(input())

    #Sort by ascending order
    array.sort()
    find_subset(array,req_sum)

"""
Input Explanation :
 - List of numbers
 - Required sum for which subset is to be found

Input : 
3 5 8 11
13

Output :
Subset for sum 13  :
8
5

"""

'''
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
Let isSubSetSum(int set[], int n, int sum) be the function to find whether there is a subset of set[] with sum equal to sum. n is the number of elements in set[].

The isSubsetSum problem can be divided into two subproblems
…a) Include the last element, recur for n = n-1, sum = sum – set[n-1]
…b) Exclude the last element, recur for n = n-1.
If any of the above the above subproblems return true, then return true.

Following is the recursive formula for isSubsetSum() problem.

isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) || 
                           isSubsetSum(set, n-1, sum-set[n-1])
Base Cases:
isSubsetSum(set, n, sum) = false, if sum > 0 and n == 0
isSubsetSum(set, n, sum) = true, if sum == 0 
Following is naive recursive implementation that simply follows the recursive structure mentioned above.
CJava
// A recursive solution for subset sum problem
#include <stdio.h>
 
// Returns true if there is a subset of set[] with sun equal to given sum
bool isSubsetSum(int set[], int n, int sum)
{
   // Base Cases
   if (sum == 0)
     return true;
   if (n == 0 && sum != 0)
     return false;
 
   // If last element is greater than sum, then ignore it
   if (set[n-1] > sum)
     return isSubsetSum(set, n-1, sum);
 
   /* else, check if sum can be obtained by any of the following
      (a) including the last element
      (b) excluding the last element   */
   return isSubsetSum(set, n-1, sum) || 
                        isSubsetSum(set, n-1, sum-set[n-1]);
}
 
// Driver program to test above function
int main()
{
  int set[] = {3, 34, 4, 12, 5, 2};
  int sum = 9;
  int n = sizeof(set)/sizeof(set[0]);
  if (isSubsetSum(set, n, sum) == true)
     printf("Found a subset with given sum");
  else
     printf("No subset with given sum");
  return 0;
}
Run on IDE

Output:
 Found a subset with given sum 
The above solution may try all subsets of given set in worst case. Therefore time complexity of the above solution is exponential. The problem is in-fact NP-Complete (There is no known polynomial time solution for this problem).

We can solve the problem in Pseudo-polynomial time using Dynamic programming. We create a boolean 2D table subset[][] and fill it in bottom up manner. The value of subset[i][j] will be true if there is a subset of set[0..j-1] with sum equal to i., otherwise false. Finally, we return subset[sum][n]
CJava
// A Dynamic Programming solution for subset sum problem
#include <stdio.h>
  
// Returns true if there is a subset of set[] with sun equal to given sum
bool isSubsetSum(int set[], int n, int sum)
{
    // The value of subset[i][j] will be true if there is a 
    // subset of set[0..j-1] with sum equal to i
    bool subset[n+1][sum+1];
  
    // If sum is 0, then answer is true
    for (int i = 0; i <= n; i++)
      subset[i][0] = true;
  
    // If sum is not 0 and set is empty, then answer is false
    for (int i = 1; i <= sum; i++)
      subset[0][i] = false;
  
     // Fill the subset table in botton up manner
     for (int i = 1; i <= n; i++)
     {
       for (int j = 1; j <= sum; j++)
       {
         if(j<set[i-1])
         subset[i][j] = subset[i-1][j];
         if (j >= set[i-1])
           subset[i][j] = subset[i-1][j] || 
                                 subset[i - 1][j-set[i-1]];
       }
     }
  
     /*   // uncomment this code to print table
     for (int i = 0; i <= n; i++)
     {
       for (int j = 0; j <= sum; j++)
          printf ("%4d", subset[i][j]);
       printf("n");
     }*/
  
     return subset[n][sum];
}
  
// Driver program to test above function
int main()
{
  int set[] = {1,2,3};
  int sum = 7;
  int n = sizeof(set)/sizeof(set[0]);
  if (isSubsetSum(set, n, sum) == true)
     printf("Found a subset with given sum");
  else
     printf("No subset with given sum");
  return 0;
}
// This code is contributed by Arjun Tyagi.
Run on IDE

Output:
Found a subset with given sum
Time complexity of the above solution is O(sum*n).Subset Sum Problem in O(sum) space
Perfect Sum Problem (Print all subsets with given sum)
'''
