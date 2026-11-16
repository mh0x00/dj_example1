from django.contrib import admin
from blog.models import Post
# Register your models here.

# @admin.register(Post,two,three)  #two Method for adding


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-null-'
    # fields = ["name", "title"]
    list_display = ['title', 'counted_view', 'status', 'published_date']
    list_filter = ('status',)
    # ordering = ['-created_date']
    # ordering = ['created_date']
    search_fields=['title','content']


admin.site.register(Post,PostAdmin)
