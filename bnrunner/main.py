import command, sys

def main():
	if len(sys.argv) == 2:
		command.run_from_path(sys.argv[1])
	else:
		print "Usage :"
		print "bnrunner <python_file>"
