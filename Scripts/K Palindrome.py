# http://www.geeksforgeeks.org/find-if-string-is-k-palindrome-or-not/

def is_k_palindrome(s: str, k: int) -> bool:
    # reverse string
    rev_s = s[::-1]
    cols = rows = len(s) + 1

    dp_array = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):

            # first string is empty : remove all chars from sec string
            if i == 0:
                dp_array[i][j] = j
            # sec string is empty : remove all chars from first string
            elif j == 0:
                dp_array[i][j] = i

            # same chars
            elif s[i - 1] == rev_s[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1]

            # different chars : remove from first char or remove from sec char
            else:
                dp_array[i][j] = min(dp_array[i - 1][j], dp_array[i][j - 1]) + 1

    return True if dp_array[rows - 1][cols - 1] <= (k*2) else False

# main
if __name__ == "__main__":
    string = input().strip()
    k = int(input())

    possible_pal = is_k_palindrome(string, k)

    if possible_pal:
        print("Palindrome is possible")
    else:
        print("Palindrome not possible")

"""
Input Explanation :
 - String
 - k (number of deletions possible)

Input :
> abcdecba 
  1

> acdcb 
  1

Output :
Palindrome is possible
Palindrome not possible

"""

'''
Given a string, find out if the string is K-Palindrome or not. A k-palindrome string transforms into a palindrome on 
removing at most k characters from it.

Examples :

Input : String - abcdecba, k = 1
Output : Yes
String can become palindrome by remo-
-ving 1 character i.e. either d or e)


Input  : String - abcdeca, K = 2
Output : Yes
Can become palindrome by removing
2 characters b and e.

Input : String - acdcb, K = 1
Output : No
String can not become palindrome by
removing only one character.
Recommended: Please try your approach on {IDE} first, before moving on to the solution.

If we carefully analyze the problem, the task is to transform the given string into its reverse by removing at most K 
characters from it. The problem is basically a variation of Edit Distance. We can modify the Edit Distance problem to 
consider given string and its reverse as input and only operation allowed is deletion. Since given string is compared 
with its reverse, we will do at most N deletions from first string and N deletions from second string to make them 
equal. Therefore, for a string to be k-palindrome, 2*N <= 2*K should hold true. Below are the detailed steps of 
algorithm - Process all characters one by one staring from either from left or right sides of both strings. Let us 
traverse from the right corner, there are two possibilities for every pair of character being traversed.

If last characters of two strings are same, we ignore last characters and get count for remaining strings. So we recur 
for lengths m-1 and n-1 where m is length of str1 and n is length of str2.
If last characters are not same, we consider remove operation on last character of first string and last character of 
second string, recursively compute minimum cost for the operations and take minimum of two values.
Remove last char from str1: Recur for m-1 and n.
Remove last char from str2: Recur for m and n-1.
Below is Naive recursive C++ implementation of above approach.

// A Naive recursive C++ program to find
// if given string is K-Palindrome or not
#include<bits/stdc++.h>
using namespace std;
 
// find if given string is K-Palindrome or not
int isKPalRec(string str1, string str2, int m, int n)
{
    // If first string is empty, the only option is to
    // remove all characters of second string
    if (m == 0) return n;
 
    // If second string is empty, the only option is to
    // remove all characters of first string
    if (n == 0) return m;
 
    // If last characters of two strings are same, ignore
    // last characters and get count for remaining strings.
    if (str1[m-1] == str2[n-1])
        return isKPalRec(str1, str2, m-1, n-1);
 
    // If last characters are not same,
    // 1. Remove last char from str1 and recur for m-1 and n
    // 2. Remove last char from str2 and recur for m and n-1
    // Take minimum of above two operations
    return 1 + min(isKPalRec(str1, str2, m-1, n), // Remove from str1
                   isKPalRec(str1, str2, m, n-1)); // Remove from str2
}
 
// Returns true if str is k palindrome.
bool isKPal(string str, int k)
{
    string revStr = str;
    reverse(revStr.begin(), revStr.end());
    int len = str.length();
 
    return (isKPalRec(str, revStr, len, len) <= k*2);
}
 
// Driver program
int main()
{
    string str = "acdcb";
    int k = 2;
    isKPal(str, k)? cout << "Yes" : cout << "No";
    return 0;
}
Run on IDE
Output :

Yes
The time complexity of above solution is exponential. In worst case, we may end up doing O(2n) operations. The worst 
case happens string contains all distinct characters.

This problem has both properties (see this and this) of a dynamic programming problem. Like other typical 
Dynamic Programming(DP) problems, re-computations of same subproblems can be avoided by constructing a temporary array 
that stores results of subproblems .

Below is Bottom-up implementation of above recursive approach.

// C++ program to find if given string is K-Palindrome or not
#include <bits/stdc++.h>
using namespace std;
 
// find if given string is K-Palindrome or not
int isKPalDP(string str1, string str2, int m, int n)
{
    // Create a table to store results of subproblems
    int dp[m + 1][n + 1];
 
    // Fill dp[][] in bottom up manner
    for (int i = 0; i <= m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            // If first string is empty, only option is to
            // remove all characters of second string
            if (i == 0)
                dp[i][j] = j; // Min. operations = j
 
            // If second string is empty, only option is to
            // remove all characters of first string
            else if (j == 0)
                dp[i][j] = i; // Min. operations = i
 
            // If last characters are same, ignore last character
            // and recur for remaining string
            else if (str1[i - 1] == str2[j - 1])
                dp[i][j] = dp[i - 1][j - 1];
 
            // If last character are different, remove it
            // and find minimum
            else
             dp[i][j] = 1 + min(dp[i - 1][j], // Remove from str1
                             dp[i][j - 1]); // Remove from str2
        }
    }
 
    return dp[m][n];
}
 
// Returns true if str is k palindrome.
bool isKPal(string str, int k)
{
    string revStr = str;
    reverse(revStr.begin(), revStr.end());
    int len = str.length();
 
    return (isKPalDP(str, revStr, len, len) <= k*2);
}
 
// Driver program
int main()
{
    string str = "acdcb";
    int k = 2;
    isKPal(str, k)? cout << "Yes" : cout << "No";
    return 0;
}
Run on IDE
Output :

Yes
Time complexity of above solution is O(m x n). We can improve time complexity by making use of the fact that only k 
deletions are allowed. Auxiliary space used is O(m x n).
'''
