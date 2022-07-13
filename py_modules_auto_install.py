'''A simple script to install python modules.
If specific module is not necessary, just comment the specift line.
Feel free to add more modules.'''
import subprocess
import sys


def install(pack):
    '''Installation command'''
    subprocess.check_call([sys.executable, "-m", "pip", "install", pack])


packages = [
    'numpy',
    'scipy',
    'pandas',
    'matplotlib',
    'ipython',
    'jupyter',
    'jupyterlab',
    'spyder',
    'sympy',
    'nose',
    'seaborn',
    'pyautogui',
    'Pillow',
    'selenium',
    'schedule',  # agenda tarefas com o python
    'pyodbc',  # conecta python com o banco de dados
    'sqlalchemy',
    'openpyxl',
    'keyboard',
    'autopep8',
    'pylint',
    'pynput'  # monitora os inputs do sistema
]

for package in packages:
    install(package)
