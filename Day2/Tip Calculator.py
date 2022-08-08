print("welcome to tip calculator")
bill=float(input("What was the total bill? Rs"))
tip=int(input("How much tip eould you like to give 10 12 or 15? "))
ppl=int(input("How many people to split the bill? "))
bwt= tip/100 * bill + bill
print(f"The total bill is{bwt}")
bpp=bwt/ppl
final_bpp=round(bpp,2)  #this does not format in proper way
final_bpp="{:.2f}".format(bpp)   #This formats in better way
print(f"Bill per person is Rs.{final_bpp}")
