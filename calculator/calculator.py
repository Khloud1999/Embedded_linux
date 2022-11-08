#calculator two modes:
# 1-standered   2-programmer

while True:
	print("Selsect mode :\n for standered press 1\n for programmer press 2")
	mode=input("Enter your choice: ")
	if mode == '1':
		print("Select operation.")
		print("1.Add")
		print("2.Subtract")
		print("3.Multiply")
		print("4.Divide")
		print("5.Reminder")
		
		# take input from the user
		choice = input("Enter your choice: ")
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		if choice == '1':
			print(num1, "+", num2, "=", (num1+ num2))
		elif choice == '2':
			print(num1, "-", num2, "=", (num1- num2))

		elif choice == '3':
			print(num1, "*", num2, "=", (num1* num2))

		elif choice == '4':
			print(num1, "/", num2, "=",(num1/ num2))
		elif choice == '5':
			print(num1, "%", num2, "=",(num1% num2))
			
	if mode =='2':
		print("Select operation.")
		print("1.BIN")
		print("2.HEX")
		print("3.OCTAL")
		print("4.XOR")
		print("5.NOT")
		print("6.OR")
		while True:
			# take input from the user
			choice = input("Enter your choice: ")
			num = int(input("Enter the number: "))
			if choice == '1':
				print(num," in binary =", (bin(num)[2:]))
			elif choice == '2':
				print(num ," in hexadicmal =", (hex(num)[2:]))
			elif choice == '3':
				print(num ," in octal =", (oct(num)[2:]))
			elif choice == '4':
				num2 = int(input("Enter second number: "))
				print(num,"^",num2,"=",(num^num2))
			elif choice == '5':
				print(num,"~","=",(~num))
			elif choice == '6':
				num2 = int(input("Enter second number: "))
				print(num,"|",num2,"=",(num|num2))				

	# check if user wants another calculation
	# break the while loop if answer is no
	next_calculation = input("Let's do next calculation? (yes/no): ")
	if next_calculation == "no":
		break
	else:

		print("Invalid Input")