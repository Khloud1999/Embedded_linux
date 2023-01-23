#!/bin/bash
while :
do
clear
echo "welcome to Phone Book"
echo "1.Add a contact"
echo "2.Search a contact"
echo "3.Delete a contact"
echo "4.View Phone Book"
echo "5.Quit"
read -p "Enter your choice " choice 
clear

case $choice in
	1)echo "Add new contact"
	read -p "Enter Name : " name
	read -p "Enter Number : " number
	read -p "Enter Address : " address
	clear
	echo "New Contact Info : "
	echo "-> Name: $name "
	echo "-> Number: $number"
	echo "-> Address: $address"
	echo " "
	echo "$name : $number : $address" >> database.txt
	echo "Saved Successfully"
	;;

	2)echo "Search Contact"
	read -p "Enter The Name " search_elem
	clear 
	echo "Search Results: "
	grep -i $search_elem database.txt
	;;
	
	3)echo "Delete Contact"
	read -p "Enter name to be deleted :" delete_elem
	sed -i -e "/$delete_elem/d" database.txt
	echo "Deleted Successfully"
	;;
	
	4)echo "PHONE BOOK"
	echo "******************************"
	echo " "
	cat database.txt
	echo " "
	echo "******************************"
	;;
	
	5)break;;
	
	*)echo "INVALED OPTION"
	;;	
esac;

read -p "press 5 to quit or anything else to return to main menu: " exit
if [$exit -eq 5]
then break
fi 

done
