# My Price Scout

This app allows you to add desired items from different online retailers to a watchlist and set your desired price. The app will notify you when the item price drops to the desired level via text notification.

## Authors

Marni Hager, Jae Loney, Pedro Perez, Sergii Otryshko

## User Stories

<https://python401.atlassian.net/wiki/spaces/US/pages/590051/User+Stories+-+My+Price+Scout>

## Database Schema

[“User”: {  
“Email”:”” : String  
 “PhoneNumber”: “” : Integers  
“PhoneCarrier” : “” : String  
“ProductsList”: [] : List[object]  
}]  
The products class gives each item the attributes below:
Product - Will have name/nickname(string), links to products(strings), current prices(integers), whether they are being tracked(Boolean), strike prices (integers).

## UML

![UML](https://github.com/Cuatro-Programadores/my-price-scout/blob/main/images/my-price-scout-uml.png)

## Wireframe

![Wireframe](https://github.com/Cuatro-Programadores/my-price-scout/blob/main/images/Wireframe-MyPriceScout.png)

## Resources

Email Validation: <https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/>  
Amazon Scraping: <https://www.youtube.com/watch?v=DHqAQxgleoc&ab_channel=JieJenn>  
Amazon Scraping: <https://www.youtube.com/watch?v=Bg9r_yLk7VY&ab_channel=DevEd>  
Amazon Scraping: <https://github.com/ArkadiyReydman/Amazon-Walmart-Etsy-Price-Tracker/blob/master/price_tracker.py>  
Email Regex Validation: <https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/>
Email Number Validation: <https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number>
Nested Dictionaries: <https://www.programiz.com/python-programming/nested-dictionary>
Function Str's and Repr's: <https://www.pythontutorial.net/python-oop/python-__repr__/>
My Price Scout Terminal Image: <https://patorjk.com/software/taag/#p=display&f=Avatar&t=Type%20Something%20>
Terminal Font Colouring: <https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal>

