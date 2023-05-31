'''**********************************************************************'''
'''
* AYTHOR  : Abdelrahman Osam Khaled
* Date    : 10 May , 2023
* Version : V1.0	
'''
'''**********************************************************************'''
print("ITI Bank")
card = input("Welcome sir,please enter your card : ")
Bank_cards = ('1','2','3')
Bank_cardNames = {'1':'Abdelrahman','2':'Osam','3':'Khaled'}
Bank_Password = ['11','22','33']
Bank_accounts = {'1':10000,'2':20000,'3':30000}
if card in Bank_cards:
	print("Hello ",Bank_cardNames[card])
	password = input("Please enter the password : ")
	if password in Bank_Password[Bank_cards.index(card)]:
		print("Correct password...")
		print("1-Cash withdrawl		2-Cash deposit")
		Operation=input("Please select the Operation :")
		if Operation == '1':
			print("your fund account : ",Bank_accounts[card])
			Money_amount =input("Please enter the money : ")
			Money_amount = int(Money_amount)
			if Money_amount <= Bank_accounts[card]:
				Bank_accounts[card]=Bank_accounts[card]-Money_amount
				print("Wait for the money")
				print("Please take your money")
				print("your remainder money account : ",Bank_accounts[card])
				print("Thank you sir")
			else :
				print("Invalid Money")
		elif Operation == '2':
			print("your fund account : ",Bank_accounts[card])
			Money_amount =input("Please enter the money : ")
			Money_amount = int(Money_amount)
			Bank_accounts[card]=Bank_accounts[card]+Money_amount
			print("Waiting")
			print("your money account : ",Bank_accounts[card])
			print("Thank you sir")
		else :
			print("Invalid Choice")
	else:
		print("incorrect password")
else:
	print("Invalid card")
