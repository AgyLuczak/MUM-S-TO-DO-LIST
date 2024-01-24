![](./docs/responsive.png)


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

The website consists of four pages:
- **Landing Page**
- **Register Page**
- **Sign In Page**
- **My List Page**
- **Categories Page**


The navbar recurring on each page allows users to easily move between the pages. Once signed in the user has access to the links in the footer to additionally help navigate the site. 
I used a  favicon with a check icon in the address bar for every page to make it clear to users that they are still on the same website.  I used the same background image and consisten use of colours for different sections on each page to create a certain design pattern for the website. The Landing Page contains a short welcome message, a hero image and button links to Sign In Page. If a user is not registered yet, they will see a link to the registration page. After signing in, users are directed to My List Page where they can start adding items to their list. Categories Page diplays all categories. Users cannot change the existing categories (this is restricted for the administrator), but they can add new ones and delete the ones they created. I also added a **404** and **500 Error Pages** that direct users to the Home Page in case there is a problem with a link.


## **Skeleton Plane**

</br>

[Wireframes](./docs/Mums_to_do_list_wireframes.pdf)

The website looks slightly different from what I initially had in mind when creating the wireframes. 



</br>

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