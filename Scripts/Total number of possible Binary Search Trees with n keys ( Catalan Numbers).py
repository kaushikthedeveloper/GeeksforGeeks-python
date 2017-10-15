# http://www.geeksforgeeks.org/total-number-of-possible-binary-search-trees-with-n-keys/
# https://www.youtube.com/watch?v=RUB5ZPfKcnY
# Catalan number

def number_of_binary_trees(n: int):
    count = [0 for i in range(n + 1)]
    count[0] = count[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            count[i] += count[j] * count[i - j - 1]

    return count.pop()

# main
if __name__ == "__main__":
    n = int(input())

    result = number_of_binary_trees(n)
    print("Number of Binary Trees possible for", n, "nodes")
    print(result)

"""
Input Explanation :
 - number of nodes

Input :
5

Output :
Number of Binary Trees possible for 5 nodes
42
"""

'''
Total number of possible Binary Search Trees with n different keys = Catalan number Cn = (2n)!/(n+1)!*n!

For n = 0, 1, 2, 3, … values of Catalan numbers are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …. So are numbers of 
Binary Search Trees.

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

Below is code for n’th Catalan number taken from here.

// See http://www.geeksforgeeks.org/program-nth-catalan-number/
// for reference of below code.
 
unsigned long int binomialCoeff(unsigned int n, unsigned int k)
{
    unsigned long int res = 1;
  
    // Since C(n, k) = C(n, n-k)
    if (k > n - k)
        k = n - k;
  
    // Calculate value of [n*(n-1)*---*(n-k+1)] / [k*(k-1)*---*1]
    for (int i = 0; i < k; ++i)
    {
        res *= (n - i);
        res /= (i + 1);
    }
  
    return res;
}
  
// A Binomial coefficient based function to find nth catalan
// number in O(n) time
unsigned long int catalan(unsigned int n)
{
    // Calculate value of 2nCn
    unsigned long int c = binomialCoeff(2*n, n);
  
    // return 2nCn/(n+1)
    return c/(n+1);
}
Run on IDE
Here is a systematic way to enumerate these BSTs. Consider all possible binary search trees with each element at the 
root. If there are n nodes, then for each choice of root node, there are n – 1 non-root nodes and these non-root nodes 
must be partitioned into those that are less than a chosen root and those that are greater than the chosen root.

Let’s say node i is chosen to be the root. Then there are i – 1 nodes smaller than i and n – i nodes bigger than i. For 
each of these two sets of nodes, there is a certain number of possible subtrees.

Let t(n) be the total number of BSTs with n nodes. The total number of BSTs with i at the root is t(i – 1) t(n – i). 
The two terms are multiplied together because the arrangements in the left and right subtrees are independent. That is, 
for each arrangement in the left tree and for each arrangement in the right tree, you get one BST with i at the root.

Summing over i gives the total number of binary search trees with n nodes.



The base case is t(0) = 1 and t(1) = 1, i.e. there is one empty BST and there is one BST with one node.


'''
