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