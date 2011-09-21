from django.db import models

class BlogPost(models.Model):
    """ Keeps track of which blog posts have already been imported
        from the Posterous site 
    """
    posterous_id = models.IntegerField()

    def __unicode__(self):
        return 'Posterous Post #{0}'.format(self.posterous_id)
