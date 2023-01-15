# Distinctiveness and Complexity

None of the projects in CS50W are quite like this one. This is a website for the Lake Eden Association. While it's not completely finished due to the owners of the site lacking on getting back to me on the specifications they want on each page, the website is finished enough to satisfy the criteria of this project. This website has no conceptual similarities to any of the other CS50 Web projects. It is a website dedicated to the documentation, news, and health of a lake in Vermont, USA called Lake Eden. Here users can view news of the lake, keep up to date with the invasive species problem, donate to the Lake Eden Association, find volunteer opportunities, and more.

First and foremost, the layout.html file contains the layout of each page. This layout consists of a header, which has the Lake Eden Association logo (which if clicked returns the user to the home page), a link to an email sign-up page, a link to the Lake Eden Association Facebook page (which uses JavaScript to open the link in a new tab as to improve user experience), and a button that will take the user to the "Join, Renew, or Donate" page. Below this header lays the nav bar. This nav bar uses a combination of CSS and JavaScript to make reactive drop-down menu buttons that change color upon hovering, and again upon clicking. Finally, below the body of each webpage is a footer, which contains a footer image, buttons that link to important and potentially heavily used pages, and the mailing address of the Lake Eden Association.

There are quite a few pages on this website, and while a fair amount of them are blank (other than the header, nav bar, and footer layout) due to reasons discussed above, the more complex pages (such as those that contain forms) are complete and connected to the website's database. These completed pages include "Contact Us", "Mission & Bylaws", "Meeting Minutes", "Plans & Annual Reports", "Join Email List", "Join, Renew, or Donate", "Report Invasives", and "News & Events". Note that the links on pages "Mission & Bylaws", "Meeting Minutes", and "Plans & Annual Reports" don't work. The infrastructure is complete, though I lack the material to populate these links with the correct PDF files due to not yet recieving them from the website owners.


Among the completed pages are the following:

-index.html: This is the home page.

-article.html: This is the html that is dynamically generated when the administrator makes a new article.

-News & Events: This page shows all articles from newest to oldest, 8 per page, with pagination in place as to increase the user experience by not polluting the page with an overwhelming amount of content.

-Contact Us: This page contains contact information for key members of the Lake Eden Association.

-Mission & Bylaws: This contains a link (that doesn't currently go anywhere) that will display the bylaws of Lake Eden, as well as the mission statement of the Lake Eden Association.

-Meeting Minutes: This contains links (that doesn't currently go anywhere) that will display transcripts of the in-person meetings of the Lake Eden Association.

-Plans & Annual Reports: This contains links (that doesn't currently go anywhere) that will display annual reports.

-Join Email List: This form allows one to sign up for the Lake Eden email list. Submissions are stored in the database and displayed via the "/admin" route as a string representation of the information entered in the form. The administrator can then manually add this individual to their email list.

-Join, Renew, or Donate: This form allows one to donate via PayPal, or sign up for annual donations. While this form redirects you to the home page upon submission, in the future (once I know the website owner's PayPal account) you will instead be redirected to the Lake Eden Association's PayPal account in which you can send them money. Depending upon what you select for the radio buttons, the PayPal form will pop up with that specified dollar amount pre-filled into the form. Lastly, upon submission, this form sends the data entered to the database and is presented to the administrator (via "/admin") in a string representation of said data.

-Report Invasives: This form, much like the other two forms, sends the data that the user entered to the database in which the administrator can then view (via "/admin") it's string representation of the complied data. The administrator can then use this information to track and combat invasive species in Lake Eden.


Note that the "blank" pages I've mentioned don't contain content but still have the navbar and footer, as this is the template for all pages on this website, with the content of each page between this navbar and header.

Here is a list of these blank pages followed by a brief description of what they will contain once the website owners tell me what they want in them:

-History of The Lake: A detailed history of Lake Eden.

-Who We Are: A detailed explpaination of the fundamentals of the Lake Eden Association.

-Boating on Lake Eden: An explaination with examples of the fun it is to boat on Lake Eden.

-Greeter Program: An explaination of their greeter program, with possible links.

-Overview: An overview of the lake.

-Public Fishing & Boat Access: A map of numerous good fishing spots and boat launches on the lake.

-Volunteer Opportunities: A list of volunteer opportunities for helping the lake and community of Eden, VT, all with detailed explainations, pictures, and who to contact if interested.

-Why Become a Member: A page dedicated to explaining the benifits of becoming a member of the Lake Eden Association.

-About Milfoil: An explaination of all the intricicies of milfoil with pictures.

-Greeter & VIP Programs: An explaination of the greeter and VIP programs that the Lake Eden Association hosts.

-Milfoil Control Efforts: A page dedicated to keeping users up-to-date with the latest milfoil control efforts on the lake.

-Other Invasive Species: A list with breif explainations and pictures of other invasive species that are either currently on Lake Eden or that it is suseptable to.

-What Is An Invasive: A detailed explaination of invasive species.

-Health Overview: An up-to-date overview of the health of the lake.

-Lake Data & Maps: Statistics and maps of Lake Eden.

-Plant Surveys: Surveys of the area with a list of the different plant species along with pictures.

-Sampling & Monitoring Program: Updates of the invasive species monitoring program.

-Shoreline Health: An up-to-date overview of the health of Lake Eden's shortline.

-Privacy Policy: This page will display the website's privacy policy once it has been created.

### As per the Django framework, the filesystem is set up as such:

Contained in the "app" directory:

-static: This folder contains the program's css file, as well as a folder containing all of the program's images.

-migrations: This folder contains all the changes made to the infrastructure of the database.

-templates: This folder contains the html files of this website. The skeleton of each page of this website lives inside this folder.

article_images directory: When the administrator of the website creates a new article for the news page, the uploaded images for these articles are stored in this folder.

eden_project directory: This directory contains some of the administrative files that come with the Django framework, such as "__init__.py", "agi.py", "settings.py", "urls.py", and "wsgi.py".

All other files are your standard Django files you get when you start a new Django application, such as models.py which is where our database resides, admin.py which is where we register the various tables of our database that I created in models.py, views.py when our backend code is written in Python, etc.

### How to run this application:

You run this application like you would any other website, simply look up the url and traverse the numerous different pages on the website. Of course since this site is not currently active, for Harvard staff grading this website you will need to cd into the directory and launch the test server via the command "python manage.py runserver" to view this website.