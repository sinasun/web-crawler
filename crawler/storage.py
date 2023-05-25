import os
import shutil

def check_line_exists(file_path, line):

	with open(file_path, 'r') as file:
		for line in file:
			if line.strip() == target_line:
				return True

	return False



def append_to_file(file_path, line):

	with open(file_path, 'a') as file:
		file.write(line)


def create_folder(path):
	
	os.makedirs(path)


def delete_folder(path):
	shutil.rmtree(path)
