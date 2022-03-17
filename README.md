# Hello There

My intent for this project is to demonstrate my Git/GitHub and Python knowledge. The Python portion of my project is geared toward data analysis.

## My Project 
This project is a very simple python script that allows the user to look at the top 10 Fantasy Football scorers and their position from years 1970-2019. It is worth noting that the script does not perform or output anything complex. However, the experience I gained by coding this project was invaluable. I tried my best to code well and be "Pythonic". However, keep in mind this is my very first Python Script! :blush:

1. Running the program will do the following:
    1. The user will select a year for which the user wants to see the top 10 Fantasy Scorers and their position for a given year. 
    2. The user can select any year from 1970-2019.
    3. The program will display a bar chart displaying the top 10 scorers names and position for the given year.
    4. Finally the program will create and save a JPG filed titled with the selected year.

I chose this project to show my skills because I have a great interest and passion for Fantasy Football. I sourced my data from [FantasyDataPros](https://www.fantasyfootballdatapros.com/csv_files).

### My Project Features
Below is information on how to run the program followed by the features I selected to meet my project requirements:

#### Steps to Run My Program:

1. Clone my repository 
2. Navigate the directory where your virtual environment will be created
    1. Create your virtual environment
    2. Install the required packages using my generated requriments.txt file
3. Run main.py from your command prompt:
    1. The user will get a welcome message.
    2. The user will be asked to select a year they would like to see data for. The year must be from 1970-2019.
        1. The user will be prompted to re-enter their choice, if any data input by the user is not in the required year range.
        2. The user will also be given the chance to quit by typing the word `end`.
    3. The program will display a plotted bar chart for the user to view.
        1. The bar chart will display the top 10 Fantasy Players
        2. The user must close the plot for the program to finish execution.
    4. Once the program finishes, the user will then be able to navigate to the jpg_output directory to find a .jpg version of the previous plot. The .jpg has a naming convention that will include the year the user chose as the input.
    5. It is worth noting that I have a Jupyter notebook in my repository too. It will out put a similar result to main.py
        1. I used the notebook for trial and error. I left nearly everything I did in the notebook. 
            1. Most code in the notebook has a commented line above for my future refernce explaining what the code did.
                1. Some of the code I didn't use but I felt like could be useful in the future, and so the code block was commented out.
            2. The notebook had some code that was executed in the notebook but was not pertinent to execution of the main program. However, was vital to was to learning some of the features of python, pandas, pyplot etc.  
    6. One final note, I uploaded all my data .csv files to the repository. I know this is not best practice, but it made the most sense to enable users to test this particular Python program.


Thats it! Now on to how I met my project requirements below.

#### Category 1- Create a list,populate it with several values, retrieve at least one value and use it in the program
To meet the requirement I created and modified a couple of lists. The player names in my data are first and last names. So using the plot tool for visualization, the full names became too long to use. I created a data frame by reading in the .csv file. I sorted the data frame by values large to small in the "Fantasy Points" column. I then created a list by concatenating two columns in the data frame into a list variable names player_name_list. The two columns were "Player" + "Position". This created one list populated with players names followed by their position. I then iterated over this list and created a new modified list. The new modified list now contained first initial, last name, and position rather than full name and position. I believe this fulfills the requirement of "creating a list, populating it with several values, retrieving data values from the list, and then using it in my program.

Also, I partially completed a 2nd item in this category. I created a function to get user input for desired year, and then called the function in the program. I stored the value returned in a variable called desired_year. I used that variable to assist in what .csv file to select and also to assist in naming the output of the .jpg file at the end of the program.

#### Category 2-Read Data From an External File
I sourced my data set from FantasyDataPros as noted above. The data set had a .csv file containing yearly fantasy football data for seasons in 1970 through 2019. I used the Pandas libary to read in data from a .csv file, which again, contained yearly Fantasy Football statics from the 1970-2019 seasons. I allowed the user to select which .csv file they wanted to read in by receiving input from the user.

In the future I intend to better learn how to use APIs, so that I can source my current data set. An example would be using ESPN.com's API for fantasy football data. Additionally there is much more analysis that can be done with this data, which in time, I would like to explore further.

#### Category 3- Data Display
For this requirment I used the matplotlib library to create a simple bar chart of the top 10 fantasy scorers for the season that the user selected. While my plot is simple I learned a create deal about using pyplot. I was able to learn how to select which data used on the X and Y axises of a bar chart. I learned how to manipulate label text, label sizing, rotation orientation etc.

The program also created and saved a .jpg version of the plot mentioned above. The .jpg file has the year selected as part of the file naming convention.

#### Category 4- Best Practices
For this requirement I created a vitrual environment to complete my project. I used the Python PIP Freeze command to periodically list my document library dependencies via a requirements.txt file, which is in my repository for this project. This use of the requirments.txt file is outlined in the `Steps to Run my Program` section above.

#### Git / GitHub

I continued my utilization of Git and furthered my knowledge on the subject during project. I learned Git terminal command using GitBash. I learned and utilized teriminal commands noted below in the list below. I made commits anytime I made changes and pushed those commits to my GitHub repository. Check out my commit history on this project [Here](https://github.com/dust39/FFL_project_2022/commits/main). Below are the Git commands I learned and used most often.git a

- Git init : to initialize my local repository.
- Git status: to check the status of any file changes in my local repository.
- Git add: to add my changed files to a staging area.
- Git commit: to commit my changed files.
- Git push: to push my local commits up to my GitHub respository.

## Conclusion
Is there ever a conclusion in technology??? I learned so much working on this project. It may seem simple on the surface, but the amount the I have learned is incredible. I loved the challenge and I look forward to continuing my coding adventure. Thank You to Code Kentucky for this opportunity and Thank You for looking at my project!
