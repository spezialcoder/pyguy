import platform,shutil,os
print "\x1b[31mWarning: The installer does not support mac.If you use mac you have to copy pyguy.py manually\x1b[39m"
if platform.system() == "Linux":
	if os.path.isfile("pyguy.py"):
		shutil.copyfile("pyguy.py", "/usr/local/lib/python2.7/dist-packages/pyguy.py")
		print "\x1b[33m[+]Successful installed\x1b[39m"
	else:
		print "\x1b[31m[-]Missing pyguy.py\x1b[39m"
elif platform.system() == "Windows":	
	if os.path.isfile("pyguy.py"):
		shutil.copyfile("pyguy.py", "C:\\Python27\\Lib\pyguy.py")
	else:
		print "\x1b[31m[-]Missing pyguy.py\x1b[39m"
else:
	print "Os not found"
