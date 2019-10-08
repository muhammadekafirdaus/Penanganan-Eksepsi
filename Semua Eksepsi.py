import sys
def main():
	print ("PROGRAM PEMBAGIAN BILANGAN")
	try:
		a = float(input("Masukkan a :"))
		b = float(input("Masukkan b :"))
		hasil= a/b
	except(ZeroDivisionError,ValueError,KeyboardInterrupt):
	else:
		print("\na: ",a)
		print("\nb: ",b)
		print(" a / b =",hasil)

if __name__=="__main__":
	main()