@echo off 
cls
title Dsa Terminal
path PATH;usr/bin
:loop
set /p input="%$ "
%input%
goto loop