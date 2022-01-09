# web-scrapping-project
#### short description about my web scraping project
in my software project i am going to extract data from the website and analyze the job market.
website: www.indeed.de
data : job title and company name

#### files and functions in my repository

I have three different types of files in my repository.

indeed.py file is my main code where i extract data from 4 different links then I create a graph between different jobs(IT, BI, data science, marketing) and analyze the job market.

I am using 3 main function in my code.
extract_data : this function returns all the company names and job titles.
extract_data_MP: this function extract all the links for multiple pages.
plot: this function make a graph between differents jobs.

I created the other two files for the local web server. the problem was, i was unable to perform unit tests with my main code becuase the data is constantly change.and the unit tests was always failed. that's why i created a local web server to perform unit tests.
test_web_local.py file is a unit test function file.

#### the points which i have covered in this project
**git**
i am using git to push my code in the github repository.

**UML & DDD**

i made three different diagram which i uploaded in github repository.

**unit tests**
I wrote 3 units tests. first unit test ckeck if the number of jobs is equal to 10.second unit test check if the number of jobs is not equal to 10 and third unit test check the multiple urls.

**continuous delivery**
i am using Jenkins for the continuous delivery. I integrated the jenkins with the git-hub repository and create a pipeline for my project.

**IDE**
i am using visual studio code(VS Code) to write the script in python. my favourite shortcut for VS Code is (Ctrl+F2 Select all occurrences of current word)

**functional programming**
i am using some functional aspects in my script.like function call inside function,function inside function function as parameter,function return function but it doesnot r
directly related to my script and just print some lines to learn a concept of functional programming.