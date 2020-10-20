@echo off
PATH %path%;chdir\usr\bin
PATH %path%;chdir\var
PATH %path%;chdir
PATH %path%;chdir\var\Lua
python -m pip install rich
python -m pip install tqdm
python Terminal.py
