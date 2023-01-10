a=int(input("Fresh loaves: "))
b=int(input("Day old loaves:"))
c=185
d=60
e=c*d/100
f=a*c
g=b*e
print("regular price:", c)
print("total amount of fresh loaves:", f)
print("Total amount of old loaves:", g)
print("Total amount:", f+g)
