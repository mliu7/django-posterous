from django.db import models

class BlogPost(models.Model):
    """ Keeps track of which blog posts have already been imported
        from the Posterous site 
    """
    posterous_id = models.IntegerField()
