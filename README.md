JAMTREE

There's a huge gap in the market for websites to bring musicians together to jam, have fun, and even start a band.
There's many websites out there to find members, but none of them particularly pretty or inviting.

UX

I set out to create a system where you didn't have to commit to joining a band, you could simply have a jam, and get to know other
musicians in your area. This meant keeping things simple, I was originally thinking of a system to create bands as well,
and even make a jam a gig, setting prices, but I dialled the functionality back to keep it casual and simple for users.

I wanted a simple interface, so the user had everything they needed in the nav bar. This also influenced the
jam-inspired color scheme of purples and reds, with the lime greens always present to guide the users eyes to the
buttons not in the search bar.

Finally, I added a welcome message on the main page for users not logged in, to explain what the site was for, 
with a link to sign up, allowing them more permissions and interactivity.

I didn't deviate too far from the original frameworks I made:

![alt text](/static/images/IMG_20190531_122737.jpg)
![alt text](/static/images/IMG_20190531_122747.jpg)

Finally, I used dbdiagram.io to help me undertand the relationships between the different databases.

Here's a link to the original diagram - https://dbdiagram.io/d/5d4d79c7ced98361d6dd75ac

FEATURES

EXISTING FEATURES

View Jams - Allows users to see all created jams
View Users - Allows users to see all users that are signed up
Login Feature - A bare-bones login system, to allow only users to be able to edit jams, and only jam creators to be able to edit
certain features.
Sign Up - Allows users to create their own accounts.
Add Jam - Allows users to create their own Jam for up to 10 people.
Edit Jam - Allows a jam creator to edit all features of the jam.
Guest-Edit Jam - Allows a user who hasn't created the jam to change the members and instruments,
effectively being able to sign themselves up.

FUTURE FEATURES

Search by county/genre - The ability to be able to search the jams by country or genre would be helpful for users to
narrow down their search.
Search by county/instruments - Similarly, searching users by county or instrument would help create a jam.
Norifications - Notifications so requests can be made eg. Requesting a user for a jam, or a user requesting to join a jam.
Hash passwords - The password feature is currently very basic. For data protection, I would implement an encryption system.
User profile - I would flesh out user profiles, using Spotify API's, profile pictures, and a bio.
Map search feature - To be able to physically see where the jams and users are would be beneficial for users looking for a jam.

TECHNOLOGIES USED

In this project I used the following:

HTML https://html.com/

SASS https://sass-lang.com/ - This was used to make the styling process more streamlined.

Materializecss - https://materializecss.com/color.html - This was to speed the styling process up.

Javascript - https://www.javascript.com/ - This was used for certain functionality, such as superficial changes to the page.

Python - https://www.python.org/ - Used for the back end, and to speak with the data in MongoDB.

MongoDB - https://www.mongodb.com/ - I used this as a database to store the objects.

Flask - https://www.fullstackpython.com/flask.html - This was used to simplify the Python code.

Google Fonts - https://fonts.google.com/ - Used for a wider range of fonts.

TESTING

I did manual testing throughout, making sure each function worked as intended. I would try all different possible outcomes, and
troubleshooted anything I wasn't happy with until I'd got the code working as expected.

A main example was when editing a jam, anything that wasn't touched by the user would simply disappear from the object. After
numerous attempts to rectify this, I simply had to re-post the information on the form, so instead of leaving a field blank,
I would have the system automatically input the original value, so if untouched, the field wasn't empty.

I also had issues with users being able to edit the jam creator to themselves, therefore being able to edit every element of 
the jam. I realised this was down to an error in my code, that overwrote the creator with whoever was logged in.

Finally, I had my friends test the website as well, creating accounts that I later deleted, and adding, editing, and deleting jams,
and then ironed out the bugs they found.

DEPLOYMENT

I deployed the project using both Github and Heroku.

I pushed my code to Github throughout it's creation, to allow myself to go back if I'd made errors.

I had issues with the Heroku app, and after much troubleshooting, the final if statement on app.py was to blame.
I updated this and finally got it working on Heroku.

MEDIA

The static background image was taken from Pexels.com, https://www.pexels.com/photo/people-in-concert-154147/.

This was the only asset used that I didn't create myself, other than the stylings from Materializecss.

ACKNOWLEDGEMENTS

My research of similar concepts helped me gain an idea of how I wanted to deviate from the normal formula, website include:
https://www.bandmix.co.uk/
https://www.find-a-musician.com
https://www.joinmyband.co.uk/

I took inspiration from Gumtree for the name, as this is the only place I have been successful finding musicians to play with.

I used coolers to refine my color scheme https://coolors.co/.

I also used this Youtube video to help create the login system - https://www.youtube.com/watch?v=vVx1737auSE

Last but not least, a HUGE thanks to both Chris Zielinski, and Brian Macharia, my former and current mentors, who made the 
seemingly unresolveable issues resolveable, and helped me understand the theory behind this.

Also a big thank you to Michael, my Tutor, who helped me with the deployment to Heroku