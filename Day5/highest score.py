# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest=0
# for score in student_scores:
#     if score>highest:
#         highest=score
# print(f"The higest score is {highest}")        

i = int(input())
lis = list(map(int,input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print (max(lis))