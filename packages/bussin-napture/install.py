import shutil, os
print("Bussin Napture v1.3.0 installer")
direct = input("Type the path of where you would like to install Bussin Napture: ")
shutil.copytree(os.getcwd(), direct)