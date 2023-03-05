# Overview
The repository contains all the lab work for the computer graphics course.
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=andrey1pf)](https://github.com/andrey1pf/Computer-graphics)    
To run the application locally there are three options:  
    * run through the IDE
    * run through the terminal 
    * run through Docker.

# Branches
main: Contains all project source files and Docker files for running the application

# Building
+ IDE. Clone tris repository, you can use <git clone > or click on clone button. Install the IDE you like. For example you can use PyCharm.  
Install all the libraries you need for the application to work. See the requirements.txt file for a complete list.
+ Terminal. Clone tris repository, you can use <git clone > or click on clone button.  
The next step is to enter a command <python app.py > in the project folder.
+ Docker. You have two options:
  * start with docker-compose - You need to execute two commands (in the project folder) <docker build -t color_app:dev . > and  
  then <docker run -p 5000:5000 color_app:dev >.
  * without docker-compose - You need to execute one command (in the project folder) <docker-compose up >.  
After that you can see how the application works by clicking on the link http://127.0.0.1:5000

# Terms of Reference
Изучить цветовые модели: RGB, CMYK, HSV, HLS, XYZ, LAB, переход от одной модели к другой, исследовать цветовой график МКО. Создать 
приложение/веб-приложение, позволяющее пользователю выбирать, а затем интерактивно менять цвет, показывая при этом его составляющие в трех моделях 
одновременно (варианты приведены в таблице ниже).
## На проверку сдаются:
  * exe, который должен работать на ПК преподавателя под Windows/вебприложение, размещенное в общем доступе;
  * исходный код приложения на gitHub;
  * сопроводительная документация.
## Основные требования к приложению
В интерфейсе дать возможность пользователю задавать точные цвета (поля ввода), выбирать цвета из палитры (аналогично графическим редакторам), плавно
изменять цвета (например, ползунки). При изменении любой компоненты цвета все остальные представления этого цвета в двух других цветовых моделях 
пересчитываются автоматически. При «некорректных цветах» (например, при переходе из XYZ в RGB в вашем расчете получился выход за границы изменения 
рассчитываемого параметра) выдавать некое ненавязчивое предупреждение, что происходит обрезаниеокругление и т.п.
## Баллы
  * Корректность перевода из одной модели в другую: 40 баллов.
  * Дружелюбный и удобный интерфейс: 30 баллов.
  * Возможность задания цвета в каждой из трех моделей тремя способами: 20 баллов.
  * Автоматический пересчет цвета во всех моделях при изменении любой из координат: 20 баллов.  
CMYK <--> RGB <--> HLS
