<h2>Presentation:</h2>

This project purposes to put a privacy filter over Selfspy software.
The module is a web application that was developed using NodeJS and <a href ="http://sailsjs.org/#!/">Sails</a> framework.
There are two major parts:
-	Privacy parameters : which allows users to define configuration settings
-	Previewer: show users the elements that will be deleted.

<h4>Privacy parameters:</h4>
Uses forms to record settings in the database. The forms only use AJAX requests to avoid page reloads. There are four settings points:<br/>
- Applications
- Keyword
- Times: when the user wishes to be registered
- Locations: where it is allowed to register.
For the location part we use Google API to autocomplete the address and avoid errors when retrieving the latitude and longitude coordinates.

<h4>Previewer part:</h4>
There is a slider that groups 15 pictures per colour scale.<br/>
A "smart scroll" that specifies which images will be deleted after filtering.<br/>
The arrows (left, right) used to change the group of images.<br/>
The "Preview" button which apply user’s filters.
Once there was a click on the "Preview" button a result box appears. It specifies for each image details associated with it, if it will be deleted and why (filter that has been applied).
<br/>
All filters have been designed as Python script.

<h2>Running:</h2>
You need to have NodeJS install:<br/>
<code>sudo apt-get install npm</code><br/>
and Sails:<br/>
<code>sudo apt-get install sails</code> <br/>
In the project root install all modules:<br/>
<code>npm install</code><br/>
Sometimes sqlite3 module doesn’t install automatically so install it:<br/>
<code>npm install sqlite3</code><br/>
<br/>
To work you must have a Sqlite database in assets/db folder you can use the script selfspy.sql in root directory.
<br/>
Previewer works with screenshots in assets/images/screens folder.<br/><br/>
Finally to run the application:<br/>
<code> sails lift </code><br/>




