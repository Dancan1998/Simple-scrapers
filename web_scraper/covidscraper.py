from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
countries = ['kenya', 'china']
for country in countries:
    req = Request('https://www.worldometers.info/coronavirus/country/{}/'.format(country), headers=header)
    html = urlopen(req)
    bs = BeautifulSoup(html, 'html.parser')
    countryName = bs.find("div", {"class":"content-inner"}).h1.text.upper()
    # print(countryName)
    totalNumberofCases = bs.find("div", {"id":"maincounter-wrap"}).h1.text.upper()
    # print(totalNumberofCases)
    cases = bs.find("div", {"class":"maincounter-number"}).span.text
    # print(cases)
    newCases = bs.find("li", {"class":"news_li"}).strong.text.split()[0]
    # print(newCases)
    newDeath = list(bs.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
    # print(newDeath)
    newsDate = bs.find("div", {"class":"news_date"}).h4.text
    notifier = ToastNotifier()
    message = " {}. Total Number of corona cases is {}. New Cases reported are {} people and {} deaths as of {}"\
        .format(countryName, cases, newCases, newDeath, newsDate)
    while True:
        notifier.show_toast("COVID-19 Update", message, duration = 10, icon_path="C:\\Users\Dancan Chibole\\Desktop\\webScraper\\virus.ico")
        time.sleep(120)
    # print(message)