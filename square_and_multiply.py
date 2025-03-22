n = 7
a = 6
original_a=a
original_n = n  
power = 1

while n > 0:
    if n & 1:
        power *= a
    a *= a  
    n >>= 1  

print(f"{original_a}^{original_n} = {power}")  
