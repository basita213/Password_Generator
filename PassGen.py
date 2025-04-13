import random as ran

Ts=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","+","-","*","/","%","=","!","<",">","&","|","^","~",":",",",".",";","(",")","[","]","{","}","'",'"',"\\"]
T=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letter_num=input("How many letters needed (number) :")
while not letter_num.isdigit() : 
 letter_num=input("How many letters needed (number) :")

sp_or_no=input("with special letters (y,n) :")
while sp_or_no != "y" and sp_or_no !="n" : 
 sp_or_no=input("with special letters (y,n) :")

for _ in range(int(letter_num)):
 if sp_or_no == "n":
  print(ran.choice(T),end="")
 if sp_or_no == "y":
  print(ran.choice(Ts),end="") 
print()