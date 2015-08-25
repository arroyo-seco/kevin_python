from os import listdir
from os.path import isfile, join
import shutil
import os

def validate_path_exists(path):
	assert os.path.exists(path), 'Path %s does not exist' % path
	return path

def get_files_in_dir(path):
	return filter(lambda f: isfile(join(path, f)), listdir(path))

def create_dist_dir(path):
	if os.path.exists(path):
		shutil.rmtree(path)
	os.makedirs(path)

def convert_to_html_filename(filename):
	return filename[:-3] + '.html'

def get_abs_path_for_file(relative_path, filename):
	return os.path.abspath(join(relative_path, filename))

def grip(markdown_file_path, html_file_path):
	command = 'grip --gfm --wide --export %s %s' % (markdown_file_path, html_file_path)
	os.system(command)

def grip_file(f, markdown_path, dist_path):
	markdown_file_path = get_abs_path_for_file(markdown_path, f)
	html_file_path = get_abs_path_for_file(dist_path, convert_to_html_filename(f))
	grip(markdown_file_path, html_file_path)
	return html_file_path

def grip_files(files, markdown_path, dist_path):
	return map(lambda f: grip_file(f, markdown_path, dist_path), files)

if __name__ == "__main__":
	markdown_path = validate_path_exists('guide')
	dist_path = 'dist'
	create_dist_dir(dist_path)
	files = get_files_in_dir(markdown_path)
	gripped_files = grip_files(files, markdown_path, dist_path)
	print str(gripped_files)