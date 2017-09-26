# GeeksforGeeks Python
Following project contains [Python3](https://docs.python.org/3/) implementation of the Algorithms and Questions found in GeeksforGeeks.

### Format of the Programs :
```
1. # <link reffering to the respective GeeksforGeeks page>
2. <from module import module | if any>
3. <Data Structures used | if any>
4. <Primary Function : handles the computation> 
   : return the desired result (whenever possible)
5. <Helper functions | if any>
6. # main
7. if __name__=="__main__" :
8. <inside main> 
   : get input from the user 
   : pre-processing of data | if required 
   : call the function 
   : print the result
9. Documentation for the code 
   : Input Explanation 
   : Input <Example>
   : Output <Example>
10. Documentation for the GeeksforGeeks page content
```

**Imp :** In the code, provide [Function Annotations](https://www.python.org/dev/peps/pep-3107/) as per [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/) **for every parameter passed in a function**. Return type specification is optional.

Annotations for *parameters* take the form of optional expressions that follow the parameter name:

```python
def foo(a: expression, b: expression = 5):
    ...

#Ex : 
def foo(l: list, s: str = 'xyz'):
    ...

#In pseudo-grammar, parameters now look like identifier [: expression] [= expression]
```

Annotations for the type of a function's return value take the form of optional expressions that is done like so:

```python
def sum() -> expression:
    ...
    
#Ex :
def sum() -> int:
    ...
    
```


##### **Note** : this is not affiliated with GeeksforGeeks in any way other than for reference purpose.

##### **Also Note** : the code implemetation (and sometimes even algorithm) might be different than the one in GeeksforGeeks. The decision is upon the author and author alone. New Algorithms for the same problem statement may be added in the future.