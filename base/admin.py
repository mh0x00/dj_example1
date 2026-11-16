from django.contrib import admin
from base.models import Contact
# Register your models here.

# @admin.register(Contact)      #two Method for adding


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-null-'
    search_fields = ['name', 'email']
    list_display = ['name', 'created_date', 'subject', 'email']
    list_filter = ('name', 'email', 'message', 'subject')


admin.site.register(Contact, ContactAdmin)
