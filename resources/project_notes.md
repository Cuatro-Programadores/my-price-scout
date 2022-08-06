# Class inputs/outputs:

* Capture email: inputs - email, outputs - validated email 
* Capture number: inputs - phone, outputs - validated phone
* Capture carrier: inputs - carrier, validated carrier
* Capture product_name: inputs - user product nickname, validated carrier
* Capture website: inputs - website name from list 
* Capture url: inputs - url, validated url(currently there is barely validation) --> (changed)Also pass to the correct scraper function- This will actually happen in App!
* Capture strike_price: inputs - integer 
* Capture notification: inputs Boolean or user input returns Boolean or none
* Capture menu_nav: inputs - number from 1-6 based on where the user would like to go


* App
  * get_or_create_user: inputs - email, phone, carrier, outputs - User instance
    * helper methods: get_user, create_user, save_user
    * save_user will parse the User instance into key values and save to Db 
      using Database Utils
  * Menu: inputs - none, outputs - screen prompts or return information
    * helpers: IO Utils, User, and Item
    * manage_user_items: logic for when a user has items to add, remove, or 
      edit items


* User
  * add_item: inputs - product name, url(s), target_price(s), output - none
  * remove_item: inputs - product name, output - none 
  * get_items: inputs - none, output - returns user watchlist
  * edit_item: inputs - product name, output - none


* Product - This will act upon the Link class to add, remove, and change url(s).
  * add_specific_product: inputs - url(s), output - confirmation string  (may need to 
    break this out to individual links)
  * add_name: inputs - name, output - confirmation string
  * add_target_price: - inputs - int, output - confirmation string
  * product_url_count: inputs - name, output - int
  * remove_url: inputs - Link aka specific product, output - confirmation 
    string
  * get_summary: inputs - name, output - all data for the item (representation)
  * change_url: inputs - website name, output - confirmation, calls 
    remove_url followed by add_url
  * is_product_being_tracked: inputs - boolean, output - string about tracking, 
    returns boolean (this should toggle tracking)


* Db Utils
  * get_data: inputs - email as key, outputs - email as key, User as value 
    from database
  * set_data: inputs - email as key, outputs - User as value to database


* Scraper
  * scrape_Amazon: inputs - url, outputs - price
  * scrape_Target: inputs - url, outputs - price
  * scrape_Walmart: inputs - url, outputs - price


* Tracker
  * fetch_data: inputs - none, outputs - refreshed data for item 
  * send_notification: inputs - price, email, outputs - text notification


* Specific_Product
  * website is the name (i.e., Amazon, Target, Walmart)
  * url is the specific webpage the user puts in
  * actual_price is the value found on the link by the Scraper