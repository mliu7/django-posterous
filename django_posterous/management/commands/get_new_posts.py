import simplejson
import urllib2
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import get_model

from django_posterous.models import BlogPost

class Command(BaseCommand):
    def handle(self, *args, **options):
        site_name = settings.DJANGO_POSTEROUS_SITE_NAME
        module = settings.DJANGO_POSTEROUS_BLOG_MODULE
        model = settings.DJANGO_POSTEROUS_BLOG_MODEL
        title_field = settings.DJANGO_POSTEROUS_TITLE_FIELD
        body_field = settings.DJANGO_POSTEROUS_BODY_FIELD
        date_field = settings.DJANGO_POSTEROUS_DATE_FIELD
        author_field = settings.DJANGO_POSTEROUS_AUTHOR_FIELD
        author_field_id = author_field + '_id'
        try:
            slug_field = settings.DJANGO_POSTEROUS_SLUG_FIELD
        except:
            slug_field = None
        author = None

        # Get all of the blog posts. Posterous limits you to 10 posts per API call, hence the loop
        posts = []
        page_number = 1
        while 1:
            # Call the posterous API to get 10 posts
            result = simplejson.loads(urllib2.urlopen('http://posterous.com/api/2/sites/{0}/posts/public?page={1}'.format(site_name, page_number)).read())
            if result:
                posts = posts + result
                page_number += 1
            else:
                break

        # Get the model to store the blog post in
        PostModel = get_model(module, model)

        for post in posts:
            # Ensure that this post has not already been saved to the blog
            if not BlogPost.objects.filter(posterous_id=post['id']).exists():

                # Get author for the post if it was not specified in the settings file
                if not author:
                    author = User.objects.all().order_by('id')[0]

                # create a new post
                new_post = PostModel()
                new_post.__dict__[title_field] = post['title']
                new_post.__dict__[body_field] = post['body_full']
                date_string = " ".join(post['display_date'].split()[0:2])
                date = datetime.strptime(date_string, '%Y/%m/%d %H:%M:%S')
                new_post.__dict__[date_field] = date
                new_post.__dict__[author_field] = author
                new_post.__dict__[author_field_id] = author.id
                if slug_field:
                    new_post.__dict__[slug_field] = post['slug']
                new_post.save()
            
                # Save this id in the database so it is not loaded again
                blog_post = BlogPost(posterous_id=post['id'])
                blog_post.save()
