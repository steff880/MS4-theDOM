<h1 align="center">TheDOM</h1>

![Responsive](/docs/images/responsive1.png)

[View Live Site Here](https://steff880-the-dom.herokuapp.com/)

## Table of Contents

> - [UX](#ux)
> - [User Stories](#user-stories)
> - [Design](#design)
> - [Data Schema](#data-schema)
> - [Wireframes](#wireframes)
> - [Features](#features)
> - [Existing Features](#existing-features)
> - [Technologies Used](#technologies-used)
> - [Testing](#testing)
> - [Deployment](#deployment)
> - [Credits](#credits)
> - [Resources](#resources)
> - [Acknowledgements](#acknowledgements)

## Intro
Hello and welcome to TheDOM.

This is a full-stack project for the Code Institute's Full Stack Web Developer Course.


# UX 
## Project Goals
This is a website for Web Development Courses.

Its goal is to allow the users, to find courses suitable for their needs and be able to purchase them at the end.

Use _HTML5_, _CSS3_, _JavaScript_, _Python_, _Django_ and _Stripe_

## Strategy
### Owner Goals
- Be able to create a welcoming and easy to navigate site.
- Be able to, as an admin, Add, Edit, or Delete Courses.
- Allow users to search the database for courses.
- Allow users to filter through courses, by selecting a category.
### User Stories

#### First time user
I would like to:
- be able to determine the sites purpose.
- be able to easily navigate through the site.
- be able to create an account and receive an email confirmation.

#### Returning User/Shopper
I would like to:
- be able to, view all available courses, in order to find one that best suits me.
- be able to, view course description and reviews to help me decide, if that is the best course for me.
- be able to, add courses to the shopping bag and also see a confirmation of how many are being added.

#### Logged in User/Shopper
I would like to:
- be able to, see all purchased courses in my Profile page.
- be able to, leave reviews.
- be able to edit reviews.
- be able to add courses to my Wishlist.
- be able to remove courses from my Wishlist.

## Design

Bootstrap, as well as custom CSS has been used to help create the current design of the website. 

### Colors

- #212529

- #fff

- #f1f0ff

- #536DFE

- #aab7c4


#### Typography

- Montserrat was used as main font throughout the website

## Data Schema

- [Schema Design](https://github.com/steff880/MS4-theDOM/tree/main/docs/Schema)

#### **Key Models**

**UserProfile**
- The user profile is connected to the User model created by Allauth on registration.
- The default fields are saved fields by the user to speed up the checkout process by pre-populating shipping details.

**Order**
- The order model is connected to the User Profile, allows the user to view their previous orders.
- The order model acts as a container for the order line items. Although the item is stored within the OrderLineItem model, having them connected allows to retrieve the item purchased.

**Course**
- The course model holds key information for each course. Each course has a unique ID.
- The course model is connected to the category model, this allows the user to filter courses by category.

**CourseReview**
- Reviews for courses can be left for courses with this model, having it connect to the course model via the ID.
- The review model also is connected to the User model to obtain the user's username. This allows the user to see the name of the user on each review. 


**WishList**
- The wishlist model allows users to save items for quicker access. These items can be removed.
- This model also acts as a container for the WishListItem model. Just like the Order model, each wishlist is unique to each user but connecting to the user ID.

### Wireframes

- [Wireframes](https://github.com/steff880/MS4-theDOM/tree/main/docs/wireframes)


## Features
### Existing Features

#### Navigation Bar

- Navbar is implemented on every page and is fully responsive across all resolutions.
- Users can navigate across the site easily.

![Navigation](/docs/images/navigation.png)

#### Intro 

- Home page features a CTA button, a welcoming message and info about what is ofered on the site

![Info](/docs/images/info.png)

![Info](/docs/images/about.png)

![Info](/docs/images/about2.png)


#### Courses

- Offers the user a choice of web development courses with categories of Frontend and Backend


![Courses](/docs/images/courses.png)

#### Search

- Users can take advantage of the search bar and search for courses by name or description


#### Reviews

- Users who have created an account can take advantage and leave reviews for courses

![Review](/docs/images/reviews.png)
![Review](/docs/images/review-post.png)


#### Toasts

Toasts are used to provide the user with a information when they perform a certain action on the website.
Like adding courses to the bag, or writing a reviews, etc.

![Bag](/docs/images/toasts.png)


#### Shopping bag

In the Shopping bag user can see their order total, if there is a discount applied, or how much more they need to spend in order to get a discount.

![Review](/docs/images/shopping-bag.png)


#### Checkout

When the user goes to the Checkout page, there is an information about their order, how much they will be charged and a payment form in order to complete their order.

![Checkout](/docs/images/checkout-page.png)

## **Technologies Used**

- [Python](https://www.python.org/) 
    - The following Python modules were used on this project, 
        - asgiref==3.4.1
        - boto3==1.18.26
        - botocore==1.21.26
        - dj-database-url==0.5.0
        - Django==3.2.5
        - django-allauth==0.41.0
        - django-countries==7.2.1
        - django-crispy-forms==1.12.0
        - django-embed-video==1.4.0
        - django-storages==1.11.1
        - gunicorn==20.1.0
        - jmespath==0.10.0
        - oauthlib==3.1.1
        - Pillow==8.3.1
        - psycopg2-binary==2.9.1
        - pylint-django==2.4.4
        - pylint-plugin-utils==0.6
        - python3-openid==3.2.0
        - pytz==2021.1
        - requests-oauthlib==1.3.0
        - s3transfer==0.5.0
        - sqlparse==0.4.1
        - stripe==2.60.0

- [Heroku Postgres](https://www.heroku.com/postgres)

- [AWS S3](https://aws.amazon.com/)
 
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

- [Bootstrap](https://getbootstrap.com/)

- [jQuery](https://jquery.com/)

- [JavaScript](https://www.javascript.com/)

- [Google Fonts](https://fonts.google.com/)

- [Font Awesome](https://fontawesome.com/)

- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

- [Github](https://github.com/)

- [Git](https://git-scm.com/)

- [Gitpod](https://www.gitpod.io/)

- [Balsamiq](https://balsamiq.com/)

- [AutoPrefixer](https://autoprefixer.github.io/)

- [Grammarly](https://www.grammarly.com/)

---

[^ back to top ^](#table-of-contents)

## Testing

[All Testing](https://github.com/steff880/MS4-theDOM/blob/main/docs/TESTING.md)

[^ back to top ^](#table-of-contents)

## Deployment


[^ back to top ^](#table-of-contents)

### Clone It

1. Login to [GitHub](https://github.com/)
2. Fork the Repository.
3. Then click **Code** under the _Settings_ button.
4. Choose HTTPS, SSH, or GitHub CLI, then click the copy button to the right.
5. Open Git Bash
6. Change the directory to the location where you want the cloned directory to be made.
7. Type _git clone_ and paste the URL you copied before.
8. To create the clone press _Enter_

[^ back to top ^](#table-of-contents)

## Credits
### Resources


[^ back to top ^](#table-of-contents)

### Code


[^ back to top ^](#table-of-contents)

### Images


[^ back to top ^](#table-of-contents)

### Acknowledgements

-   My mentor, Oluwaseun Owonikoko, for her guidance and feedback.
-   The team at Code Institute, for teaching me the necessary skills to create this site.
-   [Stackoverflow](https://stackoverflow.com/) - for general needs


