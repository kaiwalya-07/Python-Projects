total=0
for nos in range(2,101,2):
    total+=nos
print(total)

#ANOTHER WAY OF DOING THIS CAN BE
initial=0
for num in range(1,101):
    if num%2==0:
        initial+=num
print(initial)        
