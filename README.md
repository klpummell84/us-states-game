# US States Quiz Game
 US states quiz game written by Kyle Pummell using Python<br />
 background image and US States data file (csv) provided by London App Brewery @ Udemy.com
 
 used pandas module to read csv data to determine correctly guessed states and get the location on the map to print the state name

## Building from source code<br />
In a command prompt, with Python 3.10 installed, type: 

pip install pyinstaller


when it's done, enter the following command in a command prompt pointing to the folder containing the 'main.pyw' file:

pyinstaller --onefile main.pyw

**Windows**:

this will build the following folders and files into the source code root folder:  build/ , dist/ , main.spec

Those two folders and the main.spec are what's needed to run the application. To run, locate the main.exe file inside the dist/ folder and run that file 


**Other OS**:
The file structure may be different on a mac or other OS so you may need to refer to the pyinstaller documentation for further information.

<i>Pyinstaller</i>: https://pyinstaller.org/en/stable/
