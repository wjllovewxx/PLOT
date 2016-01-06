@echo off
set choice=
:a
cls
set /p opt=安装依赖库（Beautifulsoup、Flask）？[y/n]
if "%opt%"=="y" goto do
if "%opt%"=="n" echo 已忽略 & goto next
echo 输入有误
pause>nul
goto a
:do

pip install -r requirements.txt

:next
pause>nul