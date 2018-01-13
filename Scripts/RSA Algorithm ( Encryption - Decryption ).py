# https://www.di-mgt.com.au/rsa_alg.html (primary source)
# https://www.geeksforgeeks.org/rsa-algorithm-cryptography/

def rsa_algo(p: int,q: int, msg: str):
    # n = pq
    n = p * q
    # z = (p-1)(q-1)
    z = (p-1)*(q-1)

    # e -> gcd(e,z)==1      ; 1 < e < z
    # d -> ed = 1(mod z)        ; 1 < d < z
    e = find_e(z)
    d = find_d(e, z)

    # Convert Plain Text -> Cypher Text
    cypher_text = ''
    # C = (P ^ e) % n
    for ch in msg:
        # convert the Character to ascii (ord)
        ch = ord(ch)
        # encrypt the char and add to cypher text
        # convert the calculated value to Characters(chr)
        cypher_text += chr((ch ** e) % n)

    # Convert Plain Text -> Cypher Text
    plain_text = ''
    # P = (C ^ d) % n
    for ch in cypher_text:
        # convert it to ascii
        ch = ord(ch)
        # decrypt the char and add to plain text
        # convert the calculated value to Characters(chr)
        plain_text += chr((ch ** d) % n)

    return cypher_text, plain_text

def find_e(z: int):
    # e -> gcd(e,z)==1      ; 1 < e < z
    e = 2
    while e < z:
        # check if this is the required `e` value
        if gcd(e, z)==1:
            return e
        # else : increment and continue
        e += 1

def find_d(e: int, z: int):
    # d -> ed = 1(mod z)        ; 1 < d < z
    d = 2
    while d < z:
        # check if this is the required `d` value
        if ((d*e) % z)==1:
            return d
        # else : increment and continue
        d += 1

def gcd(x: int, y: int):
    # GCD by Euclidean method
    small,large = (x,y) if x<y else (y,x)

    while small != 0:
        temp = large % small
        large = small
        small = temp

    return large


#main
if __name__ == "__main__":
    p,q = map(int, input().split())
    msg = input()

    cypher_text, plain_text = rsa_algo(p, q, msg)

    print("Encrypted (Cypher text) : ", cypher_text)
    print("Decrypted (Plain text) : ", plain_text)


"""
Input Explanation :
 - 2 prime numbers (p,q)
 - Msg to be encrypted

Input :
53 59
Hello World

Output :
Encrypted (Cypher text) :  ѯ׮੢੢ѬךܩѬ঩੢ষ
Decrypted (Plain text) :  Hello World
"""

'''
Explanation : 
1.  Take two big prime numbers.
    Calculate the values of : 
        # n = pq
        # z = (p-1)(q-1)

2.  Calculate Encryption Key :
        # e -> gcd(e,z)==1      ; 1 < e < z

3.  Calculate Decryption Key :
        # d -> ed = 1(mod z)        ; 1 <d < z

4.  Get the Encrypted/Cypher text(C) and Decrypted/Plain text(P) :
        # C = (P ^ e) % n
        # P = (C ^ d) % n
'''

'''
GeeksforGeeks :

RSA algorithm is asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. 
Public Key and Private Key. As the name describes that the Public Key is given to everyone and Private key is kept 
private.

An example of asymmetric cryptography :

A client (for example browser) sends its public key to the server and requests for some data.
The server encrypts the data using client’s public key and sends the encrypted data.
Client receives this data and decrypts it.
Since this is asymmetric, nobody else except browser can decrypt the data even if a third party has public key of 
browser.

The idea! The idea of RSA is based on the fact that it is difficult to factorize a large integer. The public key 
consists of two numbers where one number is multiplication of two large prime numbers. And private key is also derived 
from the same two prime numbers. So if somebody can factorize the large number, the private key is compromised. 
Therefore encryption strength totally lies on the key size and if we double or triple the key size, the strength of 
encryption increases exponentially. RSA keys can be typically 1024 or 2048 bits long, but experts believe that 1024 bit 
keys could be broken in the near future. But till now it seems to be an infeasible task.

Let us learn the mechanism behind RSA algorithm :

>> Generating Public Key :
Select two prime no's. Suppose P = 53 and Q = 59.
Now First part of the Public key  : n = P*Q = 3127.

 We also need a small exponent say e : 
But e Must be 

An integer.

Not be a factor of n.
 
1 < e < Φ(n) [Φ(n) is discussed below], 
Let us now consider it to be equal to 3.

    
Our Public Key is made of n and e
>> Generating Private Key :

We need to calculate Φ(n) :
Such that Φ(n) = (P-1)(Q-1)     
      so,  Φ(n) = 3016

    
Now calculate Private Key, d : 
d = (k*Φ(n) + 1) / e for some integer k
For k = 2, value of d is 2011.
Now we are ready with our – Public Key ( n = 3127 and e = 3) and Private Key(d = 2011)

Now we will encrypt “HI” :

Convert letters to numbers : H  = 8 and I = 9

    
Thus Encrypted Data c = 89e mod n. 
Thus our Encrypted Data comes out to be 1394


Now we will decrypt 1349 : 
    
Decrypted Data = cd mod n. 
Thus our Encrypted Data comes out to be 89

8 = H and I = 9 i.e. "HI".

'''