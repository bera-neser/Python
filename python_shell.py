while True:
	cmd = input("command: ")
	try:
		if (cmd == "q"):
			exec("exit()")
		else:
			exec(cmd)
	except Exception as e:
		print("Error:", e)
