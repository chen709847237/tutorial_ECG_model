@echo off
set work_dir=%1
set xml_dir=%2
set csv_dir=%3

cd /d %work_dir%
setlocal enableextensions enabledelayedexpansion
set /a file_count=0
for /f %%f in ('dir /b %xml_dir%') do (
	ECGTool %xml_dir%%%f CSV %csv_dir%%%~nf.csv
	set /a file_count+=1
	echo PROCESSING FILE !file_count! ...)
endlocal

cd ..
echo Processing Over !
pause