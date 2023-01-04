n = int(input("n = "))
for i in range(n):
	#printing medium part
	if i==n-1:
		print((2*n)* "*",end ="")
		print((i+1)* "*")
	#for printing upper part	
	else:
		print((2*n)* " ",end= "")
		print((i+1)* "*")
#for printing lower part
for j in range(n-1,0,-1):
	print((2*n) *" ", end= "")
	print(j* "*")

import time
import os
	
size =    int(input("Enter the size of star: "))
loading = int(input("Enter no. of loading: "))

k = 0


while loading:
	os.system("cls")
	loading -= 1
	#--------------right---------------------
	for i in range(size):
		if i==size-1:
			print((2*size)* "*",end ="")
			print((i+1)* "*")
		else:
			print((2*size)* " ",end= "")
			print((i+1)* "*")
	for j in range(size-1,0,-1):
		print((2*size) *" ", end= "")
		print(j* "*")
	time.sleep(1)
	#--------------left---------------------
	for i in range(size):
		if i==size-1:
			print((2*size)* "*",end ="")
			print((i+1)* "*")
		else:
			print((size-i-1)* " ",end= "")
			print((i+1)* "*")
	for j in range(size-1,0,-1):
		print((size-j) *" ", end= "")
		print(j* "*")
	time.sleep(1)
	
    #---------------up --------------------
	for i in range(2*size):
		if(i < size):
			print((size-(i+1))*"  ",end=" ")
			print((2*i+1)* "* ")
		else:
		    print((2*size-1)*" ",end="")
		    print("*")
	time.sleep(1)

	#---------------down--------------------	
	for i in range(size):
		print((size-1)*" ",end="")
		print("*")
	for j in range(size):
		print((j)*" ",end="")
		print((2*(size-j)-1)*"*",end="")
		print(j*" ")

	time.sleep(1)