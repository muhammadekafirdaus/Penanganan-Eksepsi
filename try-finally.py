def main()
	try:
		f = open("data.txt" ,"r")
		try :
			f.write("pemrograman Python")
		finally:
			f.close()
	except IOError:
		print("\nError : File tidak dapat" + "dibuka/ditulis")
if __name__=="__main__":
	main()