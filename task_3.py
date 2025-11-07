from colorama import Fore, init  # import colorama
import sys  # import sys
from pathlib import Path  # import Path class from module pathlib


def show(dir_path, indent=""):  # function definition with parameters
    for path in dir_path.iterdir():  # iterates files and dir from dir_path
        if path.is_dir():  # if element of path is directory
            # change colour of text on blue add / and output only file directory
            print(f"{indent} {Fore.BLUE} {path.name}/ {Fore.RESET}")
            show(path, indent + "    ")  # call recursive function show
        else:  # if element of path is file
            # change colour of text on green and output only file name
            print(f"{indent} {Fore.GREEN} {path.name} {Fore.RESET}")


def main():  # function definition
    init(autoreset=True)  # Need for Windows

    if len(sys.argv) != 2:  # if lenth arguments not 2
        print("Need only one argument PATH")
        sys.exit(1)  # exit with error, other code not executed

    root = Path(sys.argv[1])  # use for create class path from path to directory

    if not root.exists():  # if directory no found
        print(f"Error. Directory {root.name} not found")
        sys.exit(2)  # exit with error, other code not executed

    if not root.is_dir():  # if is not a directory
        print(f"Error. {root.name} is not a directory")
        sys.exit(3)  # exit with error, other code not executed
    show(root)  # call function show with argument root


if __name__ == "__main__":  # Entry point of file
    main()  # call function main
