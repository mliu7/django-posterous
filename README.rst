Django-Posterous is a module that imports your posterous blog posts and saves them into whichever model you are currently using for your blog posts on your Django site. The usage is simple - there is just a single management command that will check for new Posterous posts on your blog and then save them into your blog. 

Installation
============
Add django-posterous to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ..,
        'django_posterous',
    )

Add django-posterous to your python path

Install Dependencies and sync your database::

    $ pip install simplejson
    $ python manage.py syncdb

Configuration 
=============
You need to configure django-posterous within your settings.py. The following variables each need to be defined so that this module knows which posterous blog to grab the entries from and where the entries should be stored. All of these variables are required and example responses are shown here::

    DJANGO_POSTEROUS_SITE_NAME = 'wiscospike'   # The site name of your posterous site (yoursitename.posterous.com)
    DJANGO_POSTEROUS_BLOG_MODULE = 'coltrane'   # The module of your django blog
    DJANGO_POSTEROUS_BLOG_MODEL = 'Entry'       # The model where the blog posts are stored
    DJANGO_POSTEROUS_TITLE_FIELD = 'title'      # The name of the title field within your blog model
    DJANGO_POSTEROUS_BODY_FIELD = 'body_html'   # The name of the field where your post will be stored
    DJANGO_POSTEROUS_DATE_FIELD = 'pub_date'    # The name of the field where the date of the post will be stored
    DJANGO_POSTEROUS_AUTHOR_FIELD = 'author'    # The name of the field where the author of the post will be stored

Possible Gotchas
----------------
This module assumes that your blog post model has a foreign key to an author. You can hard code the author of these blog posts by specifying this user in your settings.py as so::

    DJANGO_POSTEROUS_AUTHOR = Users.objects.all()[0]

If no author is specified, it defaults to the first user in your database.

Usage
=====
Django-posterous comes with a management command that fetches all public blog posts from your Posterous site, filters out any posts that have already been added to your blog, and then adds any new ones to your blog as you specified in the configuration. Using manage.py from within your blog, you can simply do the following::

    $ python manage.py get_new_posts
