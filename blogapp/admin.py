from django.contrib import admin

from .models import categories , Post ,contactus

from django.utils.html import format_html


from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('cat_id','title' , 'description','add_date','url',)
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id' , 'title' ,'url','content',)
    search_fields=('title',),
    list_filter =('cat_id',)

admin.site.register(categories, CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(contactus)      