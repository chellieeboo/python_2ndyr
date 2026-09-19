 # Name: Rochelle Bayogbog | Status: Present | Not Checked #
a = 4 
b = 8 
 
print("Before swapping:") 
print("a =", a) 
print("b =", b) 
 
# temp is used to temporarily store the product of a and b
temp = a * b 
 
a = temp / a    
b = temp / a    
 
# I add the new values of a and b
sum = a + b 
 
# I use modulus to get the remainder
remainder = b % a 
 
print("\nAfter swapping:") 
print("a =", int(a)) 
print("b =", int(b)) 
 
print("\nAddition:", int(sum)) 
print("Modulus:", int(remainder))
