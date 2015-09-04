from os import listdir
from os.path import isfile, join
import shutil
import os
import subprocess
from tempfile import mkstemp
from shutil import move
from os import remove, close
import tarfile

def validate_path_exists(path):
    assert os.path.exists(path), 'Path %s does not exist' % path
    return path

def get_files_in_dir(path):
    return filter(lambda f: isfile(join(path, f)), listdir(path))

def create_dist_dir(path, html_path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    os.makedirs(html_path)

def convert_to_html_filename(filename):
    return filename[:-3] + '.html'

def get_abs_path_for_file(relative_path, filename):
    return os.path.abspath(join(relative_path, filename))

def grip(markdown_file_path, html_file_path):
    exit_code = subprocess.call(['grip', '--gfm', '--wide', '--export', markdown_file_path, html_file_path])
    assert 0 == exit_code

def grip_file(f, markdown_path, dist_path):
    markdown_file_path = get_abs_path_for_file(markdown_path, f)
    html_file_path = get_abs_path_for_file(dist_path, convert_to_html_filename(f))
    grip(markdown_file_path, html_file_path)
    return html_file_path

def grip_files(files, markdown_path, dist_path):
    return map(lambda f: grip_file(f, markdown_path, dist_path), files)

def replace(file_path, pattern, subst):
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    remove(file_path)
    move(abs_path, file_path)

def replace_markdown_links(files):
    for f in files:
        replace(f, '.md', '.html')

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

if __name__ == "__main__":
    markdown_path = validate_path_exists('guide')
    dist_dir = 'dist'
    dist_html_path = 'dist/html'
    create_dist_dir(dist_dir, dist_html_path)
    files = get_files_in_dir(markdown_path)
    print 'found %s in %s' % (files, markdown_path)
    print 'gripping files'
    gripped_files = grip_files(files, markdown_path, dist_html_path)
    print 'replacing markdown links with html links'
    replace_markdown_links(gripped_files)
    print 'making archive'
    make_tarfile(join(dist_dir, 'python_guide.tar.gz'), dist_html_path)
    print 'complete!'
