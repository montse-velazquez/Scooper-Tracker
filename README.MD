# TERMINAL APPLICATION 
> R4.- Provide a link to your source control repository
 - [__SlideDeck__](https://www.canva.com/design/DAFVBJHR_Iw/nZ3vANXVVqjDHr45xaH1BQ/view?utm_content=DAFVBJHR_Iw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
 - [__Presentation__](https://youtu.be/ooj_PaZ6TGY)
 - [__GitHub__](https://github.com/montse-velazquez/Scooper-Tracker)

> R5.- Identify any code style guide or styling conventions that the application will adhere to. Reference the chosen style guide appropriately. 
We used for the creation of the terminal app Python 3.9.6 version, where we create a virtual enviroment for pytest, and packages, we used packages and modules like: 
-   import os
-   from datetime import date   
-   from statistics import mean
-   from math import isnan
-   from itertools import filterfalse
-   pytest

Along our code we use a several style of doing functions with logical actions such as using for loops, if statements and also using try/except for handling any type of error that it could be presented mainly by the input of the user. 

We also used a class for saving code of an object which in this case was the data of the flavours, which will print all the data analysis of the flavours, that why the name of the app stands por Scooper Tracker. 

> R6.- Develop a list of features that will be included in the application. It must include:
> - at least THREE features
> - describe each feature

It will be an app where we will register how many scoops and of which flavour the customer had grabbed his ice cream. 

1. One feature will be the fact that it will give us the total amount of each sale, since there will be customers that might choose different number of scoops which have a different price. 

    - We will complete this task by saving the input of the user since the beginning, and the running a function that will give us out bill, based in which conditions get true so it can print a different price on our screens, aside that this amount will be saving too for another feature.

2. The app will collect data about which classic flavour  and special flavour the costumers tend to choose usually 

    -  There will be a feature that be collecting data along the orders are done, so by the end of it, we can access to all this analysis that the app has done with the saved data, tellling us the average number of scoops, which flavour was popular for the day, and which other didn't even make one sell that day, it will also told us how many scoops in total so far when we do this function.


3. We are going to be able to see the sales and tendencies of other days that were registered 

    - There will be already data saved on the program as a mock up of how it will look like, however by the end of the day when sales are done, we will be able to finish the day by registering the day it is, the sum up of the sales have been being saved on time of each order, using packages of the datetime, and setting it all using different functions together one that saves the sales amount and the other that will allow us to finish the day by just setting the dat.

4. The list of flavours will be able to be updated at the beginning of the day

    - There will be a function for updating the flavour an deleting the current ones on an easy way, where the user we will just need to type the new flavour into the specials list flavours. 


**The customers will have the chance to choose between 10 classic flavours and 2 specials, the specials will be changed each week.**

>R7.- Develop an implementation plan which:
>- outlines how each feature will be implemented and a checklist of tasks for each feature
>- prioritise the implementation of different features, or checklist items within a feature
>- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Link for watching the Project Management: [Scooper Tracker](https://trello.com/invite/b/UqcKMLlY/ATTI68beee69974dc96c428f51f3f0174edf24282A60/scooper-tracker)

![Project Management](ProjectManagement.png)

>R8.- Design help documentation which includes a set of instructions which accurately describe how to use and install the application. 

1. User have in mind if you want to clone this repository for further use you will need to things:
    - Git account
    - Python installed 

2. Check that the version of Python is Pyhton3
3. On GitHub select to clone repository
4. Save repository on a directory with the name of your choice
5. Open terminal and go inside of the folder that you just created and use the command for opening it 

         $code . 


 __How to use scoop tracker__

 1. Have in mind which will be you specials flavpurs of today, since it will be the first thing you should add before strating to sell. 
 2. Check you flavours list 
 3. Start selling ice cream!
 4. You can always check any other feature like, flavours sold, but dont use Save to Data Base unless you are 100% percent that you are closing slaes for the day 
 5. Once you have closed your store, you can select the Save to Data Base, set the date and save it
 6. You can also check the statistics of the day, this option is open everytime, however it will make more sense after you have finish the day. aside of being more helpful!
