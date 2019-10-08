import sys
def main():
	print ("PROGRAM PEMBAGIAN BILANGAN")
	a = float(input("Masukkan a :"))
	b = float(input("Masukkan b :"))

	try:
		hasil= a/b
	except ZeroDivisionError:
		print("\nERROR : Nilai B tidak boleh nol")
	else:
		print("\na: ",a)
		print("\nb: ",b)
		print(" a / b =",hasil)

if __name__=="__main__":
	main()