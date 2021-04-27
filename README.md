[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Jakub1994/Bookwithrecepies)


# Recipe ME
My name is Jakub Ostaszewski and, as a student at Code Institute, I was required to create a third Milestone Project
using Python and one of the following databases: noSQL(Mongodb) or mySQL.
I decided to make an online recipes app where each account holder should be able to Create, Read, Update, and Delete (CRUD) their own recipes.

The website would be build by basic Front end Programs (HTML,CSS,Javascript), Python, Mongodb and modules what helps to connect program with database.



## Who is Recipe ME intended for?
My idea was a site where anyone can write and share recipes with other people.
I want it to allow anyone to view all recipes but only registered users to be able to create, edit and delete their own recipes.
It should also enable the user(s) to use the site as a cooking notebook that could be shared with others giving them the oportunity to try and learn new dishes they would probably never hear of.

1. First time Visitors expectations:
- As a Visitor, I want the navigation throught the site to be easy.
- As a Visitor, I want to be able to find all the details necessary for me to recreate any dish at home.
- As a Visitor, I want to be able to contact the creator in case of any issues.
- As a Visitor, I want to be able to see who the creator is and what was the idea behind the app.
- 
2. Registered User Goals:
- As a User, I want to create an account for myself.
- As a User, I want to access my account and profile.
- As a User, I want to log out from my account.
- As a User, I want to be able remove any of the recipes I posted.
- As a User, I want to be able to add new recipes.
- As a User, I want to be able to edit my recipes.
- As a User, I want to be able to contact the creator in case of any issues.

# Design:
I tried to create a simple, fresh looking site where I could use Materializedcss.
Every page has a teal colored navigation bar on the very top with the other redirecting bottons to the rest of the sections in order to access them.
There is also a light-green footer, where the user can find the creator's contact, and his social media profiles linked.
1. Color Scheme:
- The backgroung is always white.
- The recipes' names and pictures are enclosed in a light-green rectangular-shaped text box and, when clicked on, the intructions for the respective dish show up.
- The email link in footer is red and it has a pink hoover.
2.Pages:
- Home : 
    This is where the recipes are listed, one under another.
    Every text box is green and contains the dish name written in black (left side) and the dish picture (right side).
    When clicked on, a collapse effect text shows up, written in black, on a white background.
    On the right lower corner of the recipe, there is a "Created by" section, followed by the name of the recipe's author.
    The recipe's author will also have the options to edit or delete that recipe on the left lower corner.
- Register:
    This is where visitors can become registered users.
    To do so, they have to fill in the username and password fields and then press "Register".
- Login:
    Once registered, the user can access their account by typing their username and password in this section.
    After that, the next pages will show on the navigation bar:
    
    - My Profile :
    
        This page tells contains a description of all the app's features in order to make the best of it.
        Also, in case of future uptades of the software, the new funtions will be explained here.
    
    - Add Recipe :
        
        This is where the registered user can add his own recipies, by filling in the next sections:
        "Dish Name": what it actually is.
        "Image URL": a URL from where to take the picture that will appear toghether with the name.
        "Short Description": a couple of word to let other users know what this dish is recommended for.
        "Ingredients": a list of all the required ingredients and the exact quantities.
        "Step 1", "Step 2" and "Step 3": a stept by step precise explanation of what to do.
        At the very end, there is a "Vegan or not" lever that makes it easier for other user to find vegan recipes.
        Lastly, there is a "Submit" button at the very bottom to save all the above details and add the recipe to the home page.
    
    - Logout : As its name suggests, this enables the user to sign off their account.

### Wireframes:
- [Home](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=2%3A2303)
- [Register](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=2%3A2304)
- [Log in](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=4%3A2241)
- [My Profile](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=4%3A2286)
- [Add Recipe](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=5%3A6)


# Features
## Existing Features:
- Navbar : Navigation bar fixed at the very top of the page at all times. It contains the redirecting buttons to all the pages.
- Responsive Navbar for the mobile device.
- Footer : located at the very bottom of every page, it is where the owner contact details are: email, phone number and social media.
- Home : here, is where all the recipes ever posted are.
- Register : the users without an account can create one here.
- Log in : This oage enables the registered user to access his account and choose one of the next ones:
    
    - My Profile: 
        Once logged in, the user will be redirected here, where there is a description of the of what every page is for, so he/she can make the best of the app.
        Also, if an uodate occurs, the new functions will be explained here.
    
    - Add Recipe: 
        This is where the registered users can add new recipes. They are required to input the name of the dish, a URL with its picture, a short description, a list         of ingredients and a step by step guide. The user must also select whether it is a vegan dish or not.
        
    - Log out: this button enables the user to exit their account.
  
## Update improvements:
There are several features that could be built on:
- A search button that permits the user to find a specific recipe in shorter time.
- Allow the "Add recipe" page to admit pictures uploaded from the user's device, too.
- A Shop section where the users can find the links to the kitchen tools recomended by the recipes's authors and buy them online.
- A "Like" button under every recipe to show which ones are more popular, as well as a comments section for users to communicate with the recipe's author if needed.

# Technologies Used
## Programs
- HTML
- CSS
- Javascript
- Mongodb
- Python:
1. Flask 
2. Flask_pymongo
3. Werkzeug.security
4. Bson.objectid
## Framework Libraries
- MaterializeCss is a framework based on Css. I used it to design the project.
- JQuery, used to simplify DOM manipulation.
## Coding and Storing Platforms:
- Github: used to store my project and throughout the creation process for all the needed modifications.
- Gitpod: a platform used to code and store the repository.
- Visual Studio Code : Windows platform used to modiffy the project on my device.
# Testing
The app was tested on several different devices. All buttons, the navigation, the database and account responsiveness where tested in each and every page.
Tested in every page:
### Home
- The collapse effect for every recipe.
- The delete button responsiveness.
- The edit button functionality.
- If the recipes written in the "Add recipe" sections were added to the home page correctly.
### Register
- Username input: whether the maximum and minimum number of characters is implemented and the bar under the input turns green when the input is correct or red when the input is incorrect.
- Password input: whether the maximum and minimum number of characters is implemented, the text is hidden, and the bar under the input turns green when the input is correct or red when the input is incorrect.
- Whether the "Register" button sends the user's input to the mongodb database and creates a new account.
- Whether the navigation button under the "Register" one takes to the "Login" page. 
1### Log in 
Everything sent to MONGODB in the "Register" page has been put into empty pools to see if this data creates a new account.
- Username input: whether the maximum and minimum number of characters is implemented and the bar under the input turns green when the input is correct or red when the input is incorrect.
- Password input: whether the maximum and minimum number of characters is implemented, the text is hidden, and the bar under the input turns green when the input is correct or red when the input is incorrect.
- Whether the "Login" button sends the user's to their account's "My Profile" page.
- Whether the navigation button under the "Login" one takes to the "Register" page. 
### My Profile
- Whether the user is redirected to the "My Profile" page right after logging in.
- Whether the description of every page (Home, My Profile, Log out) appears after clicking on its name.
- The navigation to the every page when clicking on their respective buttons.
### Add Recipe

- Whether the respective number of maximum and minimum characters in respected in all the user's inputs.
- Whether the vegan on or off lever works.
- Whether the  "Submit" button stores all inputs in the database and then sends it to the "Home" page as a recipe.
### Logout
Whether it exits the user's account or not.
### Footer
- Social media links lead to the Github, Linkedin and Facebook profiles of the owner.
- The hoover effect of the email link: whether it becomes pink when clicked on.
- The email's mailto effect.
### Navbar
A really important part of the project was to create working navbar, the tested navigation buttons are:
- Home
- Register
- Login:
    - My Profile
    - Add Recipe
    - Logout
- Recipe ME Logo navigation to the home page

## Testing was performed in this order:
1. [Home](http://vegan-recipies-book.herokuapp.com/recipes): 
    While we open the website , we are getting to redirect to Home,after checking whether the collapse effect and footer effects and links work, after clicking on       them, I redirected us to registration by clicking the button in navbar.
    "Register"
2. [Register](http://vegan-recipies-book.herokuapp.com/register): 
    Here the most important thing was to check if the account is created after sending the data and the user can connect, despite this link to the log in under         submit button, everything worked fine except, after pressing the submit button the page showed error, but the account can log in and it worked as should.
    Next i went to login check if connection to account works.
3. [Log in](http://vegan-recipies-book.herokuapp.com/login): 
    To log in I needed an account made in registration, entering it in the free text fields and clicking submit on this page. In this way, I checked whether the         account created earlier works.
    I was also looking at what would happen after clicking the link below "Click here", what should have happened and it redirected me to the registration page.
4. [My Profile](http://vegan-recipies-book.herokuapp.com/myProfile/ostach20): 
    (To check the rest of content u need to create an account and log in look carefully above )Then, after pressing the log in button, it sent us to "My Profile".      Here, after reading the text under 'Hello Username', I clicked on
   the inscription Home and the text describing this part of the application appeared to me, I checked the rest as well and they worked, I had to check the            navigation on the icon with the name of the page, it worked.After careful consideration I could go to "Add Recipe".
5. [Add Recipe](http://vegan-recipies-book.herokuapp.com/new_recipes):
    In this part I checked all the free fields by typing a new recipe in them, I also looked at the "vegan" switch on or off. After hitting the "Submit button" it       sent data to my mongodb. After that, it was left for me to check if the mongodb data is being sent to the "Home" site.
7. [Home](http://vegan-recipies-book.herokuapp.com/recipes):
    (functionality of the Edit, Delete Button): After turning on "Home" again, I can see that the data has been redirected to the fields where it should be, to         check it carefully I clicked on the added recipe and the rest of the information appeared. There were also two buttons, the first "Edit" and the second             "Delate". After opening "Edit" a similar page to "Add Recipe" appeared to me, only with the recipe entered and the "on" lever moved as I did before on "Add         Recipe".
    after changing it and pressing the done button, the changes were saved. Pressing the "Delate" button removed the entire recipe. So everything was fine.
7. Footer : 
So I should only check the links and the hover element in the footer. After pressing Github, Linkedin, Facebook, I went to the equivalent link of this name, so it was correct. After pointing the cursor to the email, the color changed to pink, and after clicking, the mailto effect was activated.
After that, you could enter an email to the owner of the website.
8. Navbar : 
    Has been carefully inspected by checking the rest of the pages


# Deployment:
### Github:
To Deploy the project to a hosting platform (Github) I had to:
- Open the Github Website and login.
- Go to your repositories.
- Choose one.
- At the top of the Repository - just above & to the right of "Settings"  and left site of the "Star" on the menu, press the "Fork" Button.
- click Create a copy of the Original in github

### [Heroku](http://vegan-recipies-book.herokuapp.com/recipes)
 How to deploy on Heroku:
1. First create env file where you will put : 
- Import os
- IP set on 0.0.0.0  or your own
- MONGODB_NAME Name of your MONGODB collection
- MONGO_URL link to your MONGODB cluster - to do this u have to open your mongodb > go to Clusters> under your Cluster name click the button connect, then choose Connect your application. Choose the second option which is add your connection string. Copy your string in the field.
- SECRET_KEY - set it as the most difficult key what u can think about , i used for that page [Randomkeygen](https://randomkeygen.com/)
- PORT set as 5000 or as u want
your env.py should look like :
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "yourkey")
os.environ.setdefault("MONGO_URI", "yourcluster")
os.environ.setdefault("MONGO_DBNAME", "CookingBook")
2.We need a requirments.txt to satisfy heroku you need to create your requirments.txt with pip freeze --local> requirements.txt
2. Create a simple text file named Procfile without the file extension, ie Procfile.txt is not valid
3. Open procfile and tell heroku how to run the website by writing there python3 app.py
4. Open heroku Website,From there you have to create new app and open it
5. Go to settings, There u have to set the Config Vars.Set the:  IP, MONGODB_NAME, MONGO_URL, PORT, SECRET_KEY.
your setting should look like :
- IP : 0.0.0.0
- MONGODB_NAME : Name of your collection in Mongodb
- MONGO_URL : url for your cluster
- PORT : 5000
- SECRET_KEY : your secret key
6. Since u did every step from before you can go to Deploy section in heroku ,scroll down and connect app to the github,click enable automatic deploys.
7. At the bottom of the page, click on Deploy Branch, get sure the master branch is selected


1.IP and PORT - IP address identify a host/computer on a computer network. Port numbers are logical interfaces used by communication protocols
2.MONGODB_NAME - Name of yours mongodb collection
3.MONGO_URL - URL connecting to your MONGODB cluster
4.SECRET_KEY - Its the security key 

# Credits

I am really thankful to the Code Institute student care team, specially the tutors, who helped me throughout this project.
I would like to mention that, without the Python module miniproject, I don't think I could have done this ambitious project on time.
1. Media
The pictures in the recipes were downloaded from the next sites :
- https://www.bbcgoodfood.com/recipes/pumpkin-curry-chickpeas
- https://food52.com/recipes/1068-classic-french-potato-puree-extra-smooth
- https://www.goodhousekeeping.com/food-recipes/healthy/a35231/chimichurri-cauliflower-steaks/

3. Acknowledgements
- I was inspired by Code Institute Mini Project in Python Module.
- I used ready to use Materializedcss components and Javascript functions.
