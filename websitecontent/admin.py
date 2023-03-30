from django.contrib import admin
from websitecontent.models import Blogs

class BlogsAdmin(admin.ModelAdmin):
	list_display = ('name', 'author', 'topictype')
	search_fields = ('name',)

# Register your models here.
admin.site.register(Blogs, BlogsAdmin)