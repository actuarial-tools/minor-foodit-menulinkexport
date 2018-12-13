@echo off
Rem echo The current directory is %CD%
setlocal
cd /d %~dp0

REM To start a program and then close command prompt without waiting for program to exit:
start /d EmployeeExport.exe EMP
REM exit