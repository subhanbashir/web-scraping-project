import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def extract_data(url):
    response = requests.get(url)
    web_data = BeautifulSoup(response.text,'html.parser')
    return web_data

def counter(extract_data,urls):
    count=0
    for i in urls:
        jobs=extract_data(i)
        jobtitles=jobs.find_all('h2',class_='jobTitle jobTitle-color-purple')
        companyname=jobs.find_all('span',class_='companyName')
        for i in range(0,len(jobtitles)):
            print(jobtitles[i].text)
            print(companyname[i].text)
            print('******************')
            count+=1
    return count    

def extract_data_MP(scrap_data,i):
    urls=[i]
    pages=scrap_data.find('ul', class_='pagination-list')
    for a in pages.find_all('a', href=True):
        x=a['href']
        urls.append('https://de.indeed.com'+ x)
    b=counter(extract_data, urls)   
    return b

def plot(list_of_jobs,number_of_jobs):
       fig = plt.figure()
       ax = fig.add_axes([0,0,1,1])
       ax.bar(list_of_jobs,number_of_jobs)
       plt.show()

if __name__ == "__main__":
    list_of_url=['https://de.indeed.com/jobs?q=IT&l=deutschland&ts',
             'https://de.indeed.com/jobs?q=Business%20Intelligence&l=Deutschland',
             'https://de.indeed.com/jobs?q=Data%20Science&l=Deutschland',
             'https://de.indeed.com/jobs?q=marketing&l=deutschland'
            ]
    list_of_jobs=['IT','BI','data science','marketing']
    number_of_jobs=[]
    for i in list_of_url:
        scrap_data=extract_data(i)
        Total_jobs=extract_data_MP(scrap_data,i)
        number_of_jobs.append(Total_jobs)
    plot(list_of_jobs,number_of_jobs)
