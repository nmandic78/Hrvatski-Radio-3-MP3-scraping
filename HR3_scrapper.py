# Import libraries
import requests
import urllib.request
import time
import os.path
import re
import sys
from datetime import datetime
from bs4 import BeautifulSoup

# Helper function to escape telegram markup symbols.
def escape_markdown(text):
    escape_chars = '_'
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)

# Send Telegram message after download. Optional. Needs Telegram acount and API token. If not used, comment out function calls down in source.
def telegram_bot_sendtext(bot_message):     
    
    bot_token = 'XXXXXXX:XXXXXXXXXXXXXXXXXXX'	# here goes the token from Telegram API
    bot_chatID = 'XXXXXXXXX'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    print ('Telegram notification sent.\n')
    with open("log.txt", "a") as myfile:
        myfile.write("Telegram notification sent.\n")

# First find last episode on selected page (section)
def find_last_episode (url):

    # Connect to the URL
    response = requests.get(url,headers=headers)

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    one_a_tag = soup.select_one('.media-heading')
    two_a_tag = one_a_tag.select_one('a')
    link = two_a_tag['href']

    emisija_url = 'https://radio.hrt.hr'+ link

    print ('Emisija URL: ', emisija_url)

    with open("log.txt", "a") as myfile:
        myfile.write("Newest episode link: "+emisija_url+"\n")

    return emisija_url

# Find and download MP3 on episode page (url found by find_last_episode)
def download_episode(url):

    # Connect to the URL
    response = requests.get(url,headers=headers)

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    one_a_tag = soup.select_one('.track-title')
    ep_title = one_a_tag.next

    ep_title = re.sub('[!?<>\/@#$:;.,]', '', ep_title)

    pattern = re.compile(r'mp3: \"(.*?)\"')

    proba = pattern.search(response.text)

    link = proba.group(1)

    download_url = 'https://radio.hrt.hr'+ link
    mp3_file = link[link.rfind("/")+1:]
    mp3_date = datetime.strptime(mp3_file[:8], "%Y%m%d").strftime('%d.%m.%Y')
    file_name = '('+series_name+')'+ep_title+'.mp3'
    file_path = '../'+file_name

    with open("log.txt", "a", encoding="utf-8") as myfile:
        myfile.write("MP3 file: "+file_name+"\n")

    if os.path.isfile(file_path):
        print(file_name+' already downloaded.\n')
        emisijaT_msg = False
        with open("log.txt", "a", encoding="utf-8") as myfile:
            myfile.write(file_name+" already downloaded.\n")
    else:
        urllib.request.urlretrieve(download_url,file_path)
        emisijaT_msg = file_name+' (*'+mp3_date+'*) downloaded successfully! \nDownload: '+escape_markdown(download_url)
        print ('DL URL: '+download_url)
        with open("log.txt", "a", encoding="utf-8") as myfile:
            myfile.write(file_name+' ('+mp3_date+') downloaded successfully! \nDownload link: '+download_url+'\n')
        
    return emisijaT_msg


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
headers = {'User-Agent': user_agent}

with open("log.txt", "a") as myfile:
    myfile.write("********** PYTHON SCRIPT START **********\n")


url, series_name = 'https://radio.hrt.hr/arhiva/doba-znanosti/87/', 'Doba znanosti'

dl_page = find_last_episode(url)            #scrape page and find last episode page URL
msg_complete = download_episode(dl_page)    #scrape mp3 link and download if 
if msg_complete: 
    telegram_bot_sendtext(msg_complete)     #send message via Telegram if new episode downloaded


url, series_name = 'https://radio.hrt.hr/treci-program/arhiva/radio-drama/681/', 'Radio drama'

dl_page = find_last_episode(url)            #scrape page and find last episode page URL
msg_complete = download_episode(dl_page)    #scrape mp3 link and download if 
if msg_complete: 
    telegram_bot_sendtext(msg_complete)     #send message via Telegram if new episode downloaded


url, series_name = 'https://radio.hrt.hr/treci-program/arhiva/radio-igra/679/', 'Radio igra'

dl_page = find_last_episode(url)            #scrape page and find last episode page URL
msg_complete = download_episode(dl_page)    #scrape mp3 link and download if 
if msg_complete: 
    telegram_bot_sendtext(msg_complete)     #send message via Telegram if new episode downloaded


url, series_name = 'https://radio.hrt.hr/arhiva/oko-znanosti/123/', 'Oko znanosti'

dl_page = find_last_episode(url)            #scrape page and find last episode page URL
msg_complete = download_episode(dl_page)    #scrape mp3 link and download if 
if msg_complete: 
    telegram_bot_sendtext(msg_complete)     #send message via Telegram if new episode downloaded


url, series_name = 'https://radio.hrt.hr/treci-program/arhiva/znanstveni-koncentrat/980/', 'Znanstveni koncentrat'

dl_page = find_last_episode(url)            #scrape page and find last episode page URL
msg_complete = download_episode(dl_page)    #scrape mp3 link and download if 
if msg_complete: 
    telegram_bot_sendtext(msg_complete)     #send message via Telegram if new episode downloaded


url, series_name = 'https://radio.hrt.hr/treci-program/arhiva/znanost-i-drustvo/950/', 'Znanost i drustvo'

dl_page = find_last_episode(url)            #scrape page and find last episode page URL
msg_complete = download_episode(dl_page)    #scrape mp3 link and download if 
if msg_complete: 
    telegram_bot_sendtext(msg_complete)     #send message via Telegram if new episode downloaded


with open("log.txt", "a") as myfile:
    myfile.write("********** PYTHON SCRIPT END **********\n")
