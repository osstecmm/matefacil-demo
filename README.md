# MateFacil Demo

Demonstration version of **MateFacil** - A web app to evaluate skills and knowledge.

**MateFacil** is a web app to help both professors and students to learn and evaluate the skills and knowledge gained from the semester's course.
In this particular case, we decided to create a web app that can create or 'generate' mathematical problems.
On this first version (MateFacil 0.1) we focus on arithmethical and inequality problems.

This demo shows a partial approach about how the solution was implemented for the version `0.1`. 

This repository will be used as a reference for the new developers coming to work for the project next semester and/or upcoming periods.

This project is being hosted at the FOSS (Free and Open Source Software) organization **Tecnológico Mario Molina Open Source** and the main purpose for this is to
invite students to learn and adopt community and colaborational efforts to work on a project.

The main challenge of this version focus on how to execute existing code on a web app.
The existing code refers to the generators and validators of the mathematical problems, some of them are written in C, C++ and Java.

In our glossary we define:
 - **Generator**: A piece of software that generates a _unique_ mathematical problem, say arithmetical, and once that the problem is generated it's shown on a web page that the student will be able to see.
 - **Validator**: Another piece of software that validates the input given by the user, in this case when a student finishes an arithmetical exercise an introduces his solution through the web page.

On this demo you will be able to execute a web app and see how it runs C, C++ and Java code thanks to Python's subprocesses and Django framework.
All of the C, C++ and Java source has the purpose to be used as an example on how to make them work on a web app. 
Have saying that, there's no generator nor validator included for this demo.


## What will you see on this demo?
A simple web app showing the functionality of Python's subprocesses.

Screenshot:

![example](https://imgur.com/sx0SX0p.jpg)


## Steps to reproduce on your local machine

### Requirements 
 -  Python 3.8.3
 -  Django 3.0.7
 -  OpenJDK 14
 -  G++ (GCC) 10.1.0
 
Once you have all the requirements installed:
 -  Download this repository
 -  `cd matefacil`
 -  `python manage.py runserver 0.0.0.0:8000`
 -  Go to your browser at 0.0.0.0:8000
 -  Enjoy!
 
 
 ---
 ### Authoring 
 - [Luis Manuel Chávez Velasco](https://github.com/ManueLord21)
 - [Jesús Castro](https://github.com/jcstr)

Licence: GNU General Public License v3.0
