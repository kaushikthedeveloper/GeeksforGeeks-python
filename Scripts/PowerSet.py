# http://www.geeksforgeeks.org/power-set/

def power_set(array: list, n: int):
    # Len of PowerSet = 2^n
    max_len = pow(2, n)

    powerSet = []
    for num in range(max_len):
        l = []
        # 0 to n
        for i in range(n):
            if (num & (1 << i)):
                l.append(array[i])
        powerSet.append(l)

    return powerSet


# main
if __name__ == "__main__":
    array = input().split()
    n = len(array)
    powerSet = power_set(array, n)

    # Sort by length
    powerSet = sorted(powerSet, key=len)
    print("Power Set :")
    print(powerSet)

"""
Input Explanation :
 - List of numbers

Input :
1 2 3

Output :
Power Set :
[[], ['1'], ['2'], ['3'], ['1', '2'], ['1', '3'], ['2', '3'], ['1', '2', '3']]

"""

'''
Power Set Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then 
P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.

If S has n elements in it then P(s) will have 2^n elements

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.


Algorithm:

Input: Set[], set_size
1. Get the size of power set
    powet_set_size = pow(2, set_size)
2  Loop for counter from 0 to pow_set_size
     (a) Loop for i = 0 to set_size
          (i) If ith bit in counter is set
               Print ith element from set for this subset
     (b) Print seperator for subsets i.e., newline
Example:

Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc
Program:

#include <stdio.h>
#include <math.h>
 
void printPowerSet(char *set, int set_size)
{
    /*set_size of power set of a set with set_size
      n is (2**n -1)*/
    unsigned int pow_set_size = pow(2, set_size);
    int counter, j;
 
    /*Run from counter 000..0 to 111..1*/
    for(counter = 0; counter < pow_set_size; counter++)
    {
      for(j = 0; j < set_size; j++)
       {
          /* Check if jth bit in the counter is set
             If set then pront jth element from set */
          if(counter & (1<<j))
            printf("%c", set[j]);
       }
       printf("\n");
    }
}
 
/*Driver program to test printPowerSet*/
int main()
{
    char set[] = {'a','b','c'};
    printPowerSet(set, 3);
 
    getchar();
    return 0;
}
Run on IDE
Time Complexity: O(n2^n)

Refer Power Set in Java for implementation in Java and more methods to print power set.

References:
http://en.wikipedia.org/wiki/Power_set
'''
