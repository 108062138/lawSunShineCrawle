import requests
import json
from bs4 import BeautifulSoup
import random
import time

delayChoices = [1,2,3,5,8,13,21,34]
def crawSunShine(mode):
    url = "https://sunshine.jrf.org.tw/judges"
    judgeid = []
    if mode == "test":
        pages = 3#change this val to avoid blocking
    else: 
        pages = 199
    criminal = []
    res ={}
    cnt = 0
    for i in range(pages):
        cnt = cnt + 1
        r = requests.get(url)#將此頁面的HTML GET下來
        soup = BeautifulSoup(r.text,"html.parser")
        selid = soup.select("a.card--avatar--judge")
        selnext = soup.select("a.pagination__cell--next")
        for ids in selid:
            judgeid.append(ids["href"].split()[0])
        rem = ""
        for x in selnext:
            rem = x["href"].split()
            print(rem[0])#rem[0] is the next page
        url = "https://sunshine.jrf.org.tw"+ rem[0]
        if cnt % 5 == 0: 
            delay = random.choice(delayChoices)  #隨機選取秒數
            time.sleep(delay)  #延遲

    #print(judgeid)
    for x in judgeid:
        #print("for the judge id: "+x)
        if cnt % 50 ==0:
            time.sleep(30)  #延遲.
        cnt = cnt + 1
        url = "https://sunshine.jrf.org.tw" +x
        print(url)
        r = requests.get(url)#將此頁面的HTML GET下來
        soup = BeautifulSoup(r.text,"html.parser")
        #print(soup.find_all('a')[9].contents[0])
        selcriminal = soup.select("div.card--feature__content a")
        if soup.find_all('a')[9].contents[0].split()[0] != "Google相關新聞":
            res[soup.find_all('a')[7].contents[0]] = int(soup.find_all('a')[9].contents[0].split()[0][:])
        else :
            res[soup.find_all('a')[7].contents[0]] = int(soup.find_all('a')[10].contents[0].split()[0][:])
        criminal.append(selcriminal)
        if cnt % 5 ==0  or cnt % 4 == 0:
            delay = random.choice(delayChoices)  #隨機選取秒數
            time.sleep(delay)  #延遲

    with open('jg.json','w',encoding = 'utf-8') as f:
        f.write(json.dumps(res,indent=4,ensure_ascii=False))

if __name__ == '__main__':
    #mode = "test"
    mode = "impl"
    crawSunShine(mode)