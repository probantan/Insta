    Insta
===================
## Description
```Insta``` is a clone of instagram app (https://instagram.com), where users can post  pics, like , comment and follow each other.

------------------------------------------------------------------------

## User Requirements

1. Sign in to the application to start using.
2. Upload  pictures to the application.
3. See my profile with all my pictures.
5. Like a picture and leave a comment on it.

## Features

+ [x] public user profiles
+ [x] Photo feed displaying user photos along with those users follows.
+ [x] Image editing: Filter, rotate and add caption to images during upload
+ [x] search functionality for users.
+ [x] Django admin dashboard for adding & managing posts and user accounts
+ [x] SSL encryption using letsencrypt and certbot


## Getting started




### Cloning the repository
```bash
git clone git@github.com:probantan/Insta.git && cd Instagram
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```


### Database migrations

```bash
python manage.py migrate
```

### Running the server 
```bash
python manage.py runserver
```

### Admin Dashboard
Use django admin to manage the different users and posts.

### Deploying to heroku
Refer to this guide: [deploying to heroku by Ben](https://gist.github.com/Benard18/01e28cfbd911f87c7df8ee33cbdaa593)

## Running the tests
```bash
python manage.py test
```




## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## TODO 
### if i get the time to continue working on this
+ [ ] Image editing and deleting after upload
+ [ ] Block feature
+ [ ] Push notifications
+ [ ] Private messaging
+ [ ] User and Location tagging
+ [ ] Text & drawing tools
+ [ ] Double tap (i know its a just a time settings code if i get time i will add it)
+ [ ] Add inbuilt commment app synced with userprofiles
+ [ ] Ajax search functionality displaying users suggestion with keydown.
+ [ ] Direct & Group messaging
+ [ ] private profile

## Contributing

- Git clone [https://github.com/jakhax/insta-clonewars.git](https://github.com/jakhax/insta-clonewars.git) 
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Jack ogina](https://github.com/jakhax)