# http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
# easier method follows Fibonacci Series

def non_consecutive_1(n: int):
    # a : ending with 0 (can append both 0 or 1 to it)
    # b : ending with 1 (can append only 0 to it)
    a = [0] * n
    b = [0] * n

    a[0] = 1
    b[0] = 1

    # 1 -> n-1 (use DP)
    for i in range(1, n):
        a[i] = a[i - 1] + b[i - 1]
        b[i] = a[i - 1]

    return a[n - 1] + b[n - 1]

# main
if __name__ == "__main__":
    n = int(input())

    count = non_consecutive_1(n)
    print("Number of binary numbers with non-consecutive 1s possible is")
    print(count)

"""
Input Explanation :
 - integer representing length of the binary string

For 4,  list having non-consecutive '1's is 
[0001][0010][0100][1000][1010][1001][0101][0000]

Input :
4

Output :
8

"""

'''
This problem can be solved using Dynamic Programming. Let a[i] be the number of binary strings of length i which do not
 contain any two consecutive 1’s and which end in 0. Similarly, let b[i] be the number of such strings which end in 1. 
 We can append either 0 or 1 to a string ending in 0, but we can only append 0 to a string ending in 1. This yields the 
 recurrence relation:

a[i] = a[i - 1] + b[i - 1]
b[i] = a[i - 1] 
The base cases of above recurrence are a[1] = b[1] = 1. The total number of strings of length i is just a[i] + b[i].

Following is the implementation of above solution. In the following implementation, indexes start from 0. So a[i] 
represents the number of binary strings for input length i+1. Similarly, b[i] represents binary strings for input 
length i+1.

C++Java
// C++ program to count all distinct binary strings
// without two consecutive 1's
#include <iostream>
using namespace std;
 
int countStrings(int n)
{
    int a[n], b[n];
    a[0] = b[0] = 1;
    for (int i = 1; i < n; i++)
    {
        a[i] = a[i-1] + b[i-1];
        b[i] = a[i-1];
    }
    return a[n-1] + b[n-1];
}
 
 
// Driver program to test above functions
int main()
{
    cout << countStrings(3) << endl;
    return 0;
}
Run on IDE

Output:
5
Source:
courses.csail.mit.edu/6.006/oldquizzes/solutions/q2-f2009-sol.pdf

If we take a closer look at the pattern, we can observe that the count is actually (n+2)’th Fibonacci number for n >= 1.
 The Fibonacci Numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, ….

n = 1, count = 2  = fib(3)
n = 2, count = 3  = fib(4)
n = 3, count = 5  = fib(5)
n = 4, count = 8  = fib(6)
n = 5, count = 13 = fib(7)
................
Therefore we can count the strings in O(Log n) time also using the method 5 here
'''
