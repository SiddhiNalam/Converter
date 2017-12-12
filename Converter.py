choice=input("Which Conversion?\n1.Decimal-Binary\n2.Decimal-Octal\n3.Decimal-Hexadecimal\n4.Binary-Decimal\n5.Binary-octal\n6.Binary-Hexadecimal\n7.Octal-Decimal\n8.Octal-Binary\n9.Octal-Hexadecimal\n10.Headecimal-Binary\n11.Headecimal-Octal\n12.Headecimal-Decimal\n")
no=input("Enter no")
if(choice=='1'):
	print(bin(int(no)))
elif(choice=='2'):
	print(oct(int(no)))
elif(choice=='3'):
	print(hex(int(no)))
elif(choice=='4'):
	print(int(no,2))
elif(choice=='5'):
	print(oct(int(no,2)))
elif(choice=='6'):
	print(hex(int(no,2)))
elif(choice=='7'):
	print(int(no,8))
elif(choice=='8'):
	print(bin(int(no,8)))
elif(choice=='9'):
	print(hex(int(no,8)))
elif(choice=='10'):
	print(bin(int(no,16)))
elif(choice=='11'):
	print(oct(int(no,16)))
elif(choice=='7'):
	print(int(no,16))