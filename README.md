# Hrvatski-Radio-3-MP3-scraping
Automatically archive MP3 radio shows from Hrvatski Radio 3. program

Hrvatski Radio 3 is Croatian national radio, brodcasting quality content (science, culture, art, classical music, almost no commercials). 
They offer download/listening of archived aired shows, but only few last ones. So if you miss it, it is lost forever. 
Being one of the last bastions of media culture (as other media is overflowed with cheap trill movies, 20 minute blocks of commercials, stupid reality shows, only POP or worse music,...), it is shame (or crime against humanity) to loose quality content. You'll find radio dramas, science shows, etc. on HR3 website (https://radio.hrt.hr/treci-program/slusaonica/).

I love listening recorded shows in car so I made this simple script that scrapes HR3 web page for new archived shows of my preference (you could choose any or even modify script for other sites). Other part is bat file (task_download_HR3.bat) which starts this python script and is itself invoked by Task Scheduler (tested in Windos 10, but should be the same in older versions; I think). In images folder are 3 pictures describing Task Scheduler setup. Should be clear enough.

I know this wont be interesting to people who don't speak Croatian, but I'm writing it in English as code could help someone for similar purpose.
