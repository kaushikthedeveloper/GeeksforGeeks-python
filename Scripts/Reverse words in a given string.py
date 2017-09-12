#http://www.geeksforgeeks.org/reverse-words-in-a-given-string/

def reverse_words(string):
    #store words in list spilt according to space
    list_string = string.split()
    #reverse the list
    list_string = list_string[::-1]
    return ' '.join(list_string)

#main
if __name__=="__main__":
    string = input()
    reversed_words = reverse_words(string)

    print("Reversed words -")
    print(reversed_words)

"""
Input Explanation :
 - String

Input :
This is easy with python

Output :
Reversed words -
python with easy is This

"""

'''
Examples :

Input  : s = "geeks quiz practice code"
Output : s = "code practice quiz geeks"

Input  : s = "getting good at coding needs a lot of practice"
Output : s = "practice of lot a needs coding at good getting"
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
Algorithm:

1) Reverse the individual words, we get the below string.
     "i ekil siht margorp yrev hcum"
2) Reverse the whole string from start to end and you get the desired output.
     "much very program this like i"
#include<stdio.h>
 
/* function prototype for utility function to
  reverse a string from begin to end  */
void reverse(char *begin, char *end);
 
/*Function to reverse words*/
void reverseWords(char *s)
{
  char *word_begin = s;
  char *temp = s; /* temp is for word boundry */
 
  /*STEP 1 of the above algorithm */
  while( *temp )
  {
    temp++;
    if (*temp == '\0')
    {
      reverse(word_begin, temp-1);
    }
    else if(*temp == ' ')
    {
      reverse(word_begin, temp-1);
      word_begin = temp+1;
    }
  } /* End of while */
 
   /*STEP 2 of the above algorithm */
  reverse(s, temp-1);
}
 
/* UTILITY FUNCTIONS */
/*Function to reverse any sequence starting with pointer
  begin and ending with pointer end  */
void reverse(char *begin, char *end)
{
  char temp;
  while (begin < end)
  {
    temp = *begin;
    *begin++ = *end;
    *end-- = temp;
  }
}
 
/* Driver function to test above functions */
int main()
{
  char s[] = "i like this program very much";
  char *temp = s;
  reverseWords(s);
  printf("%s", s);
  getchar();
  return 0;
}
Run on IDE
Output:

much very program this like i
The above code doesn’t handle the cases when the string starts with space. The following version handles this specific case and doesn’t make unnecessary calls to reverse function in the case of multiple space in between. Thanks to rka143 for providing this version.

void reverseWords(char *s)
{
    char *word_begin = NULL;
    char *temp = s; /* temp is for word boundry */
 
    /*STEP 1 of the above algorithm */
    while( *temp )
    {
        /*This condition is to make sure that the string start with
          valid character (not space) only*/
        if (( word_begin == NULL ) && (*temp != ' ') )
        {
            word_begin=temp;
        }
        if(word_begin && ((*(temp+1) == ' ') || (*(temp+1) == '\0')))
        {
            reverse(word_begin, temp);
            word_begin = NULL;
        }
        temp++;
    } /* End of while */
 
    /*STEP 2 of the above algorithm */
    reverse(s, temp-1);
}
Time Complexity: O(n)
'''