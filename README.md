[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Jakub1994/Bookwithrecepies)


# Recipe ME
My name is Jakub Ostaszewski and as I am student of Code Institute i was required to create my third Milestone Project
, which should contain Python and one of the database noSQL(Mongodb) or mySQL.
I decided to make an online recipes app where Each account holder should be able to Create, Read, Update, and Delete (CRUD) their own recipes.Website would be build by basic Front end Programs (HTML,CSS,Javascript), Python, Mongodb and modules what helps to connect program with database.



## 1.For what group of people is website Recipe ME?
My idea was an site where anyone can write and share recipe with the other user.
Side that would be free to view recipes for anyone with options of create , edit and delete an recipe for loged in users.
They could use that side as the cook notebook also it would be shared to the others what is giving them oportunity to learn and enjoy someones amazing dish.

3. First time Visitors expectations:
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

Design:
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

Wireframe:
-

:
Contain features visible for everyone and people loged in.
Include add , delate, edit and view recipe (CRUD) and more.
1.Existing Features
- Home : Here are stock all recipes created by registered users.
- Register : Users without account can create it here.
- Log in : Thats the place where u have to give your data from registration to acces your account.
- My Profile : In the first place Login is going to take you here , this is the page with the instruction and navigations for the users.
    It has a mission to help everyone who log in.It is here where owner will inform the users about any changes in the app.
- Add Recipe : Page with the task to add recipe , In order to to give the owner of the recipe the opportunity to describe the food in detail is placed here vegan or not vegan lever and seven inputs. They are arranged in order, invoking from above: Dish name, Image URL, Short description, Ingridiens, Step 1, Step 2, Step 3. 
- Log out : Thats the button responsible for the user's exit from the account.   

App would be modified and as a creator i will add there now options.

Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

Features Left to Implement
Another feature idea
Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

JQuery
The project uses JQuery to simplify DOM manipulation.
Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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
