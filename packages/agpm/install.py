print("AGPM v0.1.0 wspm installer")
import platform
if platform.system() == "Linux":
    print("Linux detected")
    print("What is your shell? (bash, fish, zsh): ")
    shell = input()
    if shell == "bash":
        with open("~/.bashrc", "a") as f:
            f.write("alias agpm='python3 ~/.wspm/packages/agpm/main.py' \n")
    elif shell == "fish":
        with open("~/.config/fish/config.fish", "a") as f:
            f.write("alias agpm='python3 ~/.wspm/packages/agpm/main.py' \n")
    elif shell == "zsh":
        with open("~/.zshrc", "a") as f:
            f.write("alias agpm='python3 ~/.wspm/packages/agpm/main.py' \n")
    else:
        print("Invalid shell, add an alias manually")
elif platform.system() == "Darwin":
    print("Mac detected")
    print("Assuming zsh")
    with open("~/.zshrc", "a") as f:
        f.write("alias agpm='python3 ~/.wspm/packages/agpm/main.py' \n")
else:
    print("yeah nothing to do lol")