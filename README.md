# Ultimate Animal guesser 9000
23/08/2019 - 19:47
The original plan, is to use TensorFlow for python, and make a deep learning Animal Guesser
You give the "Animal Guesser 9000" a picture, and it tries to guess what animal is on it
I shall most likely feed tensorflow the color codes and the position of colors compared to each other, and see how will it work.
For color recognition I will use Pillow (Python Imaging Library)
Update 19:57: It appears that most animal databases are online.
  Update 20:03 - Im making the database with like a 1000 pictures myself.
  
p.s 
Also noticed a problem with the colorcode idea, if for normal animals it will work just fine, for cat's and dogs of different breeds it doesn't. Oh well.

20:18
AHAHAHAHHA, Problem solved, I shall make the user feed their animal pictures to my Neural Net, thus I don't need a giant database.
  p.s - Jahu declined the idea.

20:27
I din't find any datasets for animals, but found a giant dog breed database. My animal guesser is now a dog guesser.

10:06 25/08/2019
I spent so much time making the working prototype incase my grand plan fails, I don't have time to make the neuralnet

I guess im showing the prototype

The web version is temporarily available at http://dkarpov.com:5000/
And to run the code on your computer
1. Install python 3
2. Install python-pip linux - sudo apt install python-pip, on windows python -m pip install --upgrade pip
3-Linux. run pip install Pillow
pip install colorama
3-Windows. run pip install Pillow
pip install colorama
4. cd yourself into the directory "tf-Animal-Guess-Master" and run - python main.py
