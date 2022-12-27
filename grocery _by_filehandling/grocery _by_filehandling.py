#system for grocerry shop
import os
import csv

product_dict={
	"list"      : [],
    "price"     : [],
    "quantity"  : [],
	
}
#csv_file=open("product.csv","x")
with open("product.csv" , mode="r")  as csv_file:
	csvfile=csv.DictReader(csv_file)
	#displaying  contents of the csv file 
	for lines in csvfile:
		product_dict["list"].append(lines["list"])
		product_dict["price"].append(lines["price"])
		product_dict["quantity"].append(lines["quantity"])

	
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
			print(product_dict["quantity"])
			print(product_dict["price"])
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
			print(product_dict["quantity"])
			print(product_dict["price"])
			print()
		elif y=='2':
			print(product_dict["list"])
			print(product_dict["quantity"])
			print(product_dict["price"])
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
		
					q= int (product_dict["quantity"][product_dict["list"].index(order)]) - q 
					#print(product_dict["quantity"])
				elif buy =='2':
					outfile = open("pill.txt" , 'w')
					receipt=0
					outfile.write("\n")
					outfile.write("        CACH RECEIPT        \n")
					outfile.write("****************************\n")
					outfile.write("         ITI SHOP           \n")
					outfile.write("****************************\n")
						
					for i in range(len(order_dict["bag"])):
						receipt=receipt +(int( product_dict["price"][product_dict["list"].index(order_dict["bag"][i])] ))*(int(order_dict["quantity"][i]))
						outfile.write("      TOTAL PRICE "+str(receipt)+"\n")
						#outfile.write(receipt)
					'''with open('pill.txt', 'w') as outfile:
						for value in dictionary.values():
							outfile.write('{}\n'.format(value))'''
							
					outfile.write("****************************\n")
					outfile.write("  THANKS YOU FOR SHOPPING   \n")
					outfile.write("****************************\n")
				else :
					break						
		else:
			break
	else :
		break
		
		
		
with open("product.csv", "w", newline = '') as csv_file:
    # pass the csv file to csv.writer function.
    writer = csv.writer(csv_file)
    # pass the dictionary keys to writerow
    # function to frame the columns of the csv file
    writer.writerow(product_dict.keys())
    # make use of writerows function to append
    # the remaining values to the corresponding
    # columns using zip function.
    writer.writerows(zip(*product_dict.values()))