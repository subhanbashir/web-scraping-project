# web-scrapping-project
#### short description about my web scraping project
in my software project i am going to extract data from the website and analyze the job market.

website: www.indeed.de

data : job title and company name

#### files and functions in my repository

I have three different types of files in my repository.

**filename**

indeed_new.py

test_web_local.py

web_scr_local.py

indeed.py file is my main code where i extract data from 4 different links then I create a graph between different jobs(IT, BI, data science, marketing) and analyze the job market.

I am using four main functions in my code.

extract_data : this function access the website and return a scrap data.

counter: this function count the numbers of jobs and return the total numbers of jobs.

extract_data_MP: this function extract all the links of multiple pages.

plot: this function make a graph between differents jobs.

I created the other two files for the local web server. the problem was, i was unable to perform unit tests with my main code becuase the data is constantly change.and the unit tests was always failed. that's why i created a local web server to perform unit tests.
test_web_local.py file is a unit test function file.

#### the points which i have covered in this project

**1 : git**

i am using git to push my code in the github repository.

**2: UML**

i made three different diagram which i uploaded in github repository.

this diagram describe the overall working of my code.

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/sequence%20diagram%202.PNG)

employment agency

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/sequence%20diagram.PNG)

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/use%20case%20diagram.PNG)

**3 : DDD**

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/DDD1.PNG)

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/DDD2.PNG)

**7 : unit tests**

I wrote 3 units tests.

First unit test ckeck if the number of jobs is equal to 10.

Second unit test check if the number of jobs is not equal to 10.

Third unit test check the multiple urls.

[mkdnlink]: https://github.com/subhanbashir/web-scraping-project/blob/main/test_web_local.py

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/unit%20test%20output.PNG)

**8 : continuous delivery**

i am using Jenkins for the continuous delivery. I integrated the jenkins with the git-hub repository and create a pipeline for my project.

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/jenkins%20dashboard.PNG)

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/pipeline.PNG)

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/pipeline%20history.PNG)

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/pipeline%20console%20output.PNG)

**9 : IDE**

i am using visual studio code(VS Code) to write the script in python. my favourite shortcut for VS Code is (Ctrl+F2 Select all occurrences of current word). these screenshots belongs to my overall code output.

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/output%20of%20my%20code.PNG)

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/Code.PNG)

**11 : functional programming**
i am using some functional aspects in my script.like function call inside function,function inside function, function as parameter,function return function.

**6 : build management tool**

i am using **maven** to learn how the build managment tool work. i have done two small project but it doesnot related to my main project. this is just like a practice exercise.

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/maven%20projects.PNG)

in the first project i just generate some docs.

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/maven%20test%20console%20output.PNG)

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/script1.PNG)

in the second project i just create a war file for a simple web app.

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/script%202%20.PNG)

![This is an image](https://github.com/subhanbashir/web-scraping-project/blob/main/build%20project.PNG)


