### MULTITHREADED WEB SCRAPER ###

from bs4 import BeautifulSoup
import requests,webbrowser
import threading
import time

#------- Run only if /links doesn't exists or is empty-------------
#   
#   The following code is only to get data from https://animepahe.com/anime
#   the Data taken is stored in '/links' where all the anime title and there
#   animepahe link are present 
#------------------------------------------------------
#
# search = requests.get("https://animepahe.com/anime")
# soup = BeautifulSoup(search.text,'html.parser')
#
# ----------------------------------------------------- 
#   The following snippet is to print the output of     
#   http request of "https://animepahe.com/anime"       
# ----------------------------------------------------  
# output = open('output.html','w')                      
# print(soup.prettify, file = output)                           
# output.close()
#  
# ---------------------------------------------------                                       
#   The following snippet is for storing all the anime titles 
#    and thier lniks in '/links'
# ---------------------------------------------------
# anime_title = []
# anime_link = []
# search_results = soup.select('.col-12.col-md-6')
# for result in search_results:
#   anime_title.append(result.find('a').text)
#   anime_link.append('https://animepahe.com' + result.find('a').get('href'))
# output = open('links','w')
# for title,link in zip(anime_title,anime_link):
#    print(title + ' @#@ ' + link, file = output)
# output.close()
#
##------------End of intialisation of links block-------------------------



# Reading links from '/links'
titles = []
links = []
file_link = open('links','r')
readlines = file_link.readlines()
for line in readlines:
    temp = line.split('@#@')
    titles.append(temp[0].rstrip())
    links.append(temp[1].strip())

# function for scrapping data from a given link
def scraper(link,filename):
    # filename = 'data/data' + str(filename) + '.csv'
    filename = 'data/data.csv'
    search = requests.get(link)
    soup = BeautifulSoup(search.text,'html.parser')
    
    #all the variables
    title_eng = ''
    title_jap = ''
    title_eng_dub = ''
    poster_link = ''
    summary = ''
    no_episodes = ''
    status = ''
    aired_start = ''
    aired_end = ''
    studio = ''
    duration = ''
    tags = ''

    # file1 = open('outputx.html','w')
    # print(soup.prettify,file=file1)
    # file1.close

    temp = soup.select('.title-wrapper')
    for t in temp:
        title_eng = t.find('h1').text
        title_jap = t.find('h2').text
        poster_link = t.find('a').get('href')
    # print(poster_link)

    temp = soup.select('.anime-synopsis')
    for t in temp:
        summary = t.find_all(text=True)
    summary = ''.join(summary)
    
    infos = soup.select('.col-sm-4.anime-info p')
    for info in infos:
        if info.find('strong').text.strip() == "English:":
            title_eng_dub = info.find(text=True,recursive=False).strip()
        if info.find('strong').text.strip() == "Episodes:":
            no_episodes = info.find(text=True,recursive=False).strip()
        if info.find('strong').text.strip() == "Status:":
            status = info.find('a').text.strip()
        if info.find('strong').text.strip() == "Aired:":
            i = info.text.split('\n')
            aired_start = i[2]
            aired_end = i[3].replace('to ','')
        if info.find('strong').text.strip() == "Studio:":
            i = info.text.split('\n')
            i.pop(0)
            i.pop(0)
            i.pop()
            if len(i) == 1:
                studio = i[0]
            else:
                studio = ':'.join(i)
        if info.find('strong').text.strip() == "Duration:":
            duration = info.find(text=True,recursive=False).strip()
    ##############################
    # try:
    #     title_eng_dub = soup.select_one('.col-sm-4.anime-info p:nth-of-type(1)').find(text=True,recursive=False)
    # except:
    #     title_eng_dub = ""
    # try:
    #     no_episodes = soup.select_one('.col-sm-4.anime-info p:nth-of-type(3)').find(text=True,recursive=False).strip()
    # except:
    #     no_episodes = ""
    # try:
    #     status = soup.select_one('.col-sm-4.anime-info p:nth-of-type(4) a').find(text=True)
    # except:
    #     status = ""
    # try:
    #     aired = soup.select('.col-sm-4.anime-info > p:nth-of-type(5)')
    # except:
    #     aired = ""
    # for a in aired:
    #     a = a.text.split('\n')
    #     aired_start = a[2]
    #     try :
    #         aired_end = a[3].split('to ')[1]
    #     except:
    #         aired_end = ''
    # studios = soup.select('.col-sm-4.anime-info p:nth-of-type(7)')
    # for s in studios:
    #     try:
    #         studio = s.text.split('\n')
    #         studio.pop(0)
    #         studio.pop(0)
    #         studio.pop()
    #         if len(studio) == 1:
    #             studio = studio[0]
    #         else:
    #             studio = ';'.join(studio) 
    #     except:
    #         studio = ""
    
    #duration = soup.select_one('.col-sm-4.anime-info p:nth-of-type(8)').find(text=True,recursive=False).strip()
    ############
    # print(title_eng_dub)
    # print(no_episodes)
    # print(status)
    # print(aired_start)
    # print(aired_end)
    # print(studio)
    # print(duration)
    
    tags = []
    temptags = soup.select('.anime-genre a')
    for t in temptags:
        tags.append(t.text)
    tags = ';'.join(tags)
    #making a entry amd adding it

    aired_start = aired_start.replace(',','')
    aired_end = aired_start.replace(',','')
    summary = summary.replace(',',';;')
    title_eng = title_eng.replace(',',';;')
    title_eng_dub = title_eng_dub.replace(',',';;')
    title_jap = title_jap.replace(',',';;')
    studio = studio.replace(',',';;')

    data_line = [title_eng,title_eng_dub,title_jap,poster_link,no_episodes,status,aired_start,aired_end,studio,duration,tags,summary]
    data_line = '" , "'.join(data_line)
    data_line = '"' + data_line + '"' 
    file1 = open(filename,'a')
    print(data_line,file=file1)
    # print(temp,file=file1)
    file1.close()

# print("|" + links[2283] + "|")
# scraper(links[725],0)

# define a function which takes an argument 'y' and 'z'
# iterates through yth to zth links and writes the data in '/output<y>.csv'

number_of_anime = 0

def func(y,z):
    global number_of_anime
    for link in links[y:z] :
        scraper(link,y)
        number_of_anime = number_of_anime + 1
        
#func(10,15)

thread1 = threading.Thread(target=func,args=(0,180))
thread2 = threading.Thread(target=func,args=(180,360))
thread3 = threading.Thread(target=func,args=(360,540))
thread4 = threading.Thread(target=func,args=(540,720))
thread5 = threading.Thread(target=func,args=(720,900))
thread6 = threading.Thread(target=func,args=(900,1080))
thread7 = threading.Thread(target=func,args=(1080,1260))
thread8 = threading.Thread(target=func,args=(1260,1440))
thread9 = threading.Thread(target=func,args=(1440,1620))
thread10 = threading.Thread(target=func,args=(1620,1800))
thread11 = threading.Thread(target=func,args=(1800,1980))
thread12 = threading.Thread(target=func,args=(1980,2160))
thread13 = threading.Thread(target=func,args=(2160,2340))
thread14 = threading.Thread(target=func,args=(2340,2520))
thread15 = threading.Thread(target=func,args=(2520,2700))
thread16 = threading.Thread(target=func,args=(2700,2880))
thread17 = threading.Thread(target=func,args=(2880,3060))
thread18 = threading.Thread(target=func,args=(3060,3240))
thread19 = threading.Thread(target=func,args=(3240,3600))
thread20 = threading.Thread(target=func,args=(3600,3689))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()
thread17.start()
thread18.start()
thread19.start()
thread20.start()


while number_of_anime < 3690 :
    print("status : " + str(number_of_anime) + "/3690")
    time.sleep(1)

print("Completed YO!")
