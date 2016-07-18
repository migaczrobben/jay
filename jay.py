#!/usr/bin/python
import sys
import subprocess
import shutil
import errno
import os
from datetime import datetime
if len(sys.argv) == 0 or len(sys.argv) == 1:
	sys.exit("jay create\tjay c\n\tCreates the directory \"working\" at current location\njay update title\tjay u title\n\tCreates a new directory \"title\" and copies files from \"working\"\n\tArgument \"title\" is optional\njay revert title\tjay r title\n\tReverts \"working\" to the contents of \"title\"\njay note\tjay n\n\tAllows user to provide a note about the current version")
else:
	directory = subprocess.check_output("pwd").strip()
	if sys.argv[1] == "create" or sys.argv[1] == "c":
		output = subprocess.check_output("ls").strip().split("\n")
		try:
			os.makedirs(directory + "/working")
		except OSError as exc:
			if exc.errno == errno.EEXIST and os.path.isdir(directory + "/working"):
				sys.exit("The directory \"working\" already exists.")
			else:
				sys.exit("Failed to create \"working\"; do you have permission?")
		sys.exit("Directory \"working\" created.")
	elif sys.argv[1] == "update" or sys.argv[1] == "u":
		if os.path.isdir(directory + "/working"):
			title = ""
			if len(sys.argv) == 2:
				print("No title provided; using \"" + str(datetime.now()) + "\" as new title.")
				title = str(datetime.now())
			elif len(sys.argv) == 3:
				title = sys.argv[2]
			elif len(sys.argv) > 3:
				sys.exit("Failed to update; too many arguments.")
			try:
				shutil.copytree(directory + "/working", directory + "/" + title)
			except OSError as exc:
				if exc.errno == errno.EEXIST and os.path.isdir(directory + "/" + title):
					sys.exit("Failed to update; \"" + title + "\" already exists.")
				else:
					sys.exit("Failed to create \"" + title + "\"; do you have permission?")
			sys.exit("Update \"" + title + "\" has been completed; have a nice day!")
		else:
			sys.exit("Failed to update; directory \"working\" not found.")
	elif sys.argv[1] == "note" or sys.argv[1] == "n":
		if len(sys.argv) == 2:
			response = raw_input("Note: ")
			try:
				note = open("./working/note", "w")
				note.write(response)
			except OSError:
				sys.exit("Failed to create note; do you have permission?")
			except IOError:
				sys.exit("Failed to create note; does \"working\" exist?")
		else:
			sys.exit("Failed to create note; too many arguments given.")
		sys.exit("The file \"working/note\" was created or modified successfully.")
	elif sys.argv[1] == "revert" or sys.argv[1] == "r":
		if len(sys.argv) == 3:
			verify = raw_input("Caution! This will destroy the contents of \"working\"; continue? ")
			if verify.lower() == "n" or verify.lower() == "no":
				sys.exit("Failed to revert project; aborted by user.")
			elif verify.lower() == "y" or verify.lower() == "yes":
				if os.path.isdir(directory + "/" + sys.argv[2]):
					print("Reverting project.")
					try:
						shutil.rmtree(directory + "/working")
					except OSError:
						sys.exit("Failed to remove \"working\"; do you have permission?")
					except IOError:
						sys.exit("Failed remove \"working\"; does the directory exist?")
					print("Directory \"working\" removed.\nAttempting to copy \"" + sys.argv[2] + "\" and its contents.")
					try:
						shutil.copytree(directory + "/" + sys.argv[2], directory + "/working")
					except OSError as exc:
						if exc.errno == errno.EEXIST and os.path.isdir(directory + "/" + title):
							sys.exit("Failed to update; \"working\" already exists.")
						else:
							sys.exit("Failed to create \"working\"; do you have permission?")
					sys.exit("Reversion to \"" + sys.argv[2] + "\" has been completed; have a nice day!")
				else:
					sys.exit("Failed to revert project; replacement does not exist.")
			else:
				sys.exit("Failed to revert project; invalid input.")
		elif len(sys.argv) == 2:
			sys.exit("Failed to revert project; too few arguments given.")
		else:
			sys.exit("Failed to revert project; too many arguments given.")
	else:
		sys.exit("Failed to complete task; unrecognized arguments given.")