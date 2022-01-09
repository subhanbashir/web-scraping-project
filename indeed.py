import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def extract_data(url):
    count=0
    for i in url:
        response = requests.get(i)
        soup = BeautifulSoup(response.text,'html.parser')
        jobtitles=soup.find_all('h2',class_='jobTitle jobTitle-color-purple')
        companyname=soup.find_all('span',class_='companyName')
        for i in range(0,len(jobtitles)):
            print(jobtitles[i].text)
            print(companyname[i].text)
            print('******************')
            count+=1
    return count 
def Link_ann(extract_data_MP,i):
    print('i am going to extract this link'+i)   
    return extract_data_MP(i)
        
def extract_data_MP(i):
    urls=[i]
    response = requests.get(i)
    soup = BeautifulSoup(response.text,'html.parser')
    pages=soup.find('ul', class_='pagination-list')
    for a in pages.find_all('a', href=True):
        x=a['href']
        urls.append('https://de.indeed.com'+ x)
    b=extract_data(urls)   
    return b

def greet(list_of_jobs,number_of_jobs):
    print('now i am going to create a plot')       
    def plot(list_of_jobs,number_of_jobs):
       fig = plt.figure()
       ax = fig.add_axes([0,0,1,1])
       ax.bar(list_of_jobs,number_of_jobs)
       plt.show()
    return plot(list_of_jobs,number_of_jobs)
        
if __name__ == "__main__":
    list_of_url=['https://de.indeed.com/jobs?q=IT&l=deutschland&ts',
             'https://de.indeed.com/jobs?q=Business%20Intelligence&l=Deutschland',
             'https://de.indeed.com/jobs?q=Data%20Science&l=Deutschland',
             'https://de.indeed.com/jobs?q=marketing&l=deutschland'
            ]
    list_of_jobs=['IT','BI','data science','marketing']
    number_of_jobs=[]
    for i in list_of_url:
        jobs= Link_ann(extract_data_MP,i)
        number_of_jobs.append(jobs)
    greet(list_of_jobs,number_of_jobs)