Link to deployed website [Workout Planner](https://workout-tracker-python-project.herokuapp.com/)  
     
# Workout Planner

The workout planner was designed and implemented for the user to setup all kinds of workout routines that they would be doing during their gym session. The main aim of this app is to make it easier for the individual in terms of organising and planning their workout session.

To achieve this, a user is able to add a workout to their database using a ready given muscle category or creating their own manually. They are then able to insert all the required info about their workout such as the name, the number of sets/reps, their PR goal, the date this workout should be done and potentially any specific notes to keep for themselves.

Furthermore, the user will be able to view all the workouts they setup under one page and remove/mark the workout as done as they go a long with their session.


### Developer goals:

-	To make it easier for an individual to organise their workout session in the gym.
-	To aid the user in tracking their workout and potentially progress.
-   To aid the user by having all their workout notes viewed easily on the phone anywhere and during their gym session rather than having to carry a notebook with the workout notes.
-	To help the user achieve their fitness goals.

### User goals and interests:


- 	To make it easier in terms of managing their workout time and session and not having to remember their workout schedule on top of their heads.
-	Being able to look at all their planned workouts and notes which they would keep an eye on for progression purposes.
-	Setting themselves a goal and aiming to achieve this by the end of the session.
-	To make sure they are able to know exactly what workouts needs to be done for what specific days.

### Users who would be interested in this web app (Target clients)


- 	Someone looking to plan their workout day ahead.
-	Someone looking to keep all their workout goals organised and followed.
- 	Somneone looking to not have to struggle in remembering specific notes that they record for specific workouts.


## UX

**This application was developed for the following stories:**


-	As a user type, I want to plan my day at the gym properly and organise my sessoin.
-	As a user type, I want to set myself goals and personal records to try achieve these during my session for progression purposes.
-	As a user type, I want to note down any important comments regarding a specific workout to make sure this is looked at during my session.
-	As a user type, I want to set eachworkout a specific date and record how I am gonna go about actioning it.

This app was designed to be responsive on all available platforms such as desktops, tablets and mobile phones.



**Wireframes**


The user can view the initial wireframes design for this web app by downloading the following [PDF document](https://pdfhost.io/v/C58.OCEDC_Project_wireframespdf.pdf).

## Features



**Navigation around the site:**

The web app consists of three main different web pages: Home page, New workout, Manage categories. 


The navigation bar changes into a toggler when viewed on a smaller sized screen such as mobile phone. 
When the screen size shrinks, the “Menu” button appears which then can be clickable to slide out from the left all the navigation links around the app.


**Home Page:**

This is the main page where the user would be spending most of their time looking at.

This page will display all the workouts which they have setup as their to do list. The user will be able to mark the workout as done once completed. Each workout box will display the workout name and the date this is planned to get done.

When the user clicks on the workout box, a text box slides down which shows the user all the information they registered about that workout without having to navigate to another page.

The user will also be able to edit the workout incase they want to make a change or have done a typo error which they would need to correct.


**New Workout:**

This is the page where the user will be creating their workout based on their criteria which will be displayed on the homepage once confirmed.

In here, the user will pick a muscle from the muscle category which exists in the database to represent the body part they are working on. They will also need to put in the follwoing: 

The workout name which they will be doing.

Workout notes to note down any specific methods or additional info about this particular workout.

The number of sets they are going to do this workout for.

The number of reps they will be doing for each set.

The PR (Personal record) they are looking to achieve for this workout.

The date of when this workout is going to be done.


**Manage Categories:**

In this section the user will be able to view/edit and remove all the muscle categories that are available and stored in the database.

In here I have already created a category for each muscle group that is needed for the user to use.

However, some users are looking for to combine more than once muscle group in a single workout at a time for example chest and triceps.

The user will be able to create a category called "Chest and Triceps" which will be viewable for them to pick when creating a workout once saved as a category. 

This will prevent them from picking two different categories everytime they want to add a workout which involves these 2 muscle groups.

**Features to implement in the future:**

-	Last edited timestamp for when the user edits a workout.
-	Creating a page to move all workouts marked as done rather than having them completely removed from the app. Also the feature to retrieve any removed workouts back and restore them.
-	Workout comparison feature which lets you track a progress of a specific workout then comparing how you progressed through.


## Technologies used 


-	HTML/HTML5 – This was used to implement most of the content on the site.
-	CSS – This was used for the design/look and feel of the site.
-	Git – Used as a repository for version control.
-	Heroku - Used to host the files and the web app itself as well as version control.
-	Gitpod – This is the platform used for developing the web app.
-	Bootstrap – This was used mainly for navigation purposes and to aid in making the web app responsive.
-	material.io - This was used to fetch the icons for the social media platforms in the footer.
-	JavaScript/jQuery – This was used to implement the workout date calendar/button collapsible and the modal.
-	Python/Flask - This was used for the main purpose of the project(the CRUD functionality) and to link to MongoDB and retrieve the data.
-	MongoDB - This was used to store all info about the workouts and categories which then was linked to the web app and updated accordingly through Python.


## Testing

### Generic/Journey testing:

The following have been tested from a user’s perspective to ensure the web app works as expected:

-	Easy to navigate around the web app as the navigation bar/menu is easily visible on the web app.
-	Each page of the web app easily recognisable, easy to navigate around and easy to read/understand.
-	The user can read each workout as the info are displayed clearly and in a simple manner.
-	Shows clear understanding to the user that this is a fitness based web app regarding workout planning.
-	The user can easily add a workout or amend a workout as the instructions are clear and simple.
-	The user can easily update and add a category as the instructions are clear and simple.
-	The user can easily remove both a workout and a category.


### Manual Testing

-	Navigation links:
	Each navigation link has been tested to ensure that it is linked to the correct page. The navigation link has also been tested when viewed on a smaller screen sizes to ensure the functionality is consistent making sure the toggler is activated correctly.
-	Save/add workout/add cateogry buttons:
	All these buttons have been tested to make sure when a workout is added/update or a category is added/update, the workout database gets updated instantly and the new/correct info is displayed.
-	Cancel buttons:
	The cancel buttons on the update workout/category pages has been tested to make sure the user returns to the correct page if they no longer want to make amendments.
-	Edit workout/category buttons/page:
	These buttons have also been testing along with the functionality. The user gets taken to the update workout/category page where they can make amendments.
-	Edit workout page:
	This page has been tested to make sure when the user clicks on edit workout, the info that exist are pre populated and ready for them to make a change.
-	Edit category page:
	This page has been tested to make sure when the user clicks on edit category, the muscle group category pre populates the existing name.
-	Button hover:
	The button with the hover effect have been tested across the web app. The functionality was working correctly and it changes colour when hovered over.
-	Numeric fields:
	Numeric fields such as "Sets" and "Reps" have been tested to make sure the user is unable to insert any characters apart from numbers.

The web app content was checked and tested to make sure that there was no Grammarly error.




### Cross browser/device testing:

**iPad:**

-	Safari: The web app has been tested to make sure all sections are appearing correctly on iPad making sure the media queries are working as expected. This has been tested as landscape as well as portrait.

-	Chrome: The web app has also been tested on the chrome browser making sure it is displayed consistently a long with Safari on the iPad device.


**Desktop:**

-	Chrome: Testing was done to make sure all images/content was displayed clearly on the large desktop screen.

-	Firefox: Testing was also carried on Firefox to make sure everything is consistent with chrome.


**Android phone:**

-	Android internet: Tested mainly to make sure the web app is responsive correctly on small screen sizes. This was tested through landscape and portrait orientation.

-	Chrome: The web app was also tested on chrome mainly for orientation purposes.


### Issues found and resolved:

The main testing was done throughout carrying the project which means that almost all issues were fixed as the implementation carried forward.

The edit/done/remove icons were not being aligned correctly to the right hand side of each collapsible. This was fixed.

The web app title was coming out of the navigation menu when viewed on android due to size issues. This has been fixed.


### Left to resolve:

The modal which provides the user a confirmation message on the manage categories page is removing the wrong category. I will be looking into this further to find a work around and make sure the correct categoryy is removed.



## Deployment

This project was developed using Gitpod as well as MongoDB to create the database, this was then committed to git and heroku then pushed to GitHhub and Heroku as well through the terminal.

To deploy the project on Heroku, I took the following steps:

1.	Logged into Heroku.
2.	On Gitpod through terminal I created the requirements.txt file.
3.	I also created the Procfile through the terminal.
4.	I also used the terminal on Gitpod to commit and push the project to Heroku.
5.	Once the project has been pushed, I added all the necessary Config Vars to make sure the website is deployed and pulling through correctly.
6.	Once all the steps above have been done, the web app should be ready to view online when clicking on the "View app" button within Heroku.

Please note - On submission the The Development Branch and Master Branch of this project are identical.

The submission URL to the Final version of the website is: https://workout-tracker-python-project.herokuapp.com/



## Credits

**Content:**

-	All the content within the website Has been written by me from scratch.


**Media:**

-	All the icons used on the website have been taken from material.io.

**Code:**

-	The look and feel of the website was created from scratch by me however I have used https://materializecss.com/ to assist me in the design and implementation of the front-end design.

## Disclaimer

The content of this website was created for educational purposes only.