student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_ht=0
for ht in student_heights:
    total_ht +=ht
print(total_ht)    

nos=0
for st in student_heights:
    nos +=1
print(nos)

avg=round(total_ht/nos)
print(avg)