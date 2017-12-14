# Share Respite Website

- Hosted Link: https://share-respite.herokuapp.com/
- Github Link: https://github.com/callump5/share_respite_prj
- Share's Current Site Link: http://sharerespite.co.uk/


## Overview
### What is this app for?
This website is being designed for a charity that helps to look after disabled children. I hope to improve their current
website, also i wish to bring in features like a forum to make it easier for parents to communicate and talk about issues
that others may relate to.

### How to use the app
As this is mainly a user driven site, if you was to not make an account you wouldnt be able to see/use all the features
available.

As this is my course work and i want all features to be avaiable i made a user with superuser access:
- Username: CodeInstitute
- Password: coursework

#### Non-User
- Can access **Forum** and view **Threads**
- Can access **About Us** pages
- Can access **Contact Us** 
- Can Donate to Share via **Stripe**

#### User
- Can access **Profile** page; shows all owned **Threads** and **Testimonials**, the icons allow you to view, edit and delete
- Can create **Testimonials**
- Can create **Threads** and **Comments** on **Forum** page

#### Staff, SuperUser
- **Profile** page now includes all **Forum Subjects**
- Can access **Donations** page, includes graph of recent donations and a data table
- Can access **Admin** page from **Profile** page
    - Use **Admin** page to add/edit/delete **Whats-On** content
    - Use **Admin** page to add/edit/delete **Staff Gallery** images
    - Use **Admin** page to give staff status to users and 
    - Use **Admin** page to add/edit/delete All other content created by users/staff
- Can create **Forum Subjects**

## Features
### Existing Features
- Forum
- Testimonials
- Donations
- Staff Gallery
	- uploading images on local and hosted site works. Apart from when heroku puts the app into sleep mode when the site is inactive; then the images are deleted as they are not stored (I believe this is a problem with my current subscription option being the free one)
- Map

## Tech Used

### Some the tech used includes:
- [Bootstrap](http://getbootstrap.com/)
	- We use **Bootstrap** to give our project a simple, responsive layout
- [Django](https://www.djangoproject.com/)
	- We use **Bootstrap** to give our project a simple, responsive layout
- [Dc](https://dc-js.github.io/dc.js/)
    - Used for dimensional charting 
- [D3](https://d3js.org/)
    - Used for manipulating documents based on data
- [Crossfilter](http://square.github.io/crossfilter/)
    - Used for exploring large multivariate datasets in the browser.
- [Stripe](https://stripe.com/gb)
    - used for taking one off donations
 
	
## Contributing
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. Make sure all dependicies in requirements.txt are all installed
3. Finally run ```python manage.py migrate settings=settings.staging``` in the terminal then you can start working on the project!
