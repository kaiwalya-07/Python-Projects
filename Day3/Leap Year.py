# year=int(input("YEAR "))
# if year % 4 == 0:
#     if year % 100 ==0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else: 
#             print("Not a leap year")
#     else:
#         print("Leap Year")
# else:
#     print("Not a Leap Year")                    


# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1, n+1):
#         print(i, end="")
def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first_name} {last_name}! You just delved into python.')
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)