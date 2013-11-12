from django import template
from mezzanine.blog.models import BlogPost

register = template.Library()

@register.assignment_tag
def get_featured_posts(limit=5):
    posts = BlogPost.objects.filter(blogsetting__featured=True).order_by('-publish_date')[:limit]
    return posts
