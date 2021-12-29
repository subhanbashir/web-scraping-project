import requests
from bs4 import BeautifulSoup

def counter(sub_url):
    try:   
        response = requests.get(sub_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text,'html.parser')
        jobtitles=soup.find_all('h2',class_='jobTitle')
        companyname=soup.find_all('span',class_='companyName')
        count = 0
        for i in range(0,len(jobtitles)):
            count += 1
            print(jobtitles[i].text)
            print(companyname[i].text)
            print('******************')
        return count
    except requests.exceptions.HTTPError as err:
        print("error found:", err)

def multiple_url(main_url):
    urls=[]
    response = requests.get(main_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text,'html.parser')    
    pages=soup.find('ul', class_='pagination-list')
    for a in pages.find_all('a', href=True):
        x=a['href']
        urls.append('https://de.indeed.com'+ x)
    print(urls)
    
if __name__ == "__main__":
    counter('http://localhost/it_indeed_test.html')
    multiple_url('http://localhost/it_indeed_test.html')