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

![Bag Bug](/docs/images/bag-total-bug.png)
![Bag Bug](/docs/images/bag-total-bug1.png)

- Fix:

Update the **bag total** to be calculated by multiplying the _**quantity**_ by the _**price**_

- Bug:

Issue calculating the **order total** correctly. 

When testing to see the order after checkout in admin panel, realized that **discount** is applied to orders _below_ the threshold ($30).

![Bag Bug](/docs/images/order-total-discount-bug.png)
![Bag Bug](/docs/images/order-total-discount-bug1.png)

- Fix:

Change code to apply the discount only when the **total** is **_greater_** than **discount threshold**

- Bug:

When testing adding a course without image and try to access it it throws the error below. The reason is that on Course Detail page the link for couuse without image was wrong, and points to a non-existing image.

![Bag Bug](/docs/images/no-image-bug.png)
![Bag Bug](/docs/images/no-image-bug1.png)

- Fix:

Add {{ MEDIA_URL }}noimage.png in the _href_ attribute of the link.

- Bug:

Created new model and run migrations. It worked locally but seemed like the new model was not migrated to **Postgres**. Which resulted in this error.

![Bag Bug](/docs/images/migrations-postgres.png)


- Fix:

Had a _Tutor Assistance_ and was suggested to create environmental variable in gitpod called **DATABASE_URL**, which value was the _url_ for **Postgres** and set **DEBUG** to false. Stop the workspace and start it again. After doing this, in the _terminal_ was a message that I need to run migrations to **Postgres**. I used the command `python3 manage.py migrate --plan`, which showed everything that needs to be migrated. Confirmed that it is correct and run `python3 manage.py migrate`. Then when I reloaded the deployed site all worked normally.



## Known Issues

 When initially planing for MS4 did not realize that, when I create a site about web dev courses, it will not be a good idea to let users choose quantity that is greater than 1.

Unfortunately when I relized it, was already too late to make big changes, due to really being pressed by the time, so I came up with the idea to disable the form submission if the maximum value is more than 2. Also disable the +/- buttons as well following the same logic. Also I did not want to start deleting code and end up breaking something, close to submission of my project. At least now user will not be able to purchase 99 courses. I know this solution is not the best, but it was all I was able to do at that point.

This issue will be fixed in future updates.

![Bag Bug](/docs/images/course-value-issue.png)
