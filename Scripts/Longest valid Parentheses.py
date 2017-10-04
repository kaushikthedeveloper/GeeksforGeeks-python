# http://www.geeksforgeeks.org/length-of-the-longest-valid-substring/

def longest_valid_parentheses(string: str):
    # hold the substring start
    stack = [-1]
    longest_parenth_count = 0
    for i, s in enumerate(string):

        # opening braces
        if s == '(':
            stack.append(i)

        # closing braces
        elif s == ')':
            # pair made
            stack.pop()

            # stack contains '('
            if len(stack) != 0:
                # check if current substring is longest
                longest_parenth_count = max(longest_parenth_count, i - stack[len(stack) - 1])

            # empty stack, push current pos
            else:
                stack.append(i)

    return longest_parenth_count


# main
if __name__ == "__main__":
    string = input()
    longest_parentheses = longest_valid_parentheses(string)

    print("Length of the longest valid parenthesis substring")
    print(longest_parentheses)

"""
Input Explanation :
 - String containing '(' and ')'

Input :
()(()

Output :
Length of the longest valid parenthesis substring
2

"""

'''
Given a string consisting of opening and closing parenthesis, find length of the longest valid parenthesis substring.

Examples:

Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()() 

Input:  ()(()))))
Output: 6
Explanation:  ()(())

An Efficient Solution can solve this problem in O(n) time. The idea is to store indexes of previous starting brackets 
in a stack. The first element of stack is a special element that provides index before beginning of valid substring 
(base for next valid string).


1) Create an empty stack and push -1 to it. The first element
   of stack is used to provide base for next valid string. 

2) Initialize result as 0.

3) If the character is '(' i.e. str[i] == '('), push index 
   'i' to the stack. 
   
2) Else (if the character is ')')
   a) Pop an item from stack (Most of the time an opening bracket)
   b) If stack is not empty, then find length of current valid
      substring by taking difference between current index and
      top of the stack. If current length is more than result,
      then update the result.
   c) If stack is empty, push current index as base for next
      valid substring.

3) Return result.
Below are C++ and Python implementations of above algorithm.

C++JavaPython
// C++ program to find length of the longest valid
// substring
#include<bits/stdc++.h>
using namespace std;
 
int findMaxLen(string str)
{
    int n = str.length();
 
    // Create a stack and push -1 as initial index to it.
    stack<int> stk;
    stk.push(-1);
 
    // Initialize result
    int result = 0;
 
    // Traverse all characters of given string
    for (int i=0; i<n; i++)
    {
        // If opening bracket, push index of it
        if (str[i] == '(')
          stk.push(i);
 
        else // If closing bracket, i.e.,str[i] = ')'
        {
            // Pop the previous opening bracket's index
            stk.pop();
 
            // Check if this length formed with base of
            // current valid substring is more than max 
            // so far
            if (!stk.empty())
                result = max(result, i - stk.top());
 
            // If stack is empty. push current index as 
            // base for next valid substring (if any)
            else stk.push(i);
        }
    }
 
    return result;
}
 
// Driver program
int main()
{
    string str = "((()()";
    cout << findMaxLen(str) << endl;
 
    str = "()(()))))";
    cout << findMaxLen(str) << endl ;
 
    return 0;
}
Run on IDE

Output:
4
6
Explanation with example:

Input: str = "(()()"

Initialize result as 0 and stack with one item -1.

For i = 0, str[0] = '(', we push 0 in stack

For i = 1, str[1] = '(', we push 1 in stack

For i = 2, str[2] = ')', currently stack has [-1, 0, 1], we pop
from the stack and the stack now is [-1, 0] and length of current
valid substring becomes 2 (we get this 2 by subtracting stack top 
from current index).
Since current length is more than current result, we update result.

For i = 3, str[3] = '(', we push again, stack is [-1, 0, 3].

For i = 4, str[4] = ')', we pop from the stack, stack becomes 
[-1, 0] and length of current valid substring becomes 4 (we get 
this 4 by subtracting stack top from current index). 
Since current length is more than current result, we update result. 
'''
