import venv
import sys
import colorama
from pathlib import Path



if len(sys.argv) != 2:
    print("Error: one argument must be passed - directory path")
    sys.exit(1)


path = Path(sys.argv[1])


if path.exists() and path.is_dir():
    venv.create(path / "venv", with_pip=True)
    print(f"The virtual environment was created in {path}/venv")
    for entry in path.rglob("*"):
        print(colorama.Fore.RED + entry.as_posix())
        if entry.is_dir():
            print(colorama.Fore.CYAN + colorama.Style.DIM + "  " + entry.name)
        else:
            print(colorama.Fore.GREEN + colorama.Back.BLACK + colorama.Style.BRIGHT + "  " + entry.name)
else:
    print(colorama.Fore.RED + f"{path} does not exist or is not a directory")
