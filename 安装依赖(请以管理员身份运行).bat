@echo off
set choice=
:a
cls
set /p opt=��װ�����⣨Beautifulsoup��Flask����[y/n]
if "%opt%"=="y" goto do
if "%opt%"=="n" echo �Ѻ��� & goto next
echo ��������
pause>nul
goto a
:do

pip install -r requirements.txt

:next
pause>nul