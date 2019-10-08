import sys
def main():
	print ("PROGRAM PEMBAGIAN BILANGAN")
	try:
		a = float(input("Masukkan a :"))
		b = float(input("Masukkan b :"))
		hasil= a/b
	except ZeroDivisionError:
		print("\nERROR : Nilai B tidak boleh nol")
	except ValueError:
		print("\n dan B berupa angka")
	except KeyboardInterrupt:
		print("\nError : Jangan tekan ctrl+C !")
	else:
		print("\na: ",a)
		print("\nb: ",b)
		print(" a / b =",hasil)

if __name__=="__main__":
	main()