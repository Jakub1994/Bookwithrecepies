[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Jakub1994/Bookwithrecepies)


# Recipe ME
My name is Jakub Ostaszewski and as I am student of Code Institute i was required to create my third Milestone Project
, which should contain Python and one of the database noSQL(Mongodb) or mySQL.
I decided to make an online recipes app where Each account holder should be able to Create, Read, Update, and Delete (CRUD) their own recipes.Website would be build by basic Front end Programs (HTML,CSS,Javascript), Python, Mongodb and modules what helps to connect program with database.



## For what group of people is website Recipe ME?
My idea was an site where anyone can write and share recipe with the other user.
Side that would be free to view recipes for anyone with options of create , edit and delete an recipe for loged in users.
They could use that side as the cook notebook also it would be shared to the others what is giving them oportunity to learn and enjoy someones amazing dish.

1. First time Visitors expectations:
- As a Visitor I expect to be able to easily navigate throught the site.
- As a Visitor I expect to be able get information about recipe to create it at home.
- As a Visitor I want to register my account
- As a Visitor I want to access my account
- As a Visitor I want to contact owner if i would have any issue
- As a Visitor I can get interested of the owner work thats why would be
great to see his other projects/works
2. Registered User Goals:
- As a User I want to log in to my profile
- As a User I want to log out from my profile
- As a User I want to be able remove my recipe
- As a User I want to be able to add recipe
- As a User I want to be able to Modify my recipe
- As a User I want to get in touch with the owner if i want to ask about any changes 
in the feature

# Design:
I tried create simple , fresh looking site where i could use materializedcss.
Every page has navbar coloured teal with navigation to the other pages and light green footer where user can find how to contact owner , and find some social media services with his work.
1. Color Scheme:
- background color of the page is white
- elements like cards are light green that's good match with the pictures from the recipe's
- footer links are white
- email link in footer is red with pink hoover.
2.Pages

- Home : Possess cards with recipes. Cards are green with title,
    image and collapse effect while clicked.Collapse text is black with white background.
    On the botton of the page is placed sign who's created that description.
    Since the collapsed recipe is yours ,Edit and Delate buttons should appear on the left side below the text.

- My Profile : Contain whole description of the app , it shows how to use pages
    and manage your knowlage on the app. Here owner would write
    how he is gonna change the page.

- Add Recipe : Allows user to add his own dish idea to the home page.
    Mentioning from the top first is the title and next the process of the creating recipe.It starts from input named "Dish Name", "Image URL", "Short Description", "Ingredients", "Step 1", "Step 2", "Step 3", Vegan or not lever and ends on the Submit button by what u accept the changes in inputs.
- Logout : Button what takes user out of the account.

### Wireframes:
- [Home](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=2%3A2303)
- [Register](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=2%3A2304)
- [Log in](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=4%3A2241)
- [My Profile](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=4%3A2286)
- [Add Recipe](https://www.figma.com/file/T5CSxj5MMuI8EBZor7FClk/Sanity-Sketching-Kit-(Community)?node-id=5%3A6)


# Features
## Existing Features:
- Home : Here are stock all recipes created by registered users.
- Register : Users without account can create it here.
- Log in : Thats the place where u have to give your data from registration to acces your account.
- My Profile : In the first place Login is going to take you here , this is the page with the instruction and navigations for the users.
    It has a mission to help everyone who log in.It is here where owner will inform the users about any changes in the app.
- Add Recipe : Page with the task to add recipe , In order to to give the owner of the recipe the opportunity to describe the food in detail is placed here vegan or not vegan lever and seven inputs. They are arranged in order, invoking from above: Dish name, Image URL, Short description, Ingridiens, Step 1, Step 2, Step 3. 
- Log out : Thats the button responsible for the user's exit from the account.   
- Navbar : Navigation for the whole website.It's a bar where by pressing one of the buttons, you will go to the other page.
- Responsive Navbar for the mobile device.
- Footer : Is located under the every content of the site.It contain the contact options like : Email, phone number, social media.  
## Future Features:
App would be modified and as a creator i will add there new functions.
- Search button
- Update add recipe page. Image URL input its an spot where author have to copy url adress from the other page. I want to change it and create file input where he can update the picture from his private  device gallery.
- Shop page - Users can locate here pictures with links from where the others can buy the kitchen equipment liked by them, There would be an input for discribe why that item is needed for.
- Like button on the recipe . It would show what dish is the most popular on the page.
- Communication Page - people can communicate there if anyone have the problems with any steps in the recipe.

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
- MaterializeCss: Framework based on the Css . I used it for design my project.
- JQuery : Used to simplify DOM manipulation.
## Coding and Storing Platforms:
- Github: Used to store my project and and also throughout the creation process for all the needed changes.
- Gitpod: Platform used for coding and storing repository.
- Visual Studio Code : Windows platform used to modiffy the project on my device.
# Testing
App was tested on the few devices.In the every page were checked buttons , navigation, database response, account response.
### Home 
In this page i checked :
- Collapse effect in the recipes
- Delate button response
- Edit button functionality
- Recipes writed in "Add recipe" side, Get developed as should.
### Register
In this page:
- Username input: maximum and minimum characters, green colour effect under the text while text is passed and is ready to go furder, red if need more corrects. 
- Password input: maximum and minimum characters , text hideed,  green effect under the text when everything is entered correctly, red if need get modified.
- submit button sending filled inputs to mongodb database and create new account.
- under the submition navigation to the login.
### Log in 
Everything that was sent to mongodb by the registration page has been put into empty pools to see if this data creates a new account,
everything on this page has the same properties as on the registration page,
the text under the button for data approval takes us to registration.
### My Profile
After loging in to the site ,it takes us to the "My Profile". On this site has been checked:
- effect provided for the description
- navigation to the pages provided to describe
### Add Recipe
As the last page I decided to test "Add Recipe"
In this part of the app needful was to check :
- 7 text inputs : maximum and minimum characters
- vegan on or off lever
- if submit button send information to the database and then sends it to "Home" as a recipe.
### Logout
Functionality of the button what should exit from our profile account.
### Footer
- Social media links take us to the Github,Linkedin,Facebook
- hover effect on the email link makes him pink when you point on.
- effect mailto on the email
### Navbar
It was really important part of the project to create working navbar, navigation elements what were checked:
- Home
- Register
- Login
- My Profile
- Add Recipe
- Logout
- Recipe ME Logo navigation to home page

## Testing was performed in this order:
1. [Home](http://vegan-recipies-book.herokuapp.com/recipes) : While we open the website , we are getting to redirect to Home,after checking whether the collapse effect and footer effects and links work, after clicking on them, I redirected us to registration by clicking the button in navbar.
"Register"
2. [Register](http://vegan-recipies-book.herokuapp.com/register): Here the most important thing was to check if the account is created after sending the data and the user can connect, despite this link to the log in under submit button, everything worked fine except, after pressing the submit button the page showed error, but the account can log in and it worked as should.
Next i went to login check if connection to account works.
3. [Log in](http://vegan-recipies-book.herokuapp.com/login): To log in I needed an account made in registration, entering it in the free text fields and clicking submit on this page. In this way, I checked whether the account created earlier works.
I was also looking at what would happen after clicking the link below "Click here", what should have happened and it redirected me to the registration page.
4. [My Profile](http://vegan-recipies-book.herokuapp.com/myProfile/ostach20): (To check the rest of content u need to create an account and log in look carefully above )Then, after pressing the log in button, it sent us to "My Profile". Here, after reading the text under 'Hello Username', I clicked on
the inscription Home and the text describing this part of the application appeared to me, I checked the rest as well and they worked, I had to check the navigation on the icon with the name of the page, it worked.After careful consideration I could go to "Add Recipe".
5. [Add Recipe](http://vegan-recipies-book.herokuapp.com/new_recipes): In this part I checked all the free fields by typing a new recipe in them, I also looked at the "vegan" switch on or off. After hitting the "Submit button" it sent data to my mongodb. After that, it was left for me to check if the mongodb data is being sent to the "Home" site.
6. [Home](http://vegan-recipies-book.herokuapp.com/recipes) (functionality of the Edit, Delate Button): After turning on "Home" again, I can see that the data has been redirected to the fields where it should be, to check it carefully I clicked on the added recipe and the rest of the information appeared. There were also two buttons, the first "Edit" and the second "Delate". After opening "Edit" a similar page to "Add Recipe" appeared to me, only with the recipe entered and the "on" lever moved as I did before on "Add Recipe".
after changing it and pressing the done button, the changes were saved. Pressing the "Delate" button removed the entire recipe. So everything was fine.
7. Footer : So I should only check the links and the hover element in the footer. After pressing Github, Linkedin, Facebook, I went to the equivalent link of this name, so it was correct. After pointing the cursor to the email, the color changed to pink, and after clicking, the mailto effect was activated.
After that, you could enter an email to the owner of the website.
8. Navbar : Has been carefully inspected by checking the rest of the pages


# Deployment:
1.[Github]():
To Deploy the project to a hosting platform I had to:
- Open the Github Website.
- Login there.
- Go to your repositories.
- Choose one
- At the top of the Repository - just above & to the right of "Settings"  and left site of the "Star" on the menu, press the "Fork" Button.
- click Create the create a copy of the Original in github
2.[Heroku](http://vegan-recipies-book.herokuapp.com/recipes)
-

Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits
Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X
