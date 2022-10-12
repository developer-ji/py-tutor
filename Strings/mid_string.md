ma      ni   sh # ager word ki len odd hai to 

1. word =  yuneesh     # mid 'e' nikal na hai output = youesh ana chahiye
# pahle word ki length pata karege
ex- a = len(word)
    mid = a//2
# iske bad condition laga kar pata kare ge ager lengh even number hai to
     if a%2 == 0:
        word[:mid-1] + word[mid+1:] 
# word= jo user number dale ga usme indexing kare ge jitna mid me divede ho kar yega  jaise starting indexing se mid me jo aya use 1 kam or plus kare ge mid+1 mid me jo divide ho kar aya usse indexing start karege 1 plus kare 

for exmple- 
user = input("enter name:-)

def mid_remove(user):
    x = len(user)
    mid = x//2
    if x%2 == 0:
       remove_mid = user[start:mid-1] +user[mid+1:] #index kiya hai 
    else:
       remove_mid = user[start:mid] +user[mid+1:]    
    return remove_mid
print(mid_remove(remove_mid))
