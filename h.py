name=input("enter the name")
b=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
"q","r","s","t","u","v","w","x","y","z"]
i=0
position=[]
while i<len(name):
    j=0
    while j<len(b):
        if name[i]==b[j]:
            position.append(j)
        j=j+1
    i=i+1
print(position)
