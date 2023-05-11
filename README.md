# Hangman Game (Python)
![enter image description here](https://res.cloudinary.com/dloadb2bx/image/upload/v1683339104/hangman1_o2riy2.png)

## Technologies used
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

This project was created using Docker to studying the basic concepts of Python learned at day 07  in the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)**. 

## Summary
**Day 07**: Learn more about While loops, If/esle statements. 

## What user can do?

**User:** At `hangman_words.py` we have 200 randomly generated English words. When the user starts the game, a draw will be made and a word will be selected. From this, the user must try to guess which letters are in that word. If you make a mistake six times, the game will end with defeat, if you manage to fill in all the empty spaces, the user will win.

## How to run this project
This project was created with Docker, the Dockerfile is:

    FROM  python:3
    
    WORKDIR  /app
    
    COPY  .  .
    
    CMD  ["python",  "app/main.py"]

To run just download this project and run the follow commands:  `docker build -t hangman-game .`  then run `docker run -it hangman-game`. )
