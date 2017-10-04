# http://www.geeksforgeeks.org/knapsack-problem/

def knapsack(v: list, w: list, max_weight: int):
    rows = len(v) + 1
    cols = max_weight + 1

    # adding dummy values as later on we consider these values as indexed from 1 for convinence
    v = [0] + v[:]
    w = [0] + w[:]

    # row : values , #col : weights
    dp_array = [[0 for i in range(cols)] for j in range(rows)]

    # 0th row and 0th column have value 0

    # values
    for i in range(1, rows):
        # weights
        for j in range(1, cols):
            # if this weight exceeds max_weight at that point
            if j - w[i] < 0:
                dp_array[i][j] = dp_array[i - 1][j]

            # max of -> last ele taken | this ele taken + max of previous values possible
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], v[i] + dp_array[i - 1][j - w[i]])

    # return dp_array[rows][cols]  : will have the max value possible for given wieghts

    values_chosen = []
    i = rows - 1
    j = cols - 1

    # Get the items to be picked
    while i > 0 and j > 0:

        # ith element is added
        if dp_array[i][j] != dp_array[i - 1][j]:
            # add the value
            values_chosen.append(v[i])
            # decrease the weight possible (j)
            j = j - w[i]
            # go to previous row
            i = i - 1

        else:
            i = i - 1

    return dp_array[rows - 1][cols - 1], values_chosen

# main
if __name__ == "__main__":
    values = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    max_weight = int(input())

    max_value, values_chosen = knapsack(values, weights, max_weight)

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
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the 
knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
 associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum 
 value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an 
 item, either pick the complete item, or don’t pick it (0-1 property).

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

A simple solution is to consider all subsets of items and calculate the total weight and value of all subsets. Consider 
the only subsets whose total weight is smaller than W. From all such subsets, pick the maximum value subset.

1) Optimal Substructure:
To consider all subsets of items, there can be two cases for every item: (1) the item is included in the optimal subset,
 (2) not included in the optimal set.
Therefore, the maximum value that can be obtained from n items is max of following two values.
1) Maximum value obtained by n-1 items and W weight (excluding nth item).
2) Value of nth item plus maximum value obtained by n-1 items and W minus weight of the nth item (including nth item).

If weight of nth item is greater than W, then the nth item cannot be included and case 1 is the only possibility.

2) Overlapping Subproblems
Following is recursive implementation that simply follows the recursive structure mentioned above.
C/C++JavaPython
/* A Naive recursive implementation of 0-1 Knapsack problem */
#include<stdio.h>
 
// A utility function that returns maximum of two integers
int max(int a, int b) { return (a > b)? a : b; }
 
// Returns the maximum value that can be put in a knapsack of capacity W
int knapSack(int W, int wt[], int val[], int n)
{
   // Base Case
   if (n == 0 || W == 0)
       return 0;
 
   // If weight of the nth item is more than Knapsack capacity W, then
   // this item cannot be included in the optimal solution
   if (wt[n-1] > W)
       return knapSack(W, wt, val, n-1);
 
   // Return the maximum of two cases: 
   // (1) nth item included 
   // (2) not included
   else return max( val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                    knapSack(W, wt, val, n-1)
                  );
}
 
// Driver program to test above function
int main()
{
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int  W = 50;
    int n = sizeof(val)/sizeof(val[0]);
    printf("%d", knapSack(W, wt, val, n));
    return 0;
}
Run on IDE

Output:
220
It should be noted that the above function computes the same subproblems again and again. See the following recursion 
tree, K(1, 1) is being evaluated twice. Time complexity of this naive recursive solution is exponential (2^n).

In the following recursion tree, K() refers to knapSack().  The two 
parameters indicated in the following recursion tree are n and W.  
The recursion tree is for following sample inputs.
wt[] = {1, 1, 1}, W = 2, val[] = {10, 20, 30}

                       K(3, 2)         ---------> K(n, W)
                   /            \ 
                 /                \               
            K(2,2)                  K(2,1)
          /       \                  /    \ 
        /           \              /        \
       K(1,2)      K(1,1)        K(1,1)     K(1,0)
       /  \         /   \          /   \
     /      \     /       \      /       \
K(0,2)  K(0,1)  K(0,1)  K(0,0)  K(0,1)   K(0,0)
Recursion tree for Knapsack capacity 2 units and 3 items of 1 unit weight.
Since suproblems are evaluated again, this problem has Overlapping Subprolems property. So the 0-1 Knapsack problem has 
both properties (see this and this) of a dynamic programming problem. Like other typical Dynamic Programming(DP) 
problems, recomputations of same subproblems can be avoided by constructing a temporary array K[][] in bottom up manner.
 Following is Dynamic Programming based implementation.

C++JavaPython
// A Dynamic Programming based solution for 0-1 Knapsack problem
#include<stdio.h>
 
// A utility function that returns maximum of two integers
int max(int a, int b) { return (a > b)? a : b; }
 
// Returns the maximum value that can be put in a knapsack of capacity W
int knapSack(int W, int wt[], int val[], int n)
{
   int i, w;
   int K[n+1][W+1];
 
   // Build table K[][] in bottom up manner
   for (i = 0; i <= n; i++)
   {
       for (w = 0; w <= W; w++)
       {
           if (i==0 || w==0)
               K[i][w] = 0;
           else if (wt[i-1] <= w)
                 K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]);
           else
                 K[i][w] = K[i-1][w];
       }
   }
 
   return K[n][W];
}
 
int main()
{
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int  W = 50;
    int n = sizeof(val)/sizeof(val[0]);
    printf("%d", knapSack(W, wt, val, n));
    return 0;
}
Run on IDE

Output:
220
Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.
'''
