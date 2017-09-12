#http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

def calculate_distance(s1,s2):
    n1=len(s1)
    n2=len(s2)

    #DP row and col
    row=n1+1        #DP table requires +1 (for Null string)
    col=n2+1        #DP table requires +1 (for Null string)
    #DP Array
    dp_array = [[0]*col for i in range(row)]

    for i in range(row):
        for j in range(col):
            #either i or j is 0 (for converting to Null)
            if i==0:
                dp_array[i][j] = j
                continue
            if j==0:
                dp_array[i][j] = i
                continue

            #The chars don't match, so perform operation
            if s1[i-1]!=s2[j-1]:
                #Get min from updown L shape ([i-1][j], [i-1][j-1], [i][j-1]) and add 1 (performing operation)
                dp_array[i][j] = min(dp_array[i-1][j],dp_array[i][j-1],dp_array[i-1][j-1]) +1

            #Same chars, so no need for operation, hence take previous row:col values
            else:
                dp_array[i][j]=dp_array[i-1][j-1]

    #return right-bottom-most value
    return dp_array[row-1][col-1]

#main
if __name__=="__main__":
    s1,s2 = input().split()
    dist_data = calculate_distance(s1, s2)
    print("Number of operations required :")
    print(dist_data)

"""
Input Explanation :
 - Two space seperated strings

Input :
abcdef axcdy

Output :
Number of operations required :
3

"""

'''
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Examples:

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
What are the subproblems in this case?
The idea is process all characters one by one staring from either from left or right sides of both strings.
Let we traverse from right corner, there are two possibilities for every pair of character being traversed.

m: Length of str1 (first string)
n: Length of str2 (second string)
If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings. So we recur for lengths m-1 and n-1.
Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values.
Insert: Recur for m and n-1
Remove: Recur for m-1 and n
Replace: Recur for m-1 and n-1

We can see that many subproblems are solved again and again, for example eD(2,2) is called three times. Since same suproblems are called again, this problem has Overlapping Subprolems property. So Edit Distance problem has both properties (see this and this) of a dynamic programming problem. Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided by constructing a temporary array that stores results of subpriblems.

C++JavaPython
// A Dynamic Programming based C++ program to find minimum
// number operations to convert str1 to str2
#include<bits/stdc++.h>
using namespace std;
 
// Utility function to find minimum of three numbers
int min(int x, int y, int z)
{
    return min(min(x, y), z);
}
 
int editDistDP(string str1, string str2, int m, int n)
{
    // Create a table to store results of subproblems
    int dp[m+1][n+1];
 
    // Fill d[][] in bottom up manner
    for (int i=0; i<=m; i++)
    {
        for (int j=0; j<=n; j++)
        {
            // If first string is empty, only option is to
            // isnert all characters of second string
            if (i==0)
                dp[i][j] = j;  // Min. operations = j
 
            // If second string is empty, only option is to
            // remove all characters of second string
            else if (j==0)
                dp[i][j] = i; // Min. operations = i
 
            // If last characters are same, ignore last char
            // and recur for remaining string
            else if (str1[i-1] == str2[j-1])
                dp[i][j] = dp[i-1][j-1];
 
            // If last character are different, consider all
            // possibilities and find minimum
            else
                dp[i][j] = 1 + min(dp[i][j-1],  // Insert
                                   dp[i-1][j],  // Remove
                                   dp[i-1][j-1]); // Replace
        }
    }
 
    return dp[m][n];
}
 
// Driver program
int main()
{
    // your code goes here
    string str1 = "sunday";
    string str2 = "saturday";
 
    cout << editDistDP(str1, str2, str1.length(), str2.length());
 
    return 0;
}
Run on IDE
Output:

3
Time Complexity: O(m x n)
Auxiliary Space: O(m x n)
'''