import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Todo va genial!")
print(f"Creando entorno virtual...{RESET_ALL}")
subprocess.call(['python', '-m', "venv", ".venv"])
print(f"{MESSAGE_COLOR}Entorno creado!{RESET_ALL}")
print("*"*40)

print(f"Inicializando GIT...{RESET_ALL}")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
print(f"{MESSAGE_COLOR}Repo listo!{RESET_ALL}")
print("*"*40)