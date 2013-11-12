from django.contrib import admin
from mezzanine.blog.models import BlogPost
from mezzanine.blog.admin import BlogPostAdmin

from disfluxdiy.blogextras.models import BlogSetting

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class BlogSettingInline(admin.StackedInline):
    model = BlogSetting
    can_delete = False
    verbose_name_plural = 'Post Settings'

# Define a new User admin
class BlogPostAdmin(BlogPostAdmin):
    inlines = (BlogSettingInline, )

# Re-register UserAdmin
admin.site.unregister(BlogPost)
admin.site.register(BlogPost, BlogPostAdmin)
