cmd = input("Please enter a python command to execute (type q to exit): ")
try:
	if (cmd == "q"):
		exec("exit()")
	else:
		exec(cmd)
except Exception as e:
	print("Error:", e)

while 1:
	cmd = input("command: ")
	try:
		if (cmd == "q"):
			exec("exit()")
		else:
			exec(cmd)
	except Exception as e:
		print("Error:", e)
