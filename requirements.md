# Software Requirements

## Vision

The App of tomorrow that compares product prices from Amazon, Target and Wal-Mart. This App will save time for the user by automating the price tracking process for the desired product.  It provides alerts when your target price is found.


## Scope (In/Out)

IN - What will your product do

The web app will provide price comparisons based on user's input like website preference, product name and price threshold.  Users will sign in or create an account. Once the user is signed in, the app will prompt the user to enter web sites, product and desired price.
The app will automatically track pricing for each of the sites and return the information to the user. It will also notify the user through text message when the desired price is found.

OUT - What will your product not do.

The app will not automatically find the web page within the web site for a given product. The app will not support every website.  It will not buy the product on behalf of the user.

## MVP

What will your MVP functionality be?

For MVP, the app will take in user email, telephone number and cell carrier. Create an account for the user and let the user track product(s) from Amazon, Target and Walmart.  User will need to provide the links to the specific product page from the desired sites. The app will continue to track price changes. User will set target price to receive text notification and program will automatically send when target price is found.

What are your stretch goals?

Our stretch goals are: (1) see historical data from previous saved product searches (2) style the text output in the terminal (3) automation of product search i.e. without user providing link.


## Functional Requirements

A user can create and update their profile information

A user can track multiple products on the different web sites

A user can set a desired price for the product

Data Flow

User enters profile or contact information
User enters a product  (name, price, product web page) to track
Data is sent to the scraper function.  
Scraper function returns parsed data from a given web site.
Parsed data is stored in a database under the user's email.
Check prices against target price for notification.

## Non-Functional Requirements

Usability
App will have a command line interface for the user that is menu driven. Account settings will be configurable for contact information, price notification and product information.

Testability
We will be testing for components functionality, logic and desired output. Test coverage would be at least 80%.
