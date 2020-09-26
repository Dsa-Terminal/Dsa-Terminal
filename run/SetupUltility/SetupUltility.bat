REM Created by HTML Compiler v2.1
REM ©2015 HTML Compiler, David Esperalta
REM More information at www.htmlcompiler.com

@ECHO OFF
CLS

REM Set our project file in PROJECT variable
SET PROJECT="E:\Dsa-Terminal\run\SetupUltility\SetupUltility.hcp"

REM Set HTML Compiler CMD path in COMPILER variable
SET COMPILER="C:\Program Files (x86)\David Esperalta\HtmlCompiler\HtmlCompilerCmd.exe"

REM Call the compiler passing the project file as argument
%COMPILER% %PROJECT%

