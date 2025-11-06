# from pathlib import Path
# import sys
# from colorama import Fore, Style, init


# def main():
#     init(autoreset=True)

#     if len(sys.argv) != 2:
#         print("Використання: python Task3.py <шлях/до/директорії>")
#         sys.exit(1)

#     root = Path(sys.argv[1])

#     if not root.exists() or not root.is_dir():
#         print(f"Помилка: не знайдено директорію {root}")
#         sys.exit(2)

#     print(Fore.MAGENTA + root.name + "/" + Style.RESET_ALL)

#     for path in root.rglob("*"):
#         # Пропускаємо приховані файли та папки (починаються з ".")
#         if any(part.startswith(".") for part in path.parts):
#             continue

#         level = len(path.relative_to(root).parts) - 1
#         indent = "    " * level

#         if path.is_dir():
#             print(indent + Fore.BLUE + path.name + "/" + Style.RESET_ALL)
#         else:
#             print(indent + Fore.GREEN + path.name + Style.RESET_ALL)


# if __name__ == "main":
#     main()


from colorama import Fore
import sys
from pathlib import Path


def main():
    directory = Path(sys.argv[1])
    for path in directory.rglob("*"):
        if path.is_dir():
            print(f"{Fore.BLUE}{path.name}{Fore.RESET}")
        if path.is_file():
            print(f"{Fore.GREEN}{path.name}{Fore.RESET}")


if __name__ == "main":
    main(
        "C:\\Users\\Anton\\OneDrive\\Desktop\\Python_Projects\\Pyhon_Neoversity\\goit-pycore-hw-03"
    )

    # if len(sys.argv) > 1:
