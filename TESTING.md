Go back to the [README.md](README.md) file


## **Testing**


### User Stories

<br>
 
| USER STORY  |  TESTING |
|---          |---       |
| As a first-time visitor, I want to easily understand the purpose of the app. |  <ul><li> App name clearly states what it is - a to-do list for mums</li> <li> Landing Page - provides users with a clear understanding of what the app offers</li></ul>|
|As a first-time visitor, I want to be able to register and sign in to my profile. | <ul><li> Users need to register first to start creating their list in their accounts. The Registration Page provides a simple registration form with clearly labeled input fields.</li><li>Sign-In Page allows registered users access their accounts. Users are provided with a simple form with clear input fields for their username and password. After signing in, they are directed to their list.|</li></ul>
|  As a first-time and returning visitor, I want to stay signed in to avoid frequent log-ins , but with a clear and accessible sign-out option for when I need to exit my profile securely.  | <ul><li> The user's username is stored in the session for 7 days.</li><li>Users can easily find a sign-out option on each page either in the navbar or in the footer.|</li>
|  As a first-time and returning visitor, I want to navigate the app easily the app. I can access all the pages easily and go back to my list quickly.            | <ul><li> The navigation bar is provided at the top of the page. Users can navigate the app easily on different devices. </li><li> The footer offers additional navigation options, allowing to access the required pages</li><li>Both the navigation bar and the footer have clear links to the My List Page allowing the user to access it quickly</li>|
| As a first-time and returning visitor, I want to be able to add, edit and delete tasks and categories.            |<li>CRUD(Create, Read, Update, Delete) operations have been implemented in the app</li><li>Users can easily find the right action buttons to add, edit, and delete tasks and categories</li>|
| As a first-time and returning visitor, I want to be able to add details and due dates to my tasks.            |<li>When users add a new list item, they can use a date picker to set a due date for their task</li>  |
| As a first-time and returning visitor, I want to be able to prioritize tasks.            |<li> Users can mark a list item as important using a switch in the form for creating new tasks. This will then display a star icon next to the tasks marked as important</li><li> Users can use one of the sorting options to display the important tasks first to prioritize them</li> |
| As a first-time and returning visitor, I want to be able to cross out list items that are done and remove them from the list.            |<li>Tasks can be marked as completed by pressing the check button. The item will be then crossed out</li></li><li>Users can delete single items or perform a bulk action and delete all checked items using an action button placed below their to-do list</li>   |
| As a first-time and returning visitor, I want to be able to sort items on my list and categories as well.           |<li>On the My List Page the footer contains an interactive button to sort list items. Sorting options include alphabetical, by category or by importance<li>On the Categories Page the footer also contains a button for sorting. Here the sorting options include alphabetical and 'created by me first'.    |
| As a first-time and returning visitor, I want to be able to use the app easily on different devices.            | <li>Materialize CSS framework was used to create this app. It uses a flexible grid system, making layout responsive by default. This system ensures that your website’s content  maintains its integrity across devices</li><li>Additionally, CSS media queries have been used to ensure responsiveness on different screen sizes |
|  As a first-time and returning visitor, I want to receive immediate and clear feedback through notifications or messages within the app for various interactions, such as successfully adding, editing, or deleting tasks, errors, or confirmation prompts.           |<li> Flash messages provide immediate feedback to users following their actions within the app</li><li> JavaScript confirmation dialogs have been implemented to prevent accidental deletions. Before deleting any items or categories, users see a confirmation prompt asking them if they are sure they want to perform that action</li>|
|  As a first-time and returning visitor, I want to be able to search through to-do items and categories           | <li> The search box, prominently placed within the application's interface, enables users to find specific items or categories within their to-do list</li>  |
| As an administrator, I want to be able to add and delete categories.            | <li> The categories displayed to all users can only be added and deleted by the admin account</li> |


### Full Testing


| FEAUTURE | EXPECTED OUTCOME | TESTING PERFORMED | RESULT | PASS/ FAIL|
| --- | --- | --- | --- | --- |
| `Navbar` |
|  |  |  |  |  |
| **Mum's To-Do List Logo**| When clicked the user will be redirected to the landing page when not logged in and My List Page when logged in. | 1. Clicked the Logo when not logged in 2.Repeated the same action when logged in | 1. When not logged in, I was redirected to the Landing Page, whereas when logged in I was redirected to My List. | Pass |
| **Sign In Link**| When clicked the user will be redirected to the Sign In Page| Clicked the link | Redirected to the Sign In Page | Pass |
| **Register Link** | When clicked the user will be redirected to the Register Page. | Clicked the link | Redirected to the Register Page. | Pass |
| **My List Link**(Logged in users only) | When clicked the user will be redirected to My List Page. | Clicked the link | Redirected to My List Page | Pass |
| **Categories Page Link** (Logged in users only) | When clicked the user will be redirected to the Categories Page | Clicked the link | Redirected to the Categories Page | Pass |
| **Sign Out Link** (Logged in users only) | When clicked the user is signed out and is redirected to Sign In Page. On top of the Page the user sees a flash message 'You have been signed out' | Clicked the link | Got signed out and redirected to the Sign In Page. 'You've been signed out' message appeared| Pass |
| `Sign in Page` |
|  |  |  |  |  |
| **Username input** | The username should be between 3-15 characters  | Entered username less than 3 characters long | tooltip lets the user know they have not matched the requested format | Pass | |
| **Username input - empty** | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required | Pass |
| **Password input** | The password should be between 3-15 characters  | Entered password less than 3 characters long | tooltip lets the user know they have not matched the requested format | Pass | |
| **Password input empty**| This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required |  Pass |
| **Sign In button** | Saves the user to session and redirects to the My List Page with a user's name in the heading of a list.  | Submitted form | Redirected to the My List Page and my name shows in the list's heading | Pass |
| **Incorrect username or password used** | A flash message should display saying username/password incorrect - this is defensive programming - not letting user know which input is incorrect | Incorrect username/password entered |A message flashed to let the user know they have entered an incorrect username/password | Pass |
| **Register Link** | When clicked the user will be redirected to the Register Page. | Clicked the link | Redirected to the Register Page. | Pass |
| `Register Page` |
|  |  |  |  |  |
| **Username input** | The username should be between 3-15 characters  | Entered username less than 3 characters long | tooltip lets the user know they have not matched the requested format | Pass |
| **Username input - empty** | The username is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| **Username input** | If username already exists, message should flash to user | Entered an existing username | Message flashed to say username already exists | Pass|
| **Password input** | This field should be between 3-15 characters long | Entered password less than 3 characters long | Tooltip tells the user to match the requested format | Pass |
| **Password input** - empty | The password is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
| **Register button** | Should redirect the user to the My List Page and a 'registration complete message' will flash. The list's heading should display the user's name | Created new user and submitted form | Redirected to My List Page and the message 'registration complete' flashed. User's name was diplayed in the list's heading | Pass |
| **Sign In Link**| When clicked the user will be redirected to the Sign In Page.| Clicked the link | Redirected to the Sign In Page. | Pass |
| `Search Box` |
|   |   |   |   |  |
| **Search feature** | A search is performed when the user enters an item or category they are looking for  | <ol><li>Searched for an item on my list</li><li> Searched for a category</li></ul>| <ol><li>The search returned a list item I was looking for </li><li> The search returned all the items in that category</li></ul> | Pass |
| **Search feature** - nothing to show | If an item or a category does not exist, a flash message 'Sorry, there are no such items or categories' is displayed and directs them to the My List Page. | Searched for an item and then a category that hadn't been created | Both searches returned a 'Sorry....' message and I was redirected to My List Page | Pass |
| `My List` |
|   |   |   |   |  |
| **Add '+' button** in the heading | When the user clicks this button they should be taken to the Add New Item Page| Clicked button | Redirected to the Add New Item Page | Pass |
| **List item card reveal** | When the user clicks on the list item, the card reaveals item details | Clicked the item | Card revealed the details | Pass |
| **Check button on the list item card**| 1. When the user clicks the check button, the item should be  crossed out and a flash message 'One less thing to worry about!' should appear 2. If the user clicks that button again the crossing should disappear and the message 'That's fine, take your time' should appear.| 1.Clicked the check button 2. Clicked the check button again | 1. The item was crossed out and the right flash message appeared 2. The crossing disappeared and the right message appeared| Pass |
|**Edit  button on the list item card**| When the user clicks the edit button they should be directed to the Edit Item Page | Clicked the edit button | Redirected to Edit Item Page | Pass |
| **Delete button on the list item card**| When the user clicks the delete button a confirmation dialog should appear asking the user if they want to delete the item with options to confirm and cancel. If confirmed the item should be removed from the list and a flash message should appear | Clicked the delete button | The confirmation dialog appeared. After clicking ok to confirm, the item was removed from the list and a 'Deleted' flash message appeared | Pass |
| **Delete all checked items button** | When the user clicks the delete all checked buttons, a confirmation dialog will appear asking the user if they are sure they want to delete all the checked items. Once that's confirmed all the checked items should be removed from the list and a flash message 'Done and dusted! You're a star! should appear | Clicked the button | Confirmation dialog appeared, clicked ok - all checked items were removed | Pass |
| `Footer` |
|  |  |  |  |  |
|  **Filter button**| When clicked the user should see a collapsible head with 'sort by' header. Upon clicking on it, the full collapsible should display with all sorting options on it. They should be all clickable and depending on which one is clicked the user will see their items sorted alphabetically, by category or importance | Clicked the button. Clicked the button again to see all sorting options. Tried clicking them one by one. | Saw the sorting options and was able to click on them. The items were sorted accordingly. |  |
| **'+' button** | When clicked the user will be redirected to the Add New Item Page. | Clicked the button | Redirected to the Add New Item Page. | Pass |
| **Folder button**| When clicked the user will be redirected to the Categories Page | Clicked the button | Redirected to the Categories Page | Pass |
| **Sign Out button**| When clicked the user will be signed out and redirected to Sign In Page. The flash message 'You've been signed out' should appear | Clicked the button | Redirected to the Sign In Page. 'You've been signed out' message appeared | Pass |
| `Add New Item Page` |
|  |  |  |  |  |
| **Select Category**  | Select a category from a dropdown. This should be pre-populated with categories provided and categories created by the user. This is a required field.  |Clicked on the dropdown. The dropdown was pre-populated with categories| Selected category  |Pass  |
| **Select Category** - no category selected  | The form requires a category. When trying to save changes the user should be prompted with a tooltip to select a category.|Didn't select any category. Prompted by tooltip to select a category when tried to save changes.  |  |Pass  |
| **New List Item Input Field** | This is a required field. The new list item should have at least 3 characters. After putting the valid item name and pressing the save button the item will show on the list. The user will be redirected to My List Page and the flash message 'Added to the list' should appear. |Added New Item to the list. Directed to the My List Page. A flash message appeared | Added New Item |Pass  |
| **New List Item Input Field** - input not valid | If the input is not at least 3 characters long, the user will be prompted by a tooltip to use more characters when trying to save the form |Used only 2 characters in a new item input| Tooltip said to lengthen the text to at least 3 characters when I was trying to save the changes |Pass  |
| **New List Item Input Field** - no input | If the field is left blank, the user will be prompted by a tooltip to fill in the required field when trying to save the form |Left the field blank| Tooltip said to fill in the field when I was trying to save the changes |Pass  |
|** Details input field** (optional) | This field is optional. If the user adds details when filling out the form, they will be added to the card reveal on My List Page. |Filled the details field| Details can be seen when the to-do item card is revealed|Pass  |
| **Details input field** - invalid input | This field is optional.If the user adds details when filling out thoptional they will be added to the card optional My List Page. Used only 2 characters in a new item input| Tooltip said to fill in the field when I was trying to save the changes |Pass  |
| **Details input field** - no input | This field is optional so the user should be able to save the changes without filling it|Left the field blank| Added New Item without details|Pass  |
| **Date picker** (optional) | Once user selects a due date and saves the changes, the due date will appear on a list item card reveal. When the list item is clicked the date should be seen|Picked up the date and saved changes| Due date can be seen when clicked on the list item|Pass  |
| **Date picker** - date not selected | This field is optional so the user should be able to save the changes without filling it|Didn't select the date| Added New Item without due date|Pass  |
| **Important switch** | When the user clicks on the switch next to "Is Important" a list item will get a star icon next to it| Clicked on the switch. The added item was starred. |Pass  |
|**Cancel and Save buttons**| If the user clicks the cancel button, they will be redirected to My List Page without making any changes. After pressing the save button, the new item will be added to the list.| Clicked cancel button - redirected to My List Page with no changes. Clicked save after filling in the form - new item added to the list.|Pass  |
| `Footer` |
|  |  |  |  |  |
|  **Filter button**| When clicked the user should see a 'sort by' collapsible head. Upon clicking on it the full collapsible should display with all sorting options on it. They should be all clickable and depending on which one is clicked the user will see their items sorted alphabetically, by category or importance | Clicked the button. Clicked the button again to see all sorting options. Tried clicking them one by one. | Saw the sorting options and was able to click on them. The items were sorted accordingly. |  |
| **List button** | When clicked the user will be redirected to the My List Page. | Clicked the button | Redirected to My List Page| Pass |
| **Folder button**| When clicked the user will be redirected to the Categories Page | Clicked the button | Redirected to the Categories Page | Pass |
| **Sign Out button**| When clicked the user will be signed out and redirected to Sign In Page. The flash message 'You've been signed out' should appear | Clicked the button | Redirected to the Categories Page | Pass |
| `Edit Item Page` |
|  |  |  |  |  |
| **Select Category**  | Select a category from a dropdown. This should be pre-populated with categories provided and categories created by the user. This is a required field.  |Clicked on the dropdown. The dropdown was populated with categories    | Selected category  |Pass  |
| **Select Category** - no category selected  | The form requires a category. When trying to save changes the user should be prompted with a tooltip to select a category.|Didn't select any category. Prompted by the tooltip to select a category when trying to save changes.  |  |Pass  |
| **Edit List Item Input Field**  | This is a required field. The new list item should have at least 3 characters. After putting the valid item name and pressing the save button the item will show on the list. The user will be redirected to My List Page and the flash message 'Updated' should appear. |Added New Item to the list. Directed to the My List Page. The right flash message appeared | Added New Item |Pass  |
| **Edit List Item input field** - input not valid | If the input is not at least 3 characters long, the user will be prompted by a tooltip to use more characters when trying to save the form |Used only 2 characters in a new item input| Tooltip said to lengthen the text to at least 3 characters when I was trying to save the changes |Pass  |
|**Edit Item input field** - no input | If the field is left blank, the user will be prompted by a tooltip to fill in the required field when trying to save the form |Left the field blank| Tooltip said to fill in the field when I was trying to save the changes |Pass  ||
| **New List Item Input Field** - no input | If the field is left blank, the user will be prompted by a tooltip to fill in the required field when trying to save the form |Left the field blank| Tooltip said to fill in the field when I was trying to save the changes |Pass  |
| **Details input field** (optional) | This field is optional. If the user adds details when filling out the form, they will be added to the card reveal on My List Page. |Filled the details field| Details can be seen when the to-do item card is revealed|Pass  |
| **Details input field**- invalid input | This field is optional.If the user adds details when filling out the thoptional they will be added to the card optional My List Page. Used only 2 characters in a new item input| Tooltip said to fill in the field when I was trying to save the changes |Pass  |
| **Details input field** - no input | This field is optional so the user should be able to save the changes without filling it|Left the field blank| Added New Item without details|Pass  |
| **Date picker** (optional) | Once user selects a due date and saves the changes, the due date will appear on a list item card reveal. When the list item is clicked the date should be seen|Picked up the date and saved changes| Due date can be seen when clicked on the list item|Pass  |
| **Date picker** - date not selected | This field is optional so the user should be able to save the changes without filling it|Didn't select the date| Added New Item without due date|Pass  |
| **Important switch** | When the user clicks on the switch next to "Is Important" a list item will get a star icon next to it| Clicked on the switch. The added item was starred. |Pass  |
|**Cancel and Save buttons**| If the user clicks the cancel button, they will be redirected to My List Page without making any changes. After pressing the save button, the item will be updated to the list.| Clicked cancel button - redirected to My List Page with no changes. Clicked save after filling in the form - new changes added to the list.|Pass  |
| `Footer` |
| The same features as in Add Item Page | follow the same steps for testing | Followed the same steps | All functionality worked | Pass |
| `Categories` |
|   |   |   |   |  |
| **Add '+' button** in the heading | When the user clicks this button they should be taken to the Add Category Page| Clicked button | Redirected to the Category Page | Pass |
| **Categories cards** | When the user goes or is redirected to Categories page, they should see at least 4 categories that are provided and any categories they have created.| Clicked the Categories Page in the navbar | Saw 4 provided categories and the ones I've created | Pass |
| **Edit button on the category card** (only available for categories created by an individual user)| When the user clicks the edit button they should be directed to the Edit Category Page | Clicked the edit button | Redirected to Categories Page | Pass |
| **Edit button on the category card** - ADMIN ACCOUNT| The admin should see edit buttons on all categories cards. When the admin clicks the edit button they should be directed to the Edit Category Page | Edit buttons were available on all category cards. Clicked the edit button | Redirected to Edit Category Page | Pass |
| **Delete button on the category card** (only available for categories created by an individual user)| When the user clicks the delete button a confirmation dialog should appear asking the user if they want to delete the category with options to confirm and cancel. If confirmed the item should be removed from the list and a flash message:'Category Successfully Deleted' should appear | Clicked the delete button | The confirmation dialog appeared. After clicking ok to confirm, the category was removed from the list and the right flash message appeared | Pass |
| **Delete button on the category card** - ADMIN ACCOUNT| The admin should see edit buttons on all category cards|When the admin clicks the delete button a confirmation dialog should appear asking the user if they want to delete the category with options to confirm and cancel. If confirmed the category should be removed from the list and a flash message:'Category Successfully Deleted' should appear. The deleted category should no longer be available to the rest of the users | Clicked the delete button | The confirmation dialog appeared. After clicking ok to confirm, the category was removed from the list and the right flash message appeared. The deleteded catgory longer displayed to the users | Pass |
| `Footer` |
|  |  |  |  |  |
|  **Filter button**| When clicked the user should see a collapsible head with 'sort by' heading. Upon clicking on it the full collapsible should display with all sorting options on it. They should be all clickable and depending on which one is clicked the user will see their items sorted alphabetically,  or 'created by me first'| Clicked the button. Clicked the button again to see all sorting options. Tried clicking them one by one. | Saw the sorting options and was able to click on them. The categories were sorted accordingly. | Pass  |
|** '+' button **| When clicked the user will be redirected to the Category Page | Clicked the button | Redirected to the Add New Category Page. | Pass |
|** List button** | When clicked the user will be redirected to the My List Page. | Clicked the button | Redirected to My List Page| Pass 
| **Sign Out button**| When clicked the user will be signed out and redirected to Sign In Page. The flash message 'You've been signed out' should appear | Clicked the button | Redirected to the Categories Page | Pass |
| `Add Category` |
| **New Category input field**  | This is a required field. The new list item should have at least 3 characters. After putting the valid item name and pressing the save button the item will show on the list. The user will be redirected to My List Page and the flash message 'Added' should appear. |Added New Item to the list. Directed to the My List Page. A flash message appeared | Added New Item |Pass  |
| **New Category**- input not valid | If the input is not at least 3 characters long, the user will be prompted by a tooltip to use more characters when trying to save the form |Used only 2 characters in a new item input| Tooltip said to lengthen the text to at least 3 characters when I was trying to save the changes |Pass  |
| **New Category**- no input | If the field is left blank, the user will be prompted by a tooltip to fill in the required field when trying to save the form |Left the field blank| Tooltip said to fill in the field when I was trying to save the changes |Pass  |
| `Footer` |
|  |  |  |  |  |
|  **Filter button**| When clicked the user should see a collapsible head with a 'sort by' heading. Upon clicking on it the full collapsible should display with all sorting options on it. They should be all clickable and depending on which one is clicked the user will be redirected to My Categories Page and see their items sorted alphabetically,  or 'created by me first'| Clicked the button. Clicked the button again to see all sorting options. Tried clicking them one by one. | Saw the sorting options and was able to click on them.Redirected to My Categories Page. The categories were sorted accordingly. | Pass  |
| **List button** | When clicked the user will be redirected to the My List Page. | Clicked the button | Redirected to My List Page| Pass
| **Folder button**| When clicked the user will be redirected to the Categories Page | Clicked the button | Redirected to the Categories Page | Pass |
| **Sign Out button**| When clicked the user will be signed out and redirected to the Sign In Page. The flash message 'You've been signed out' should appear | Clicked the button | Redirected to the Categories Page | Pass |
| `Edit Category Page` |
| **Edit Category input field**  | This is a required field. The changed category name should have at least 3 characters. After putting the valid item name and pressing the save button the item will show on the list. The user will be redirected to the Categories Page and the flash message 'Category Updated' should appear. |Changed the category's name. Directed to the Categories Page. A flash message appeared: 'Category Updated!' |Pass  |
| **Edit Category - input not valid**| If the input is not at least 3 characters long, the user will be prompted by a tooltip to use more characters when trying to save the form |Used only 2 characters in a new item input| Tooltip said to lengthen the text to at least 3 characters when I was trying to save the changes |Pass  |
| **Edit Category- no input** | If the field is left blank, the user will be prompted by a tooltip to fill in the required field when trying to save the form |Left the field blank| Tooltip said to fill in the field when I was trying to save the changes |Pass  |
| `Footer` |
| The same features as in Add Category Page | follow the same steps for testing | Followed the same steps | All functionality worked | Pass |
| `404 Page` |
|   |   |   |   |   |
| **Redirection link link**| 1. Redirects the user to the My List Page(if signed in) 2. Redirects the user to Sign In Page (if the user is not signed in) | 1. Clicked link when signed it 2. Clicked the link when signed out | 1. Redirected to My List Page 2. Redirected to Sign In Page | Pass |


### CRUD Testing Focus (For methods please see ### Full Testing section)

|CRUD   | ACTION  |  RESULT |
|---|---|---|
| **CREATE** |<li>**Adding New To-Do Items**: Users can add new to-do items through a form. Each item can include details such as the item name, category, importance, due date, and additional details</li><li>**Adding New Categories**: Users have the ability to create categories</li> | PASS  |
| **READ**  | <li>**Displaying To-Do Items**: The application lists all to-do items created by the logged-in user. Users can view their tasks, along with relevant details such as category, importance, and due date</li><li>**Viewing Categories**: Users can view all categories, including those created by them and default categories provided by the application |  PASS |
| **UPDATE**  | <li> **Editing To-Do Items**: Users can edit their to-do items to update any details, including the item name, category, importance, due date, and additional details</li><li>**Modifying Categories**: Users can also edit categories to update their names |  PASS |
| **DELETE**  |<li> **Deleting To-Do Items**: Users can delete individual to-do items. Before deletion, a confirmation prompt ensures that the user does not accidentally remove an item </li><li> **Removing Categories**: Categories can be deleted. The application asks for confirmation to prevent unintentional deletion of categories</li><li>**Bulk Deletion**: Users can mark multiple to-do items as completed (or crossed out) and then opt to delete all checked items in one action</li>| PASS  |

<br>

### Database Testing

| ACTION  |   RESULT |
|---|---|
|Create a new user account and verify its presence in the user collection in MongoDB  | PASS  |
|Create a new list item to check its presence in the to_do_items collection in MongoDB  | PASS  |
|Edit a to-do list item and confirm the accurate changes in the to_do_items collection of MongoDB | PASS  |
|Mark an item as done by pressing the check button and confirm the change in  to_do_items collection (is_crossed_out: true)  | PASS  |
|Delete a list item and verify the successful removal from the to_do_items collection in MongoDB  | PASS  |
|Delete all checked items and verify their successful removal from the to_do_items collection in MongoDB   | PASS  |
|Create a new category tand check its presence in the categories collection in MongoDB   | PASS  |
|Edit a category and confirm the accurate changes in the categories collection of MongoDB  | PASS  |
|Delete a category and verify the successful removal from the categories collection in MongoDB   | PASS  |

<br>

### Code Validation

- [W3C Markup Validator](https://validator.w3.org/)

I used W3C Validator to test all HTML pages. Initially, the validator showed a few unclosed or stray tags and a nesting issue with a paragraph under <h5> tag on a landing page. The remaining errors are a result of using a Jinja template.


| PAGE  | SCREENSHOTS  |
|---|---|
| Landing Page  | ![landing page validation](./docs/landing_page_validation.png)  |
| Register  | ![registration page validation](./docs/registration_page_validation.png)   |
| Sign In  | ![sign in page validation](./docs/sign_in_page_validation.png)   |
| My List  | ![my list page validation 1](./docs/to_do_items_page_validation1.png) ![my list page validation 2](./docs/to_do_items_page_validation2.png) ![my list page validation 3](./docs/to_do_items_page_validation3.png) |
| Add New Item  |![add new item page validation 1](./docs/add_new_item_page_validation1.png) ![add new item page validation 2](./docs/add_new_item_page_validation2.png) ![add new item page validation 3](./docs/add_new_item_page_validation3.png)  |
| Edit Item  | ![edit item page validation 1](./docs/edit_item_page_validation1.png)![edit item page validation 2](./docs/edit_item_page_validation2.png)![edit item page validation 3](./docs/edit_item_page_validation3.png) ![edit item page validation 3](./docs/edit_item_page_validation3.png) ![edit item page validation 4](./docs/edit_item_page_validation4.png)|
| Categories  | ![categories page validation 1](./docs/categories_page_validation1.png) ![categories page validation 2](./docs/categories_page_validation2.png)  |
| Add Category  | ![add category page validation 1](./docs/add_category_page_validation1.png) ![add category page validation 2](./docs/add_category_page_validation2.png)  |
| Edit Category  |![edit category page validation 1](./docs/edit_category_page_validation1.png)![edit category page validation 2](./docs/edit_category_page_validation2.png)   |
| 404  | ![404 page validation 1](./docs/404_page_validation.png)  |
| 500  |![500 page validation 1](./docs/500_page_validation.png)   |

<br>

### CSS

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

I used W3C CSS Validator for the CSS. Initial results showed errors around the 'progid' property. This one is a part of the code pasted from the gradient generator. After removing that property, the only error flagged by the validator is that the property 'font-display' does not exist. It is however a valid property, which either indicates that the validation tool is outdated or does not recognise this value in the particular context it's been used in.

|  INITIAL RESULT | FINAL RESULT  |
|---|---|
|![css_validation_initial1.png](./docs/css_validation_initial1.png) ![css_validation_initial2.png](./docs/css_validation_initial2.png)  | ![css_validation_final.png](./docs/css_validation_final.png)  |

<br>

### Python and Jinja Syntax

- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/)

I have used the PEP8 CI Python Linter application to test my Python and Jinja syntax. The initial results showed a lot of white space and lines of code that were too long. After formatting the code, the validation still flagged some lines as too long. I decided to leave them in their original format as breaking them down could harm the clarity of the code.

|  INITIAL RESULT | FINAL RESULT  |
|---|---|
|![python_validation_initial.png](./docs/python_validation_initial.png)  | ![python_validation_final.png](./docs/python_validation_final.png)  |

<br>

### Lighthouse

|  PAGE | DESKTOP  | MOBILE  |
|---|---|---|
|  Landing Page | ![lighthouse landing desktop](./docs/landing_desktop.png)  | ![lighthouse landing mobile](./docs/landing_mobile.png)   |
| Register  | ![lighthouse register desktop](./docs/register_desktop.png)   | ![lighthouse register mobile](./docs/register_mobile.png)   |
| Sign In  | ![lighthouse signin desktop](./docs/sign_in_desktop.png)   | ![lighthouse signin mobile](./docs/sign_in_mobile.png)   |
| My List  |![lighthouse mylist desktop](./docs/my_list_desktop.png)   | ![lighthouse mylist mobile](./docs/my_list_mobile.png)  |
| Add New Item  | ![lighthouse add item desktop](./docs/add_item_desktop.png)  | ![lighthouse add item mobile](./docs/add_item_mobile.png)  |
| Edit Item  | ![lighthouse edit item desktop](./docs/edit_item_desktop.png)  |  ![lighthouse edit item mobile](./docs/edit_item_mobile.png)  |
| Categories  | ![lighthouse categories desktop](./docs/categories_desktop.png)  | ![lighthouse categories mobile](./docs/categories_mobile.png)  |
| Add Category  |![lighthouse add category desktop](./docs/add_category_desktop.png) |  ![lighthouse add category mobile](./docs/add_category_mobile.png) |
| Edit Category  |![lighthouse edit category desktop](./docs/edit_category_desktop.png)  | ![lighthouse edit category mobile](./docs/edit_category_mobile.png)  |