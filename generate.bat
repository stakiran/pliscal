@echo off
setlocal ENABLEDELAYEDEXPANSION

set n=3
set baseyear=2017

set /a n="%n%-1"
for /L %%i in (0,1,%n%) do (
	set /a curyear="%baseyear%+%%i"
	echo year=!curyear!...
	python %~dp0pliscal.py -y !curyear!
)

pause
