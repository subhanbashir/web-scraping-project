# web-scrapping-project
###### short description about my web scraping project
in my software project i am going to extract data from the website and analyze the job market.
website: www.indeed.de
data : job title and company name

###### files and functions in my repository

I have three different types of files in my repository.

indeed.py file is my main code where i extract data from 4 different links then I create a graph between different jobs(IT, BI, data science, marketing) and analyze the job market.

I am using 3 main function in my code.
extract_data : this function returns all the company names and job titles.
extract_data_MP: this function extract all the links for multiple pages.
plot: this function make a graph between differents jobs.

I created the other two files for the local web server. the problem was, i was unable to perform unit tests with my main code becuase the data is constantly change.and the unit tests was always failed. that's why i created a local web server to perform unit tests.
test_web_local.py file is a unit test function file.

