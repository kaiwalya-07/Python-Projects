import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gaame_img=[rock,paper,scissors]

u_choice=int(input("What is your choice 0 for rock,1 for paper,2 for scissors \n"))
if  u_choice >=3 or u_choice < 0 :
    print("You entered vinvalid number You lose")
else:
    print(gaame_img[u_choice])
    ai_choice=random.randint(0,2)
    print("Computer chose\n")
    print(gaame_img[ai_choice])


    if u_choice==0 and ai_choice==2:
        print("You win !!")
    elif u_choice==2 and ai_choice==0:
        print("You Lose :(")   
    elif ai_choice>u_choice:
        print("You Lose :(") 
    elif u_choice>ai_choice:
        print("You Win !!")      
    elif ai_choice==u_choice:
        print("It is a draw") 