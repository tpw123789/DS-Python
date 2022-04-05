import math


s = [1, 2, 3, 4, 5, 6]
for i in range (0,math.floor(len(s)/2)): #create a loop variable from 0 to mid ength of the loop
    b = s[len(s)-1-i];  #asssign a temp the value of i th index from the end and swap th e ith, last ith values
    print(b)
    print(s[len(s)-1-i], s[i])
    s[len(s)-1-i] = s[i]
    s[i] = b
    print(s)
print(s)
