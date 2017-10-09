# http://www.geeksforgeeks.org/longest-common-subsequence/

def lcs(s1: str, s2: str):
    # rows -> s1 , cols -> s2
    rows = len(s1) + 1
    cols = len(s2) + 1

    # row0 and col0 will be 0 as they will signify null strings
    dp_array = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):

            # if the chars match, go for left-top diagonal value + 1
            if s1[i - 1] == s2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            # otherwise get max of top or left
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])

    # length of longest common sub-sequence
    # return dp_array[rows-1][cols-1]

    # store the common sequence (will be stored in reverse)
    sub_sequence = []

    i = rows - 1
    j = cols - 1

    # find the lcs
    while i > 0 and j > 0:
        # if top is not equal, that means present char was used
        if dp_array[i][j] != dp_array[i - 1][j]:
            sub_sequence.append(s1[i - 1])
            i -= 1
            j -= 1
        # not used
        else:
            i -= 1

    # return length of lcs, list of char containing the lcs elements
    return dp_array[rows - 1][cols - 1], sub_sequence[::-1]

# main
if __name__ == "__main__":
    s1, s2 = input().split()

    max_lcs, sequence = lcs(s1, s2)

    print("Length of longest common sub-sequence")
    print(max_lcs)
    print("Longest commmon sub-sequence")
    print(''.join(sequence))

"""
Input Explanation :
 - Two strings with space as delimiter

Input :
AGGTAB GXTXAYB

Output :
Length of longest common sub-sequence
4
Longest commmon subsequence
GTAB

"""

'''
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A 
subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, 
“abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different 
possible subsequences.

It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences 
between two files), and has applications in bioinformatics.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

The naive solution for this problem is to generate all subsequences of both given sequences and find the longest 
matching subsequence. This solution is exponential in term of time complexity. Let us see how this problem possesses 
both important properties of a Dynamic Programming (DP) Problem.

1) Optimal Substructure: 
Let the input sequences be X[0..m-1] and Y[0..n-1] of lengths m and n respectively. And let L(X[0..m-1], Y[0..n-1]) be 
the length of LCS of the two sequences X and Y. Following is the recursive definition of L(X[0..m-1], Y[0..n-1]).

If last characters of both sequences match (or X[m-1] == Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2])

Examples:
1) Consider the input strings “AGGTAB” and “GXTXAYB”. Last characters match for the strings. So length of LCS can be 
written as:
L(“AGGTAB”, “GXTXAYB”) = 1 + L(“AGGTA”, “GXTXAY”)
longest-common-subsequence
2) Consider the input strings “ABCDGH” and “AEDFHR. Last characters do not match for the strings. So length of LCS can 
be written as:
L(“ABCDGH”, “AEDFHR”) = MAX ( L(“ABCDG”, “AEDFHR”), L(“ABCDGH”, “AEDFH”) )

So the LCS problem has optimal substructure property as the main problem can be solved using solutions to subproblems.

2) Overlapping Subproblems:
Following is simple recursive implementation of the LCS problem. The implementation simply follows the recursive 
structure mentioned above.

C/C++JavaPython
/* A Naive recursive implementation of LCS problem */
#include<bits/stdc++.h>
 
int max(int a, int b);
 
/* Returns length of LCS for X[0..m-1], Y[0..n-1] */
int lcs( char *X, char *Y, int m, int n )
{
   if (m == 0 || n == 0)
     return 0;
   if (X[m-1] == Y[n-1])
     return 1 + lcs(X, Y, m-1, n-1);
   else
     return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
}
 
/* Utility function to get max of 2 integers */
int max(int a, int b)
{
    return (a > b)? a : b;
}
 
/* Driver program to test above function */
int main()
{
  char X[] = "AGGTAB";
  char Y[] = "GXTXAYB";
 
  int m = strlen(X);
  int n = strlen(Y);
 
  printf("Length of LCS is %dn", lcs( X, Y, m, n ) );
 
  return 0;
}
Run on IDE

Output:
Length of LCS is 4
Time complexity of the above naive recursive approach is O(2^n) in worst case and worst case happens when all 
characters of X and Y mismatch i.e., length of LCS is 0.
Considering the above implementation, following is a partial recursion tree for input strings “AXYT” and “AYZX”

                         lcs("AXYT", "AYZX")
                       /                 
         lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
         /                              /               
lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")
In the above partial recursion tree, lcs(“AXY”, “AYZ”) is being solved twice. If we draw the complete recursion tree, 
then we can see that there are many subproblems which are solved again and again. So this problem has Overlapping 
Substructure property and recomputation of same subproblems can be avoided by either using Memoization or Tabulation. 
Following is a tabulated implementation for the LCS problem.

C/C++JavaPython
/* Dynamic Programming C/C++ implementation of LCS problem */
#include<bits/stdc++.h>
  
int max(int a, int b);
  
/* Returns length of LCS for X[0..m-1], Y[0..n-1] */
int lcs( char *X, char *Y, int m, int n )
{
   int L[m+1][n+1];
   int i, j;
  
   /* Following steps build L[m+1][n+1] in bottom up fashion. Note 
      that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] */
   for (i=0; i<=m; i++)
   {
     for (j=0; j<=n; j++)
     {
       if (i == 0 || j == 0)
         L[i][j] = 0;
  
       else if (X[i-1] == Y[j-1])
         L[i][j] = L[i-1][j-1] + 1;
  
       else
         L[i][j] = max(L[i-1][j], L[i][j-1]);
     }
   }
    
   /* L[m][n] contains length of LCS for X[0..n-1] and Y[0..m-1] */
   return L[m][n];
}
  
/* Utility function to get max of 2 integers */
int max(int a, int b)
{
    return (a > b)? a : b;
}
  
/* Driver program to test above function */
int main()
{
  char X[] = "AGGTAB";
  char Y[] = "GXTXAYB";
  
  int m = strlen(X);
  int n = strlen(Y);
  
  printf("Length of LCS is %dn", lcs( X, Y, m, n ) );
 
  return 0;
}
Run on IDE

Time Complexity of the above implementation is O(mn) which is much better than the worst case time complexity of Naive Recursive implementation.
'''
