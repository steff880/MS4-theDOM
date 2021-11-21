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



## Technologies Used
### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
---

[^ back to top ^](#table-of-contents)

### Frameworks, Libraries & Programs Used


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


