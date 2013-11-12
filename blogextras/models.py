from django.db import models
from mezzanine.blog.models import BlogPost


class BlogSetting(models.Model):
    blog_post = models.OneToOneField(BlogPost)
    featured = models.BooleanField(default=False)
