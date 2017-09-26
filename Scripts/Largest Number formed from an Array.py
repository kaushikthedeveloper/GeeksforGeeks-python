#http://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

def calc_largest_num(numbers: list):
    #sort the numbers in descending order (not considering their length)
    #custom compare function applied to the sorting proces
    sorted_nums = sorted(numbers,key=cmp_to_key(mycmp),reverse=True)
    return ''.join(sorted_nums)


#Sorting magic happens here
#compare adjacent numbers combined and then swapped. Whichever is higher, is retained
def mycmp(x,y):
    if int(x+y)>int(y+x):
        return 1
    elif int(x+y)==int(y+x):
        return 0
    else:
        return -1

#a recepie class for translating return value to key for 'cmp' function
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

#main
if __name__=="__main__":
    numbers=input().split()
    largest_num = calc_largest_num(numbers)

    print("Largest number possible")
    print(largest_num)

"""
Input Explanation :
 - List of numbers

Input :
3 30 34 5 9

Output :
Largest number possible
9534330

"""

'''
Given an array of numbers, arrange them in a way that yields the largest value. For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.

Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
A simple solution that comes to our mind is to sort all numbers in descending order, but simply sorting doesn’t work. For example, 548 is greater than 60, but in output 60 comes before 548. As a second example, 98 is greater than 9, but 9 comes before 98 in output.

So how do we go about it? The idea is to use any comparison based sorting algorithm. In the used sorting algorithm, instead of using the default comparison, write a comparison function myCompare() and use it to sort numbers. Given two numbers X and Y, how should myCompare() decide which number to put first – we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y). If XY is larger, then X should come before Y in output, else Y should come before. For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.

Following is the implementation of the above approach. To keep the code simple, numbers are considered as strings, and vector is used instead of normal array.
C++Java
// Given an array of numbers, program to arrange the numbers to form the
// largest number
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
 
// A comparison function which is used by sort() in printLargest()
int myCompare(string X, string Y)
{
    // first append Y at the end of X
    string XY = X.append(Y);
 
    // then append X at the end of Y
    string YX = Y.append(X);
 
    // Now see which of the two formed numbers is greater
    return XY.compare(YX) > 0 ? 1: 0;
}
 
// The main function that prints the arrangement with the largest value.
// The function accepts a vector of strings
void printLargest(vector<string> arr)
{
    // Sort the numbers using library sort funtion. The function uses
    // our comparison function myCompare() to compare two strings.
    // See http://www.cplusplus.com/reference/algorithm/sort/ for details
    sort(arr.begin(), arr.end(), myCompare);
 
    for (int i=0; i < arr.size() ; i++ )
        cout << arr[i];
}
 
// driverr program to test above functions
int main()
{
    vector<string> arr;
 
    //output should be 6054854654
    arr.push_back("54");
    arr.push_back("546");
    arr.push_back("548");
    arr.push_back("60");
    printLargest(arr);
 
    // output should be 777776
    /*arr.push_back("7");
    arr.push_back("776");
    arr.push_back("7");
    arr.push_back("7");*/
 
    //output should be 998764543431
    /*arr.push_back("1");
    arr.push_back("34");
    arr.push_back("3");
    arr.push_back("98");
    arr.push_back("9");
    arr.push_back("76");
    arr.push_back("45");
    arr.push_back("4");
    */
 
   return 0;
}
Run on IDE

Output:
6054854654
'''