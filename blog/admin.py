from django.contrib import admin

from blog.models import post,Category

class Postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display=('test','author','counted_views','status','publish_date','created_date',)
    empty_value_display = '-empty-'
    list_filter=('status','author')
    #ordering=['-created_date']
    search_fields=('test','content')
admin.site.register(post,Postadmin)
admin.site.register(Category)