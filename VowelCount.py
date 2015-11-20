key = ["a", "e", "i", "o", "u"]

a = 0
e = 0
i = 0
o = 0
u = 0

string = input("Please input a string: ")

for j in string:
    
    if j == key[0]:
        a += 1
        
    elif j == key[1]:
        e += 1 
        
    elif j == key[2]:
        i += 1 
        
    elif j == key[3]:
        o += 1
        
    elif j == key[4]:
        u += 1

print("There were", a, "a's,", e, "e's,", i, "i's,", o, "o's, and", u, "u's.")
    
