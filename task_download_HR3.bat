ECHO. >> log.txt
ECHO SESSION STARTED (%DATE% - %TIME%) >> log.txt
ECHO Waiting 120 seconds to establish WiFi connection to internet (%DATE% - %TIME%) >> log.txt
timeout 120
ECHO Starting Download script. (%DATE% - %TIME%) >> log.txt
python D:\DOBA_ZNANOSTI\SCRIPT\HR3_scrapper.py
ECHO Waiting 60 seconds and going to sleep... (%DATE% - %TIME%) >> log.txt
timeout 60
ECHO Going to sleep now >> log.txt
ECHO SESSION FINISHED (%DATE% - %TIME%) >> log.txt
ECHO. >> log.txt
Rundll32.exe Powrprof.dll,SetSuspendState Sleep
