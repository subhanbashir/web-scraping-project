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

I am using 3 main functions in my code.

extract_data : this function access the website and return a scrap data.

counter: this function count the numbers of jobs and return the total numbers of jobs.

extract_data_MP: this function extract all the links of multiple pages.

plot: this function make a graph between differents jobs.

I created the other two files for the local web server. the problem was, i was unable to perform unit tests with my main code becuase the data is constantly change.and the unit tests was always failed. that's why i created a local web server to perform unit tests.
test_web_local.py file is a unit test function file.

#### the points which i have covered in this project

**git**

i am using git to push my code in the github repository.

**UML & DDD**

i made three different diagram which i uploaded in github repository.

**filenames:** 

use case diagram.png (employment agency).

sequence diagram.png (employment agency work ).

sequence diagram 2.png (describe the working of my code).

**unit tests**

I wrote 3 units tests.

First unit test ckeck if the number of jobs is equal to 10.

Second unit test check if the number of jobs is not equal to 10.

Third unit test check the multiple urls.

I also attach screenshots of the output of unittest.

**filename:** 

unit test output.png.

**continuous delivery**
i am using Jenkins for the continuous delivery. I integrated the jenkins with the git-hub repository and create a pipeline for my project.

filename:

jenkins dashboard.png.

pipeline.png.

pipeline history.png.

pipeline console output.png.

**IDE**
i am using visual studio code(VS Code) to write the script in python. my favourite shortcut for VS Code is (Ctrl+F2 Select all occurrences of current word). these screenshots belongs to my overall code output.

**filename:**

output of my code.png (this screenshot shows the final output of my code).

Code.png (this screenshot show the overall code).


**functional programming**
i am using some functional aspects in my script.like function call inside function,function inside function, function as parameter,function return function.

**build management tool**

i am using **maven** to learn how the build managment tool work. i have done two small project but it doesnot related to my main project. this is just like a practice exercise.

**filename**

maven projects.PNG

in the first project i just generate some docs.

maven test console output.PNG

script1.PNG 

in the second project i just create a war file for a simple web app.

**filename**

pom.xml

jenkinfile

script 2 .PNG

build project.PNG


