import os
from dataclasses import dataclass
from pathlib import PurePosixPath
import re


INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

cd_re = re.compile(r"^\$\s+cd\s+(.+)")
dir_re = re.compile(r"^dir\s+(.+)")
file_re = re.compile(r"^(\d+)\s+(.+)")


@dataclass()
class File:
    path: PurePosixPath
    size: int


@dataclass()
class Folder:
    path: PurePosixPath
    files: dict[str, File]
    sub_folders: list["Folder"]
    size: int


root = Folder(path=PurePosixPath("/"), files=dict(), sub_folders=list(), size=0)
cwd = root.path
folders_by_path: dict[PurePosixPath, Folder] = {root.path: root}


def handle_cd(p: str):
    global cwd
    if p == '..':
        cwd = cwd.parent
    else:
        cwd /= p


def update_sizes(new_file: File):
    global folders_by_path
    path = new_file.path.parent
    while True:
        folders_by_path[path].size += new_file.size
        if path == root.path:
            break
        else:
            path = path.parent


def handle_file(line: str):
    global cwd, folders_by_path
    current_folder = folders_by_path[cwd]

    if file_match := file_re.match(line):
        file_name = file_match.group(2)
        file_size = int(file_match.group(1))
        if file_name not in current_folder.files:
            new_file = File(path=cwd/file_name, size=file_size)
            current_folder.files[file_name] = new_file
            update_sizes(new_file)
    elif dir_match := dir_re.match(line):
        dir_path = cwd / dir_match.group(1)
        if dir_path not in folders_by_path:
            new_folder = Folder(path=dir_path, files=dict(), sub_folders=list(), size=0)
            current_folder.sub_folders.append(new_folder)
            folders_by_path[new_folder.path] = new_folder
    else:
        raise Exception()


for line in input_:
    if cd_match := cd_re.match(line):
        handle_cd(cd_match.group(1))
        continue
    if line[0] != '$':
        handle_file(line)

answer = sum(filter(lambda s: s < 100000, map(lambda f: f.size, folders_by_path.values())))
print(answer)
