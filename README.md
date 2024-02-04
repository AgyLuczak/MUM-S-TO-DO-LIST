![](./docs/responsive_pic.png)


# **MUM'S TO-DO-LIST - 3rd milestone project**


## **Introduction**

</br>

Welcome to my third milestone project: Mum's To-Do List, This is a comprehensive Flask application for managing to-do items and categories aimed at busy mums. The application uses MongoDB as its database and includes a variety of features such as user authentication, adding, editing, and deleting to-do items and categories, as well as sorting and searching functionalities.


[Visit the website here](https://mums-to-do-list-64ef2a4f0d01.herokuapp.com/)


</br>

## **UX-User Experience Design**

</br>

## **Strategy Plane**

</br>

**The business goals for the website:**

1. To offer an easy and intuitive way for users to manage their daily tasks in a more organised and efficient manner.
2. To enhance user productivity by allowing users categorise to-do items, sort items and categories and set priorities.
3. Offer personalization and flexibility by allowing the users set their own categories.
4. Provide feedback to the users in a form of flash messages making the app more user friendly.
5. Encourage regural use by ensuring the app is easy and convenient to use.
6. Provide seamless cross-device experience by ensuring the website is responive and accessible on different devices.

</br>

**User stories:**

1. As a first-time visitor, I want to easily understand the purpose of the app.
2. As a first-time visitor, I want to be able to register and sign in into my own profile.
3. As a first-time and returning visitor, I want to stay signed-in to avoid frequent log-ins , but with a clear and accessible sign-out option for when I need to securely exit my profile.
4. As a first-time and returning visitor, I want to be able to easily navigate the app. I can access all the pages easily and go back to the my list quickly. 
5. As a first-time and returning visitor, I want to be able to add,edit and delete tasks and categories.
6. As a first-time and returning visitor, I want to be able to add details and due date to my tasks.
7. As a first-time and returning visitor, I want to be able to be able to prioritise tasks.
8. As a first-time and returning visitor, I want to be able to cross-out list items that are done and remove them from the list.
9. As a first-time and returning visitor, I want to be able to sort items on my list and categories as well.
10. As a first-time and returning visitor, I want to be able to use the app easily on different devices.
11. As a first-time and returning visitor, I want to receive immediate and clear feedback through notifications or messages within the app for various interactions, such as successfully adding, editing, or deleting tasks, errors, or confirmation prompts.
12.  As a first-time and returning visitor, I want to be able to search through to-do items and categories.
13. As an administrator, I want to be able to add and delete categories.

</br>

## **Scope Plane**

</br>

In order to achieve the strategy goals, the following features are included on the website:

- A  landing page with a welcome message at the top of the Home Page stating clearly stating the purpose of the app.
- A register and sign in page. Once users are signed it they are directed to their to-do list.
- A user stays signed it for 7 days to avoid frequent log-ins. There is a sign-out option which is easily accessible on each page.
- Navbar and footer links to navigate easily between the pages. 
- Adding, editing, and deleting options for to-do items and categories. Items on the list can be crossed out when done.
- Option to add details and the due date for each task
- An option to mark list items as important to allow prioritarization
- Sorting options both for to-do items and categories.
- Materialise.css classes and media queries were used to ensure responiveness on different devices
- Flash messages informing the user items and categories were successfully added, edited or deleted. Also users see a message when an item is crossed out as done.
- 404 and 500 pages with an option to go back to the list if there is an unexpected error.
- Search Box for searching items and categories.
- Administrator account with where categories can be added or deleted.

</br>

## **Structure Plane** 

</br>

The website consists of nine pages:
- **Landing Page**
- **Register Page**
- **Sign In Page**
- **My List Page**
- **Add New Item Page**
- **Edit Item Page**
- **Categories Page**
- **Add New Category Page**
- **Edit Category Page**


The navbar recurring on each page allows users to easily move between the pages. Once signed in the user has access to the links in the footer to additionally help navigate the site. 
I used a  favicon with a check icon in the address bar for every page to make it clear to users that they are still on the same website.  I used the same background image and consisten use of colours for different sections on each page to create a certain design pattern for the website. The Landing Page contains a short welcome message, a hero image and button links to Sign In Page. If a user is not registered yet, they will see a link to the registration page. After signing in, users are directed to My List Page where they can start adding items to their list. Categories Page diplays all categories. Users cannot change the existing categories (this is restricted for the administrator), but they can add new ones and delete the ones they created. I also added a **404** and **500 Error Pages** that direct users to the Home Page in case there is a problem with a link.

## **Surface Plane**

</br>

**Colour Scheme**

![colours](./docs/color_palette.png)


The selection of colors for Mum's to-do app was made with the intention of creating a visually appealing and user-friendly for busy mothers.  I chose Purple Lighten-1 (#7E57C2) and Pink Lighten-1 (#F48FB1)  to infuse a sense of warmth, positivity, and femininity into the app's design. The addition of Pink Darken-3 (#C2185B) provides a subtle contrast and was used as a background colour for the navbar. Grey Lighten-4 (#F5F5F5) offers a clean and neutral backdrop, enhancing readability and minimizing visual distractions.  Purple (#800080) and Crimson (#DC143C) were used in forms for focus in and focus out. The background is a repeatedimage representing a figure of a mum as a superhero who multitasks on an everyday basis. This is set against a white backdrop to ensure enough contrast and clarity. 


**Typography**

I used two fonts:

*Dancing Script* for the logo

![logo_font](./docs/Dancing_Script.png)


and *Shantell Sans* for the rest of the body

![body_font](./docs/Shantell_Sans.png)


*Dancing Script* was selected for the app's name because of its elegant and handwritten style. This font gives a sense of personal touch and warmth. On the other hand, *Shantell Sans* was chosen for the app's body text due to its clean and modern appearance. This sans-serif font ensures optimal readability and a straightforward user interface, making it easy for users to manage their to-do lists efficiently. The combination of *Dancing Script* and *Shantell Sans* strikes a balance between a friendly, inviting app name and a practical, user-centric body text.

</br>




## **Skeleton Plane**

</br>

[Wireframes](./docs/Mums_to_do_list_wireframes.pdf)

The website looks slightly different from what I initially had in mind when creating the wireframes. The landing page now has an image of a mum as a superhero. 'My List' items have an additional check button which can be used to cross out a item that has been done. Additionally, there is a 'delete all checked items' button which allows the users delete all items that have been crossed out. I used icons for all the buttons rather that words like 'save' or 'cancel' as shown in the wireframes. Categories section now includes 'edit' and 'delete' buttons only for categories created by a logged-in users. The four basic categories that are displayed to every user can only be managed by the adoministrator.

</br>


## **Feautures**

- **Navigation Bar**

The navigation bar provides users with an intuitive and seamless navigation experience. It features a responsive design that adapts to both desktop and mobile devices, ensuring accessibility and ease of use for all users. Created with the Materialize CSS framework, the navigation bar highlights essential links and functionalities, including access to the user's to-do list, categories, and account management options such as signing in, registering, or signing out. 

![navbar lg](./docs/navbar_lg.png)


The navigation bar displays the app's logo and name, "Mum's To-Do List", anchored on the left side. This provides users with a consistent visual reference across the application. An icon (fa-solid fa-circle-check) next to the brand name enhances the visual appeal and is hidden on medium and smaller screens to maintain a clean look.

![navbar sm](./docs/navbar_sm.png)

A side navigation is provided for mobile users, ensuring that navigation links remain accessible on smaller devices. This mobile navigation is triggered by a hamburger menu icon.

![sidenav](./docs/sidenav.png)

The navigation bar dynamically adjusts its links based on the user's authentication state. For logged-in users, links to "My List" and "Categories" are displayed, along with an option to "Sign Out". The current page or section is highlighted with an active class, providing users with visual feedback on their current location within the app.


- **Footer**

The footer is designed to offer logged in  users additional navigation options and functionalities related to the app. It's responsive design enhances the user's experience on various devices.

![footer_lg](./docs/footer_lg.png)

![footer_sm](./docs/footer_sm.png)

It consists of:

- Filter and Sort Button:

A button is provided to trigger a collapsible element, allowing users to filter and sort their to-do list items (or categories on categories pages). This feature enhances user engagement by providing a dynamic way to view their tasks.

- Collapsible Sort Options:

Upon clicking the filter button, users are presented with a collapsible list that offers sorting options ( e.g. alphabetically, or by importance). This allows for a customized viewing experience. (For more details on searching functionality read this section...)
Each option is a link that modifies the display of the to-do list according to the selected sort method.

![footer_functionality](./docs/footer_functionality.png)

- Quick Access Icons:

Additional icons provide quick access to common tasks: adding new to-do items, managing categories, and signing out. Each action is represented by a distinct icon and is accompanied by visually hidden text for accessibility, ensuring users can navigate the app efficiently.


- **Favicon**

![favicon](./static/images/favicon-32x32.png)

The favicon features a stylized check mark centered within a vibrant pink circle. I chose the check mark as it fits in the purpose of the app. The colour choice aligns with the app's branding.


- **Landing Page**

The landing page serves as the first point of interaction for users, aimed at providing them with a clear understanding of what the app offers and how it can benefit them in their daily lives. The page starts with a welcoming and personalized heading, "Hi there, Super Mum!", immediately resonating with the target audience. Under the heading the page contains a card with a hero iage and a welcome message,
The image shows a mum portrayed as a superhero holding a to-do-list. It recognizes and celebrates the multifaceted roles and strengths of mothers. There are two versions of the welcome message – one for large screens and another for smaller displays.

![welcome-large](./docs/landing_page_lg.png)

![welcome-small](./docs/landing_page_sm.png)

 'Get Started' button encourage users to sign up and try the app.

</br>

- **Registration Page**


The registration page is simple and intuitive, ensuring a straightforward process for users. It features a clean and organized layout with clearly labeled input fields, reducing any potential confusion during the sign-up process.
Users are required to create a unique username, which must be 3-15 characters long. The input field is validated for length and character type (alphanumeric), enhancing both usability and security.

![username_exists](./docs/username_exists.png)

A password input field, also constrained to 3-15 characters and alphanumeric input, ensures that users create secure passwords.

The form includes client-side validation, ensuring that users fill out the form correctly before submission. This feature enhances user experience by providing immediate feedback on input errors. 

![register](./docs/register.png)

The form data is submitted using a POST method to the server, ensuring that user credentials are securely transmitted.

For users who already have an account, the page provides a direct link to the sign-in page. This thoughtful addition enhances user experience by facilitating easy navigation.

</br>


- **Sign-In Page**

![sign in](./docs/sign_in_page.png)

The sign-in page features a clear and concise layout, making it easy for users to understand and use.
The heading "Sign in to see your list" is straightforward and indicates the purpose of the page directly.
 Users enter their username in a field with a minimum and maximum length requirement, ensuring consistency with the registration process.
 A separate field for the password enhances security. The password is also subject to length and character type restrictions.
The form uses the POST method to submit data, which helps in keeping user credentials secure. If the username or password are incorrect the users get feedback immediately.

![icorrect user or password](./docs/incorrect_user_password.png)

If the username and the password are correct the user is taken to their To-Do-List Page. The user's username is stored in the session. Setting session.permanent = True makes the session persistent across browser sessions until explicitly logged out or session expires (session set for 7 days).

For new users, the page provides a direct link to the registration page. This addition enhances user experience by facilitating easy navigation between signing in and registering.

</br>

- **My List Page**

The My List page serves as the primary interface for users to interact with their tasks. It is designed to offer a personalized and intuitive user experience where users can view, manage, and organize their to-do list efficiently.

The page greets users with a custom message, "{{ username }}'s list", creating a personalized space. A floating action button, styled distinctly, is provided for users to quickly add new tasks to their list.

![my item btn](./docs/add_item_btn.png)


Users can interact with their to-do items, which are displayed in an attractive card layout. Each card provides a visual summary of a task, including its name, associated category, and importance status marked by a star icon.

![my list page](./docs/my_list_page.png)


A card reveal feature is incorporated, which allows users to view additional details of each task, such as the due date and specific notes, by clicking on the task name.

![card reveal](./docs/card_reveal.png)


Tasks can be marked as completed, edited, or deleted directly from the card, offering users full control over their to-do list.

![cardbuttons](./docs/card_buttons.png)

![checked item](./docs/checked_item.png)


Users can perform bulk actions, such as deleting all completed tasks, with a single click. This feature simplifies list management and improves the user experience.

![delete all items](./docs/delete_all_checked.png)


The footer contains an interactive button to  sort tasks, enabling users to customize how they view their list. Sorting options include alphabetical, by category, or by importance, allowing users to prioritize their tasks as needed.

![sorting items](./docs/sorting_items.png)

</br>

- **Add New Item Page**

The "Add New Item" allows users to insert new tasks into their to-do list. The page features a straightforward form wrapped within a Materialize CSS card panel, guiding users through the task creation process with clear input fields for task details.

![add item page](./docs/add_item.png)

A dropdown menu is provided for users to categorize their new task, helping to keep the to-do list organized. Users can choose from a list that includes categories created by them or provided in the app.

![add item page](./docs/categories_dropdown.png)

Users can enter the name of the new task, with validation rules ensuring that the input is within the specified character limits for optimal display and management. An additional text area is available for users to add more details to their tasks if they wish to do so.

The form includes a date picker for users to optionally set a due date for the task, integrating a calendar UI for easy date selection.

![calendar](./docs/calendar.png)

A switch is provided for users to mark tasks as important, visually represented by a star icon. This feature helps users prioritize their tasks.

![important](./docs/important.png)

Two large, easy-to-identify buttons offer users the option to either save the new task or cancel the operation. The save button submits the form, while the cancel button redirects users back to their list without adding the new task.

</br>

- **Edit Item Page**

The Edit Item page allows users to make changes to existing tasks. All fields in the edit form are pre-filled with the existing details of the selected task. Users can see the current information and make necessary adjustments easily.

A dropdown menu populated with available categories allows users to re-categorize tasks if needed. Categories created by the user or an admin are included.

Users can edit the name and detailed description of the task and change the due date of the task.

A switch is available to mark the task as important, which can be toggled during the edit process. 

The form provides clear options to either save changes or cancel and return to the list. This ensures users have full control over the editing process and can opt-out at any moment.

![edit_item](./docs/edit_item.png)


</br>

- **Categories Page**

This feature allows users to view, add, edit, and delete categories, providing a comprehensive toolset for category organization.
 A floating action button (+) is prominently displayed, enabling users to add new categories effortlessly. This button takes users to a dedicated form where they can enter the name of the new category.

 ![categories](./docs/categories_page.png)

There are four categories provided in the app, but users can add their own. They can also edit and delete categories they created themselves. Editing and deletion capabilities are conditionally rendered based on the user's session information, ensuring that only authorized users can modify or remove categories. Editing and deleting the original categories is resrticted to the admin account.

![ own categories](./docs/categories_own.png)


A collapsible filter button allows users to sort categories alphabetically or by those created by them first, offering enhanced navigation and personalization of the category viewing experience.

![ sort categories](./docs/sort_categories.png)


</br>

- **Add Category Page**


The "Add Category" feature enables users to create customized categories for their tasks. This functionality is designed to help users organize their tasks into meaningful groups, making task management more efficient and personalized. 

![ add category](./docs/add_category.png)


Users can easily add a new category through a simple form. This form includes an input field for the category name, ensuring a straightforward way to introduce new categories into their to-do list. The form validates user input to ensure that category names meet specific criteria (e.g., length between 3 to 20 characters).

Action buttons are provided to navigate away from the page without adding a new category or to submit the new category. 




## **Database Design**

I used a non-relational MongoDB database. The name of the database is **mums_to_do_list** and it consists of three collections:

- **categories**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | category_name | String | |
    | created_by | String | selected from **users** collection |


- **to_do_items**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | category_name | String | selected from **categories** collection |
    | to_do_item | String | |
    | item_details | String | |
    | is_important | String | |
    | due_date | String | |
    | created_by | String | |
    | is_crossed_out| Boolean | |
    

- **users**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | username | String | |
    | password | String | uses Secure Hash Algorithm (SHA) |



</br>

