from django.contrib import admin

from blog.models import post
@admin.register(post)
class Postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display=('test','counted_views','status','publish_date','created_date',)
    empty_value_display = '-empty-'
    list_filter=('status',)
    #ordering=['-created_date']
    search_fields=('test','content')