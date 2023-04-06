# Overview
The repository contains all the lab work for the computer graphics course.  

The repository contains:
  * Python files for backend
  * HTML, CSS, JS files for frontend
  * Docker to start the project

To run the application locally there are three options:  
  * run through the IDE
  * run through the terminal 
  * run through Docker

# Branches
main: Contains all project source files and Docker files for running the application.

# Building
+ IDE. Clone the repository, you can do this by using command ```git clone``` or downloading the zip archive. Install the IDE you like. For example you can use PyCharm.  
Install all the libraries you need for the application to work. See the requirements.txt file for a complete list.
+ Terminal. Clone the repository, you can do this by using command ```git clone``` or downloading the zip archive.  
The next step is to enter a command ```python app.py``` in the project folder.
+ Docker. Clone the repository, you can do this by using command ```git clone``` or downloading the zip archive. You have two options:
  * start with docker-compose - You need to execute two commands (in the project folder) ```docker build -t color_app:dev .``` and  
  then ```docker run -p 5000:5000 color_app:dev```.
  * without docker-compose - You need to execute one command (in the project folder) ```docker-compose up```.  
After that you can see how the application works by clicking on the link http://127.0.0.1:5000

# Terms of Reference
1. [lab1](https://github.com/andrey1pf/Computer-graphics/blob/main/Conditions/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%201.pdf)
CMYK <--> RGB <--> HLS
2. [lab2](https://github.com/andrey1pf/Computer-graphics/blob/main/Conditions/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%202_12_13%D0%B0%20%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%8B.pdf)
3. [lab3](https://github.com/andrey1pf/Computer-graphics/blob/main/Conditions/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%203_%D0%B3%D1%80%D1%83%D0%BF%D0%BF%D1%8B%2012%2C%2013%D0%B0_final.pdf)
Option 6
