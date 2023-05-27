import os
import shutil

def check_line_exists(file_path, line):
	with open(file_path, 'r') as file:
		for l in file:
			if l.strip() == line:
				return True

	return False



def append_to_file(file_path, line):

	with open(file_path, 'a') as file:
		file.write(line)


def create_folder(path):
	if not os.path.exists(path):
		os.makedirs(path)


def delete_folder(path):
	shutil.rmtree(path)
