@echo off
rem this batch file runs java -jar ..\lib\mdb.jar
rem but first extracts from ..\etc\mplab_ide.conf the location where java exists
rem in the current MPLAB X installation
set here=%~dsp0
SET mplabx_dir=%here%..\
SET netbeans_dir=%mplabx_dir%
SET development_netbeans_dir=%mplabx_dir%\mplabide-nb-platform\nbbuild\netbeans
IF EXIST %development_netbeans_dir% SET netbeans_dir=%development_netbeans_dir%
SET mdb_jar=%mplabx_dir%\lib\mdb.jar
set exe_dir=%~dp0
for %%I in ("%exe_dir%\..") do set "parent=%%~fI"
set MPLABX_THIRDPARTY_LIB_PATH=%parent%\thirdparty\
rem extract jdkhome from mplab_ide.conf without assuming command extensions (for /F)
rem and without using echo | set /p=set since that fails in some machines.
findstr /B jdkhome "%mplabx_dir%\etc\mplab_ide.conf" > %TMP%\jdk.txt
set /p xxx=<%TMP%\jdk.txt
echo set %xxx%\bin\java.exe > %TMP%\setjdkhome.bat
call %TMP%\setjdkhome.bat
rem at this point jdkhome="c:\XXXXXXX\"java\bin
rem jdkhome has a trailing \ followed by a "
rem if we call java from jre7, it gets confused by the \"
rem so we need to remove the quotes
set jdkhome=%jdkhome:"=%
rem finally, call java on the jar (remove the final space added by the last set
"%jdkhome:exe =exe%" -Dfile.encoding=UTF-8 -jar "%mdb_jar%" %*
