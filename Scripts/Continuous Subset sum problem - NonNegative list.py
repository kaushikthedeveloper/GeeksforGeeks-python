# http://www.geeksforgeeks.org/find-subarray-with-given-sum/
# print the first subset that satisfies the condition

def find_continuous_subset(array: list, req_sum: int):
    left = 0
    right = 0

    temp_sum = array[0]
    while left < len(array):
        if temp_sum == req_sum:
            break

        # subset sum is more than req_sum , so decrease
        if temp_sum < req_sum:
            # subset is at the end and can not increase further : so subset not found
            if right == len(array) - 1:
                break
            right += 1
            temp_sum += array[right]

        # subset sum is less than req_sum , so decrease
        else:
            temp_sum -= array[left]
            left += 1

    # continuous subse for sum is not possible
    if temp_sum != req_sum:
        return None

    sum_subset = array[left:right + 1]
    return sum_subset

# main
if __name__ == "__main__":
    array = list(map(int, input().split()))
    req_sum = int(input())

    sum_subset = find_continuous_subset(array, req_sum)

    # If Sum is not possible
    if sum_subset is None:
        print("Sum :", req_sum, "is not possible")
    else:
        print("Continuous Subset for sum", req_sum)
        print(' '.join(str(x) for x in sum_subset))

"""
Input Explanation :
 - List of numbers
 - Required sum for which subset is to be found

Input :
1 4 0 0 3 10 5
7

Output :
Continuous Subset for sum 7
4 0 0 3
"""

'''
Find subarray with given sum | Set 1 (Nonnegative Numbers)
Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There may be more than one subarrays with sum as the given sum. The following solutions print first such subarray.

Method 2 (Efficient)
Initialize a variable curr_sum as first element. curr_sum indicates the sum of current subarray. Start from the second 
element and add all elements one by one to the curr_sum. If curr_sum becomes equal to sum, then print the solution. If 
curr_sum exceeds the sum, then remove trailing elemnents while curr_sum is greater than sum.

Following is the implementation of the above approach.
CJava
/* An efficient program to print subarray with sum as given sum */
#include<stdio.h>
 
/* Returns true if the there is a subarray of arr[] with sum equal to 'sum'
   otherwise returns false.  Also, prints the result */
int subArraySum(int arr[], int n, int sum)
{
    /* Initialize curr_sum as value of first element
       and starting point as 0 */
    int curr_sum = arr[0], start = 0, i;
 
    /* Add elements one by one to curr_sum and if the curr_sum exceeds the
       sum, then remove starting element */
    for (i = 1; i <= n; i++)
    {
        // If curr_sum exceeds the sum, then remove the starting elements
        while (curr_sum > sum && start < i-1)
        {
            curr_sum = curr_sum - arr[start];
            start++;
        }
 
        // If curr_sum becomes equal to sum, then return true
        if (curr_sum == sum)
        {
            printf ("Sum found between indexes %d and %d", start, i-1);
            return 1;
        }
 
        // Add this element to curr_sum
        if (i < n)
          curr_sum = curr_sum + arr[i];
    }
 
    // If we reach here, then no subarray
    printf("No subarray found");
    return 0;
}
 
// Driver program to test above function
int main()
{
    int arr[] = {15, 2, 4, 8, 9, 5, 10, 23};
    int n = sizeof(arr)/sizeof(arr[0]);
    int sum = 23;
    subArraySum(arr, n, sum);
    return 0;
}
Run on IDE

Output:
Sum found between indexes 1 and 4
Time complexity of method 2 looks more than O(n), but if we take a closer look at the program, then we can figure out 
the time complexity is O(n). We can prove it by counting the number of operations performed on every element of arr[] 
in worst case. There are at most 2 operations performed on every element: (a) the element is added to the curr_sum (b) 
the element is subtracted from curr_sum. So the upper bound on number of operations is 2n which is O(n).
'''
