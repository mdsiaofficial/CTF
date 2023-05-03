""" 
Decrypt my super sick RSA:
c: is the chipher text
n: product of p and q
e: key to Encode Decode
"""
c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537

p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573

"""
 the Euler totient function φ(n) = (p - 1)(q - 1) is used instead of λ(n) for calculating the private exponent d.
"""
t = (p-1) * (q-1)
# e*d = 1 mod t
# => d= e^-1 mod t

d = pow(e, -1, t);

plain = pow(c, d, n)
print(plain)
print(hex(plain))
# print(hex(plain)[2:].decode('ascii')) #this code works in python 2
print(bytearray.fromhex(hex(plain)[2:]).decode('ascii'))