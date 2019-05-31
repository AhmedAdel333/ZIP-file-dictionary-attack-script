import zipfile
import sys


def unzip():
	for passwd in passwords:
		passwd = passwd.rstrip("\n")
		try:
			zfile.extractall(pwd=passwd.encode('ascii'))
			print ("[+] password found: " + passwd)
			break;
		except Exception:
			print ("wrong password: " + passwd)

while True:
	zip_file = input("your file: ")
	Pfile = input("pass file: ")
	zfile = zipfile.ZipFile(zip_file)
	passfile = open(Pfile, "r")
	passwords = passfile.readlines() 
	unzip()

