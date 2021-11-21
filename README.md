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

The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institiue student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

**Requirements**

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)
- [AWS S3](https://aws.amazon.com/)

**Creating a Clone**

1. From the repository, click *Code*
2. In the *Clone >> HTTPS* section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2 - ``git clone https://github.com/steff880/MS4-theDOM.git``
6. Set the following values in a `env.py` file.
```
import os

os.environ.setdefault("SECRET_KEY", "<app secret key of your choice>")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault('STRIPE_PUBLIC_KEY', '<key generated by Stripe>')
os.environ.setdefault('STRIPE_SECRET_KEY', '<key generated by Stripe>')
os.environ.setdefault('STRIPE_WH_SECRET', '<key generated by Stripe>')
```

- Stripe keys are generated by Stripe, each individual have their own unique key values.
- *PLEASE MAKE SURE NEVER TO PUBLISH THESE KEYS, ADD THE `env.py` TO A `.gitignore` TO AVOID PUSHING KEYS TO GITHUB.*
7. Install the project requirements - `pip3 install requirements.txt`
8. Apply database migrations - `python manage.py migrate`
9. Create a superuser - `python manage.py createsuperuser`
10. The project can be run with the following - `python manage.py runserver`

**Heroku Deployment**

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have `dj_database_url` and `psycopg2` installed.
```
pip3 install dj_database_url
pip3 install psycopg2
```
5. Login to the Heroku CLI - `heroku login -i`
6. Run migrations on Heroku Postgres - `heroku run python manage.py migrate`
7. Create a superuser - `python manage.py createsuperuser`
8. Install `gunicorn` - `pip3 install gunicorn`
9. Create a requirements.txt file - `pip3 freeze > requirements.txt`
10. Create a `Procfile` (note the capital P), and add the following,
```
web: gunicorn the_dom.wsgi:application
```
11. Disable Heroku from collecting static files - `heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>`
12. Add the hostname to project settings.py file
```
ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost']

```
13. Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing `connect`
14. In Heroku, within settings, under config vars select `Reveal config vars`
15. Add the following, 
```
AWS_ACCESS_KEY_ID =	<your variable here>
AWS_SECRET_ACCESS_KEY =	<your variable here>
DATABASE_URL =	<added by Heroku when Postgres installed>
DISABLE_COLLECTSTATIC =	1 
EMAIL_HOST_PASS = <your variable here>
EMAIL_HOST_USER = <your variable here>
SECRET_KEY = <your variable here>
STRIPE_PUBLIC_KEY = <your variable here>
STRIPE_SECRET_KEY = <your variable here>
STRIPE_WH_SECRET = <different from env.py>
USE_AWS = True
```
16. Go back to the Deploy tab and under Automatic deploys choose `Enable Automatic Deploys`
17. Back in your CLI add, commit and push your changes and Heroku will automatically deploy your app
```
git add .
git commit -m "Initial commit"
git push
```
18. Your deployed site can be launched by clicking `Open App` from its page within Heroku.

**AWS S3 Bucket setup**
1. Create an Amazon AWS account
2. Search for S3 and create a new bucket
    - Allow public access
3. Under Properties > Static website hosting
    - Enable
    - index.html as index.html
    - save
4. Under Permissions > CORS use the following:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Under Permissions > Bucket Policy:
    - Generate Bucket Policy and take note of Bucket ARN
    - Chose S3 Bucket Policy as Type of Policy
    - For Principal, enter *
    - Enter ARN noted above
    - Add Statement
    - Generate Policy
    - Copy Policy JSON Document
    - Paste policy into Edit Bucket policy on the previous tab
    - Save changes
6. Under Access Control List (ACL):
    - For Everyone (public access), tick List
    - Accept that everyone in the world may access the Bucket
    - Save changes

**AWS IAM (Identity and Access Management) setup**
1. From the IAM dashboard within AWS, select User Groups:
    - Create a new group
    - Click through and Create Group
2. Select Policies:
    - Create policy
    - Under JSON tab, click Import managed policy
    - Choose AmazongS3FullAccess
    - Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
    - Click next step and go to Review policy
    - Give the policy a name and description of your choice
    - Create policy
3. Go back to User Groups and choose the group created earlier
    - Under Permissions > Add permissions, choose Attach Policies and select the one just created
    - Add permissions
4. Under Users:
    - Choose a user name 
    - Select Programmatic access as the Access type
    - Click Next
    - Add the user to the Group just created
    - Click Next and Create User
5. Download the `.csv` containing the access key and secret access key.
    - **THE `.csv` FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.**

**Connecting Heroku to AWS S3**
1. Install boto3 and django-storages
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
2. Add the values from the `.csv` you downloaded to your Heroku Config Vars under Settings:
3. Delete the `DISABLE_COLLECTSTATIC` variable from your Cvars and deploy your Heroku app
4. With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.
    - **PLEASE MAKE SURE `media` AND `static` FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS**



[^ back to top ^](#table-of-contents)

## Credits
### Resources


[^ back to top ^](#table-of-contents)

### Code

- A large amount of code came from the Code Institute, Boutique Ado Project.
[Code Institute, Boutique Ado](https://github.com/steff880/ci-boutique_ado_v1)
- Boutique Ado is a walkthrough project by Code Institute, this project gave students an introduction to Django/AWS S3/Stripe/Heroku Postgres
- The core functionality of TheDOM is all taken from the Boutique Ado project.

[Harry-Leepz, Nourish and Lift](https://github.com/Harry-Leepz/Nourish-and-Lift)

- Rreview and wishlist part from the link above

**Bootstrap**
- The Bootstrap Library was used through the project. The project used version 4.4.
- [Bootstrap](https://getbootstrap.com/docs/4.4/components/alerts/)
    - Toasts/Navigation Bar/Forms/Dropdown Menu/Buttons, the core elements mentioned are all found in the Bootstrap components section and built upon.

**Django Documentation**
- [Django Documentation ](https://docs.djangoproject.com/en/3.2/)

[^ back to top ^](#table-of-contents)

### Images

[Flask Logo](https://www.cleanpng.com/png-flask-python-web-framework-web-application-america-5227332/)

[Django Logo](https://www.pngwing.com/en/free-png-hwwqg)

[JavaScript Logo](https://www.cleanpng.com/png-javascript-node-js-logo-computer-programming-progr-2052076/)

[CSS Logo](https://www.cleanpng.com/png-web-development-cascading-style-sheets-css3-html-1615602/)

[Python Logo](https://www.cleanpng.com/png-angle-text-symbol-brand-other-python-622381/)

[HTML Logo](https://brandslogos.com/h/html-logo/)

[React Logo](https://www.pngwing.com/en/free-png-cgbgg)

- All SVG illustrations from:

[unDraw](https://undraw.co/illustrations)

The site does not allow to get individual liks for the illustrations.

All illustrations can be found on the link above.


[^ back to top ^](#table-of-contents)

### Acknowledgements

-   My mentor, Oluwaseun Owonikoko, for her guidance and feedback.
-   The team at Code Institute, for teaching me the necessary skills to create this site.
-   [Stackoverflow](https://stackoverflow.com/) - for general needs


