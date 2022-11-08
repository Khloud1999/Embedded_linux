#system for grocerry shop
import os

product_dict={
	"list"      : ["banana", "apple", "Tomatoes","milk"],
    "price"     : [ 25,       15,      9,         23],
    "quantity"  : [ 10,       20,      10,        50],
	
}
order_dict={
	"bag"      : [],
	"quantity" : [],
	"receipt"  : [],
}

while 1:
	print()
	print("**************Welcome to ITI shop**************")
	print()
	print("for owner     press  1")
	print("for customer  press  2")
	print("for exist     press  0")
	mode=input("Enter the number of your choice :")
	print("***********************************************")
	if mode== '1':
		print("To show our product  press 1")
		print("To add new items     press 2")
		print("To change cost       press 3")
		print("To exist             press 0")
		x = input("Enter the number of your choice :")
		print("***********************************************")
		if x=='1':
			print(product_dict["list"])
		elif x=='2':
			n1=input ("add your items : ")
			n2=int(input ("add item's price: "))
			n3=int(input ("add item's quantity: "))
			product_dict["list"].append(n1)
			product_dict["price"].append(n2)
			product_dict["quantity"].append(n3)
			print(product_dict["list"])
			print(product_dict["price"])
			print(product_dict["quantity"])
		elif x=='3':
			print(product_dict["list"])
			p1=input ("which element you want change : ")
			p2=int(input("Enter the new price"))
			product_dict["price"][product_dict["list"].index(p1)]=p2
		else :
			break;
		
	elif mode == '2':
		print("To show our product      press 1")
		print("To buy from our oroduct  press 2")
		print("To exist                 press 0")
		y=input("Enter the number of your choice : ")
		print("***********************************************")
		if y=='1':
			print(product_dict["list"])
			print()
		elif y=='2':
			print(product_dict["list"])
			print(product_dict["quantity"])
			print("***********************************************")
			while 1:
				print("TO Continue buying     press 1")
				print("TO print cash receipt  press 2")
				print("TO exist               press 0")
				buy = input("Enter your choice : ")
				if buy=='1':
					order=input("Enter the element you choice : ")
					order_dict["bag"].append(product_dict["list"][product_dict["list"].index(order)])
					print (order_dict["bag"])
					q=int(input("Enter your quantity of this element: "))
					order_dict["quantity"].append(q)
					product_dict["quantity"][product_dict["list"].index(order)] -= q
					#print(product_dict["quantity"])
				elif buy =='2':
					receipt=0
					print()
					print("        CACH RECEIPT        ")
					print("****************************")
					print("         ITI SHOP           ")
					print("****************************")
					print("ORDER : ",order_dict["bag"])
					for i in range(len(order_dict["bag"])):
						receipt += product_dict["price"][product_dict["list"].index(order_dict["bag"][i])] *order_dict["quantity"][i]
						print("TOTAL PRICE : ",receipt)
					print("****************************")
					print("  THANKS YOU FOR SHOPPING   ")
					print("****************************")
				else :
					break						
		else:
			break
	else :
		break