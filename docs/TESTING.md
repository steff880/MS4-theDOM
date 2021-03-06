![Responsive](/docs/images/responsive1.png)

## Bugs and Fixes

- Bug:

When testing if printing _**bag_items**_ will print the _**item_id**_, _**quantity**_ and the _**course*_, encountered few issues.

![Bag Bug](/docs/images/bag-bug.png)

As I was following the Boutique Ado mini project, unintentionally wrote _**product_count**_ instead of _**course_count**_. The other issue is, that I missed to append the _**course**_ in _**bag_items**_.

- Fix:

Change the variable _**product_count**_ to _**course_count**_ and append the _**course**_ in _**bag_items**_.

- Bug:

While testing the **Shopping bag page**, noticed that the **bag total** was not calculated properly. 
Instead of multiplying the _**quantity**_ by the _**price**_, it was adding the _**quantity**_ to the _**price**_.

![Bag total](/docs/images/bag-total-bug.png)
![Bag total](/docs/images/bag-total-bug1.png)

- Fix:

Update the **bag total** to be calculated by multiplying the _**quantity**_ by the _**price**_

- Bug:

Issue calculating the **order total** correctly. 

When testing to see the order after checkout in admin panel, realized that **discount** is applied to orders _below_ the threshold ($30).

![Order total](/docs/images/order-total-discount-bug.png)
![Order total](/docs/images/order-total-discount-bug1.png)

- Fix:

Change code to apply the discount only when the **total** is **_greater_** than **discount threshold**

- Bug:

When testing adding a course without image and try to access it it throws the error below. The reason is that on Course Detail page the link for couuse without image was wrong, and points to a non-existing image.

![No image](/docs/images/no-image-bug.png)
![No image](/docs/images/no-image-bug1.png)

- Fix:

Add {{ MEDIA_URL }}noimage.png in the _href_ attribute of the link.

- Bug:

Created new model and run migrations. It worked locally but seemed like the new model was not migrated to **Postgres**. Which resulted in this error.

![Migrations](/docs/images/migrations-postgres.png)


- Fix:

Had a _Tutor Assistance_ and was suggested to create environmental variable in gitpod called **DATABASE_URL**, which value was the _url_ for **Postgres** and set **DEBUG** to false. Stop the workspace and start it again. After doing this, in the _terminal_ was a message that I need to run migrations to **Postgres**. I used the command `python3 manage.py migrate --plan`, which showed everything that needs to be migrated. Confirmed that it is correct and run `python3 manage.py migrate`. Then when I reloaded the deployed site all worked normally.

## Testing User Stories

- Detemine site's purpouse

    - Site's purpose is clearly notable from the moment user enters the site

- Easy navigation

    - The fixed top navigation bar makes the site easy to navigate from any position to any point of the site
    - Site's logo will always take the user back to home page on desctop and home icon will do the same on mobile
    - Button are placed through the site so the user can navigate to the other pages.

- Account creation and email confirmation.

    - Users can fill in the registration form and create an account.
    - Uppon completing the registration form, users will receive a confirmation email with a link to activate their account.

- View all courses and choose best for them.

    - Users can navigate to Courses page through the navigation menu or from Explore Courses button.
    - After creating an account, users can view the Course Detail page and learn more about the course.

- View course description and reviews.

    - Users can find course description on Course Detail page and also view all reviews.

- Add courses to the bag and see a confirmation.

    - Once users create an account, they can add courses to the shopping bag.
    - If course is added to the bag, a toast message will inform the user that a course has been added to the bag.

- Be able to view courses in the Profile page.

    - If the user has made a purchase, the course video is added to their page.

- Be able to leave reviews.

    - If the user has an account, he/she can add reviews about courses after filling in the course review form.

- Be able to eddit reviews.

    - If user is logged in or a superuser, they can edit their course reviews.

- Be able to add/remove courses to the wishlist.

    - If the user has an account, he/she can add/remove courses to/from their wishlist.

## Manual Testing

The following tests have been carried out without issue:

### Sign in and Out

- Confirm clicking Login or Sign Out from the Account tab signs the user out and displays a confirmation message

    - Pass

### Navigation

- Click TheDOM logo to go back to Home page

    - Pass

- Click All Courses displays all courses

    - Pass

- Click Frontend displays only frontend courses

    - Pass

- Click Backend displays only Backend courses

    - Pass

- Click My Account (logged out) to confirm only options Register and Login are displayed

    - Pass

- Click My Account (logged in as Registered user) to confirm only options My Profile and Logout are displayed

    - Pass

- Click My Account (logged in as Superuser) to confirm options Manage Courses, My Profile and Logout are displayed

    - Pass

- Click Wishlist or Heart on mobile (logged out) to confirm redirect to Sign In page

    - Pass

- Click Wishlist or Heart on mobile (logged in as Registered user) to confirm Wishlist page is displayed

    - Pass

- Click Bag (logged out) to confirm redirect to Sign In page

    - Pass

Click Bag (logged in as Registered user) to confirm goes to Shopping Bag page
    - Pass

- Reduce horizontal screen width to 991px to confirm hamburger icon replaces main nav items

    - Pass


- Reduce horizontal screen width to 991px to confirm are Home, Search, User, Heart, and Bag icons are displayed

    - Pass

- Reduce horizontal screen width to 320px to confirm no display errors

    - Pass

### Footer

- Hover over footer icons to trigger animation

    - Pass

- Click each footer icon to confirm relevant social media page opens in a new window
    - Pass


### Search Bar

- Confirm search for "Web" displays courses containing the word either in their name ot description 

    - Pass

- Confirm the display of correct information about the search
    
    - As expected, from the previous test the display was **_6 Courses found for "web"_**


### Home Page

- On page load, confirm animation of the text showing from the right and the CTA button pops up 

    - Pass

- Confirm Explore Courses cta button displays Courses page showing all courses

    - Pass


- Confirm scrolling down the page triggers text fade in from the right 

    - Pass

- Confirm hovering over buttons triggers hover effects 

    - Pass


### Courses

- Select each option from the Sort By selector to confirm courses are listed in the corresponding order

    - Pass

- Check against the database that the correct price is shown for each course

    - Pass

- Confirm the correct category is displayed for each course

    - Pass

![Category](/docs/images/category.png)

- Click on the course image to display Course Detail Pge

    - Pass

### Course Details Page

- Confirm correct information about Course is displayed

    - Pass

- Confirm no edit or delete buttons are shown if user is not **superuser**

    - Pass

- When logged in as a superuser confirm clicking edit button leads to the Edit Course page

    - Pass

- Confirm clicking delete button brings up modal asking for confirmation

    - Pass

- Confirm clicking Delete removes the course from the database

    - Pass

- Confirm that users can update the quantity using the +/- buttons or by inputing into the field

    - Pass

- Confirm that the quantity entered cannot be less than 1 or more than 2, either using arrow keys, clicking the +/- or entering the number manually

    - Pass
 
![Max value](/docs/images/max-value.png)

- Confirm that clicking the Keep Shopping button takes user back to all courses view

    - Pass

- Confirm that clicking the Add to Bag button does add the course to the shopping bag

    - Pass

- Confirm that clicking the Add to Wishlist button does add the course to the wishlist

    - Pass

![Course info](/docs/images/course-info.png)

- Confirm that if a course has no reivews, a message asking user to leave a review is displayed

    - Pass

- Confirm that only review owner or Super user can see edit button to edit their review

    - Pass

### Shopping Bag

- Confirm that when there are no courses in the shopping bag, visiting the Shopping Bag page displays a message saying "Your bag is empty" and there is a Keep Shopping Button, which navigates to Courses page
    - Pass

- Confirm quantities updated by clicking **Update**

    - Pass

- Confirm line items can be removed by clicking the **Remove**

    - Pass

- Confirm 10% discount is applied to orders over $30

    - Pass

- Confirm that if a course was removed from shopping bag, a toast message appears informing the user that it has been removed from the bag

    - Pass

### Checkout

- Confirm correct items and amounts carried over from the bag, including discount if applied

    - Pass

- Confirm Stripe webhooks successfully processed and Order saved

    - Pass


### My Account

- Confirm details can be updated and they prepopulate checkout form

    - Pass

- Confirm buying a course adds an embeded video in the My Courses section 

    - Pass

![My courses](/docs/images/my-courses.png)

- Confirm Order History is shown and successfully updates 

    - Pass

### Add/Edit Courses

- Confirm only superuser can access those pages

    - Pass

- Confirm added or updated course reflected in database

    - Pass

## Responsiveness

The site has been designed with a mobile first approach, with the help of Bootstrap and has been testd using Chrome DevTools

Media queries are used as well to maximize responsiveness.

### Browsers

Tested on:

- Chrome

    - No issues

- Edge

    - No issues

- Opera 

    - No issues

- Firefox 

    - No issues


### Screen sizes

Tested with Chrome DevTools using profiles for the following devices, accounting for minimum screen widths of 320px:

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro

... and also using the responsive profiles of:

- Mobile S (320px)
- Mobile M (375px)
- Mobile L (425px)
- Tablet (768px)
- Laptop (1024px)
- Laptop L (1440px)

Real world testing on:

- Samsung Galaxy S10
- Samsung Galaxy S9+


## Known Issues

 When initially planing for MS4 did not realize that, when I create a site about web dev courses, it will not be a good idea to let users choose quantity that is greater than 1.

Unfortunately when I relized it, was already too late to make big changes, due to really being pressed by the time, so I came up with the idea to disable the form submission if the maximum value is more than 2. Also disable the +/- buttons as well following the same logic. Also I did not want to start deleting code and end up breaking something, close to submission of my project. At least now user will not be able to purchase 99 courses. I know this solution is not the best, but it was all I was able to do at that point.

This issue will be fixed in future updates.

![Course category](/docs/images/course-value-issue.png)

- Bag is not saved if a user logs out while items are in their bag.


### W3C Validator Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were
no syntax errors in the project.

[W3C Markup Validator](https://validator.w3.org/)

- One error and one warning was found for a duplicate ID used. The reason for thisis that there is a second file for mobile-top-navigation and it contains the same code as the one on the **base template**. It does not affect the functionality of the website.

![W3C Markup Validator](/docs/images/w3c-markup.png)


[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

- No errors found. All warnings are from bootstrap and vendor prefixes.

![CSS](/docs/images/w3c-css.png)
![CSS](/docs/images/w3c-css-bs.png)
![CSS](/docs/images/w3c-css-vendor.png)


### [JSHint](https://jshint.com/)

All code found valid. Few warnings for Jquery _$_ sign.


### Python code testing

The python extention was used to test for Pep8 compliance and linting.

- Most of the Python errors were fixed during development

- Any errors related to files auto generated by Django were left untouched.

    - Migration files
    - Project `settings.py`
    - ./manage.py file
    - checkout/init.py

- The errors related to the variable **'e'** were left untouched

    - Variable 'e' here is used to capture any errors from the Stripe webhook handler.

- **'checkout.signals'** not being used in ./checkout/apps.py

    - The import is used to let Django know there a signals module, listening for changes to automatically updating the totals

- Line too long erros

    - Most of line too long errors were fixed during development
