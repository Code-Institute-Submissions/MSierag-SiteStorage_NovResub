<h1 align="center">SiteStorage</h1>

[View the live project here.](https://msierag.github.io/It-sil-heve/)

## Purpose of the website

This is a simple app for inventory management on a construction site. In my previous career I was fortunate enough to work on a few construction sites for a German mulitinational, where I was responsible for site logistics. This company had an integrated system for delivery tracking, but this was only available for the large items sent to site by the logistics department. However, the construction team received daily deliveries of small items which sometimes went missing as they were untracked or the information wasn't shared.  

The purpose of this app is to provide an easy to use platform for a construction team to track any and all small deliveries. It is intented to be made available only to the construction team to facilitate the communication between them. It's intentionally devoid of images and frills to facilitate readability in a construction environment. The website is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential users.

## User Experience (UX)

-   ### User stories

    -   #### Visiting User Goals

        1. As a visiting user, I want to easily understand the main purpose of the site. 
        2. As a visiting user, I want to be able to easily navigate throughout the site.
        3. As a visiting user, I want to know my position in the game.
        4. As a visiting user, I want to compete.
        
-   ### Design
    -   #### Colour Scheme
        -   There are five colours used throughout the site, the first two are the main colours and the remaining three are used for accents.
        ##### Main colours
           ![Coolors rendering of main colour scheme](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/maincolours.png?raw=true)
            
            The colour #009688 was chosen from the MaterializeCSS colour options as it approaches the colour used by the German multinational. The colour #26a69a is a variation on this colour. .
        ##### Accent colours
           ![Coolors rendering of effect colourscheme](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/effectcolours.png?raw=true)
            
            The colours #4caf50, #f4436, and #03a9f4 are accent colours. They are used on buttons throughout the site. 
    -   #### Typography
        -   The font used throughout the site are the standard fonts defined by MaterializeCSS.

*   ### Wireframes

    -   Welcome page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevehome.png?raw=true)

    -   Register page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevegame.png?raw=true)

    -   Login page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilheveendgame.png?raw=true)

    -   Profile page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevescoreboard.png?raw=true)

    -   Items page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevesmartphone.png?raw=true)

    -   Add Item page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevetablet.png?raw=true)

    -   Edit Item page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevetablet.png?raw=true)

    -   Locations page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevetablet.png?raw=true)

    -   Add Location page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevetablet.png?raw=true)

    -   Edit Location page wireframe - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/wireframes/Itsilhevetablet.png?raw=true)

## Features
-   Navbar at the top of the page is not visible on the Welcome page, but on all subsequent pages. The Register and Login pages 
    show no buttons on the navbar yet. Once the user is successfully logged in the navbar displays the buttons "Home", "New item", "Locations" and "Logout". The buttons have a hover effect.
-   Delete functions throughout the site are intentionally without defensive programming. 

### Existing features

#### Page specific features

##### Welcome page

-   Large title welcomes visitor to SiteStorage. 

-   A card the text Please register / login below is displayed underneath the title.

-   Call to action button labelled "Register" which when clicked opens the Register page.

-   Call to action button labelled "Login" which when clicked opens the Login page. 

-   The page is intentionally without a navbar, to ensure only registered users enter the site.  

##### Register page

-   Top of the screen shows the navbar which is empty apart from the logo, no further buttons visible to visitors.

-   Middle section holds a form with fields for Username and Password prefixed by an icon.

-   Below the fields is a call to action button labelled "Register" which when clicked has two options:
        -if the registration was successfull, the user is redirected to the Profile page with a flash message of "You are now registered"
        -if the registration was unsuccessfull, the user receives a flash message "Username already exists" and is redirected to the Registration page.

##### Login page

-   Top of the screen shows the navbar which is empty apart from the logo, no further buttons visible to visitors.

-   Middle section holds a form with fields for Username and Password prefixed by an icon.  

-   Below the fields is a call to action button labelled "Login" which when clicked has two options:
        -if the login was successfull, the user is redirected to the Home page with a flash message of "Welcome (username)" 
        -if the login was unsuccessfull, the user is redirected to the Login page with a flash message of "Username and / or password incorrect".

##### Profile page

-   Top of the screen shows the navbar which now show the buttons "Home", "New item", "Locations" and "Logout".

-   Middle section is formed by a card which displays the message "(username) logged in successfully".  

-   Below this section is a simple statement invites the user to select a task above. 

##### Home page

-   Top of the screen shows the navbar which now show the buttons "Home", "New item", "Locations" and "Logout".

-   Below the navbar the page title of All Items is displayed.

-   Below the title is a search field with two buttons to the right, Reset and Search. This allows the user to search the    items listed below.

-   Middle section holds a collapsible  which displays all items in the database. The collapsed items displays a down caret, two buttons Edit and Used, the item name and the date it was received. When the user selects the down caret, the unfolded item shows the storage location, the item description and who took receipt of it. 
    -   The Used button serves as the delete function. When pushed, the item is deleted from the database and the user receives a flash message of "Item deleted"
    -   The Edit button when pushed redirects the user to the Edit Item page

##### New Item page

-   Top of the screen shows the navbar which now show the buttons "Home", "New item", "Locations" and "Logout".

-   Below the navbar the page title of Add Item is displayed.

-   Middle section holds a form with fields to be completed by the user to add a new item to the database. The first field is a dropdown menu for the storage location, followed by Item Name, Item Description and Date received. The latter is a date picker. 

-   At the bottom of the form is a large button labelled Add item which when pushed has two possible outcomes:
    -if all fields were filled out correctly, the user is redirected to the Home page where the item has been added to the list and a flash message reads "Item added successfully"
    -if all fields were not filled out correctly, the user is alerted to the missing or incorrect information by the validation functionality.

##### Edit Item page

-   Top of the screen shows the navbar which now show the buttons "Home", "New item", "Locations" and "Logout".

-   Below the navbar the page title of Edit Item is displayed.

-   Middle section holds a form with prefilled fields to be edited by the user to edite the item in the database.

-   At the bottom of the form there are two large buttons labelled Cancel and Edit Item 
    -Cancel takes the user back to the Home page 
    -Edit Item will, if all fields were filled out correctly, redirect the user to Home page with a flash message of "Item updated successfully" 
    -Edit Item will, if all fields were not filled out correctly, alert the user to the missing or incorrect information by the validation functionality.

##### Locations page

-   Top of the screen shows the navbar which now show the buttons "Home", "New item", "Locations" and "Logout".

-   Below the navbar the page title of Manage Locations is displayed.

-   Below the title is a large button labelled Add Location which when pushed redirects the user to the Add Location page.

-   Middle section holds a collection of cards which display all locations currently in the database. The cards have two buttons Delete and Edit 
    -   The Delete button deletes the location from the database and the user receives a flash message of "Location deleted successfully"
    -   The Edit button when pushed redirects the user to the Edit Location page

##### Add location page

-   Top of the screen shows the navbar which now show the buttons "Home", "New item", "Locations" and "Logout".

-   Below the navbar the page title of Add Location is displayed.

-   Middle section holds a form with a single field to be completed by the user to add a new location to the database. 

-   At the bottom of the form is a large button labelled Add location which when pushed redirects the user to the Locations page where the new location has been added and a flash message of "New storage location added".

##### Edit location page

-   Top of the screen shows the navbar which now show the buttons "Home", "New item", "Locations" and "Logout".

-   Below the navbar the page title of Edit Location is displayed.

-   Middle section holds a form with a single prefilled field to be completed by the user to edit the current location in the database. 

-   At the bottom of the form there are two large buttons labelled Cancel and Edit Item 
    -Cancel takes the user back to the Locations page 
    -Edit Location will redirect the user to Locations page with a flash message of "Location updated successfully" 

### Future features

-   Currently no future features are envisioned.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://www.python.org/)


### Frameworks, Libraries & Programs Used

1. [MaterializeCSS:](https://materializecss.com/)
    - MaterializeCSS was used to assist with the responsiveness and styling of the website.
1. [jQuery:](https://jquery.com/)
    - jQuery was used for the functionality of the MaterializeCSS components.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [MongoDB:](https://www.mongodb.com/)
    - MongoDB is used for the database. 
1. [Heroku:](https://heroku.com/)
    - Herokuapp is the platform used to display the project after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
1. [Coolors](https://coolors.co/)
    - Coolors was used to generate the palette used throughout the site.

## Testing

### Validation 

The W3C Markup Validator, W3C CSS Validator Services and JSHint were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    - Home - [Result](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/homehtml.png?raw=true)
    - Game - [Result](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/gamehtml.png?raw=true)
    - Endgame - [Result](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/endgamehtml.png?raw=true)
    - Scoreboard - [Result](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/scoreboardhtml.png?raw=true)

    No errors or warnings were given for the HTML code.
    
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

    One error and one warning were given for the CSS code - [Results](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/cssbefore.png?raw=true)
    The error referred to the fact that for the hover effect on the buttons transform: scale(0.3rem) was used. Rem is not allowed as a value for transform. Correcting this to transform: scale(1.3) resolved the error.
    
    The warning referred to the fact that the W3C CSS Validator cannot check linked/imported files in direct input. Style.css has an import link for the Google Font of 'Raleway' and the link to the background image for the home page. This seems to be a minor issue inherent to the way the validator is set up, but as it doesn't impact the function of the site I've decided to leave it as is. - [Results](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/cssafter.png?raw=true)  

-  [JSHint](https://jshint.com/)     
    The linter gave no fatal errors, only warnings. Most of these pertained to the fact that the syntax used is only available in ES6. As the code also doesn't produce any errors in ChromeDevTools I desiced to leave the code as it is. 
    
    Script.js - [Results](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/scriptjs.png?raw=true) 
    
    Endgame.js - [Results](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/endgamejs.png?raw=true)
    
    Scoreboard.js - [Results](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/validation/scoreboardjs.png?raw=true) 

### Google Lighthouse

I used Google Lighthouse to audit the site's performance, accessibility, use of best practices and search engine optimization.

Testing resulted in the following [score](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/lighthouse/lighthouse.png?raw=true):
-   Performance: 98%
-   Accessibility: 100%
-   Best Practices: 100%
-   SEO: 100%

**Performance** - Two suggested improvements involved removing or altering CSS and JavaScript elements which are included in Bootstrap. I decided against tampering with this. 

### Responsiveness testing

To test the responsiveness of the site [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and [Responsive Design Checker](https://responsivedesignchecker.com/) were used. 
Screenshots for the home page and the game page are included. The end game and scoreboard pages with their minimal content followed the same line as the other two pages.

#### Home page
Desktop 1920x1080 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/desktop1920x1080.png?raw=true)

Notebook 1366x768 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/notebook1366x768.png?raw=true)

Tablet 800x1280 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/tablet800x1280.png?raw=true)

Tablet 768x1024 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/tablet768x1024.png?raw=true)

Smartphone 414x736 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/smartphone414x736.png?raw=true)

Smartphone 320x568 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/smartphone320x568.png?raw=true)

#### Game page
Desktop 1920x1080 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/game1920x1080.png?raw=true)

Notebook 1366x768 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/game1366x768.png?raw=true)

Tablet 800x1280 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/game800x1280.png?raw=true)

Tablet 768x104 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/game768x1024.png?raw=true)

Smartphone 414x736 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/game414x736.png?raw=true)

Smartphone 320x568 - [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/responsiveness/game320x568.png?raw=true)

#### Conclusions
Only on the smallest smartphone screen (320x480) did the background image interfere with the text on the buttons.  [Screensizemap](https://screensizemap.com/) was consulted to determine the popularity of this screen size.
The popularity listed for this type of screen hovers around 2% and seems to concern smartphones which can be considered at the end of their lifecycle. 
It is listed as a known issue.   

### Testing User Stories from User Experience (UX) Section

-   #### Visiting User Goals

    1. As a visiting user, I want to easily understand the main purpose of the site.

        1. Upon entering the site, users are automatically greeted with the clean and easily readable page which contains the title heading "It sil heve" and underneath that the subheading "Elfstedentocht quiz" with three buttons to go to the page of their choice. [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/btnhowtoplay.png?raw=true)
        2. Underneath the titles are three buttons labelled "How to play?", "Let's play" and "Scoreboard". 
        3. Text has intentionally been kept to an absolute minimum.
        
    2. As a visiting user, I want to be able to easily navigate throughout the site.

        1. The buttons on the home page provide the user with clearly marked links to the respective pages. These buttons are the same across all pages. [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/btnletsplay.png?raw=true)
        2. The home button is located at the bottom of every screen [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/homebtn.png?raw=true), except of course the home page itself.
        3. The game page automatically opens into the end of game page upon completion of the game [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/endgame.png?raw=true)
        4. After submitting a username and saving their score, the scoreboard page also loads automatically [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/endgame2.png?raw=true) and [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/scoreboard.png?raw=true)
                      
    3. As a visiting user, I want to know my position in the game.
        
        1. On the game page the user is presented with the question counter in the top left hand corner. [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/play.png?raw=true)
        2. The counter shows what question out of ten question in a game the user is currently playing.
        3. A new question is automatically loaded one second after submitting the answer to the previous question.
        4. An easily distinguishable "Home" button sits at the bottom of the screen should the user wish to abort the game and return to the home page [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/homebtn.png?raw=true)
        5. At the end of the game, the end of game page is automatically opened and the user is urged to submit their name to be added to the scoreboard. [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/endgame.png?raw=true) 
                   
    4. As a visiting user, I want to compete.
        
        1. On the home page, the user is first presented with a button labelled "How to play?" [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/btnhowtoplay.png?raw=true) which when clicked opens a modal with instructions [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/modal.png?raw=true)        
        2. On the home page, the user is presented with a button labelled "Let's Play" which when clicked opens the game page [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/btnletsplay.png?raw=true)
        3. The game page loads questions automatically  [View](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/play.png?raw=true)
        4. Correctly answered questions are noted in [this](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/correct.png?raw=true) manner while incorrectly answered questions are noted in [this](https://github.com/MSierag/It-sil-heve/blob/master/assets/images/testing/userstories/incorrect.png?raw=true) manner.
        4. At the end of the game the user is prompted to enter their name and submit their score.
        5. Alternatively, the user can view the scoreboard or play again to improve their score.  

### Known Issues

-   On mobile devices with a screen narrower than 360px the contents of the card section on index.html pushed out of alignment.
    -   Text and text on buttons disappears from view as a result.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps:

1. Log in to GitHub and locate the [It-sil-heve repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://msierag.github.io/It-sil-heve/) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [It-sil-heve repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [It-sil-heve repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Bootstrap5](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [YouTube](https://www.youtube.com/watch?v=MxrGPP4F8Sc): The game page with its JavaScript functionality was copied from this tutorial.   

-   I feel compelled to mention I spend countless hours wading through repositories and tutorials. I learned so much and was influenced by all of it. So thank you to all who have shared JavaScript code relating to quiz games online, this project would not have been possible without you.

### Content

-   Inspiration for the questions was taken from [Wikipedia](https://en.wikipedia.org/wiki/Elfstedentocht).

### Media

-   Background image for the home page by Steve Photography on [Shutterstock](https://www.shutterstock.com/image-photo/ice-skating-on-gouwzee-netherlands-86205925)

### Acknowledgements

-  Code Institure Student Care, Alexander Farrell for invaluable help.

-  Code Institue assessors for understanding and leniency. 

-  Friends and family for feedback and helpful suggestions.