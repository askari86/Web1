from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import post,Category,comment

class Postadmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display=('test','author','counted_views','status','login_require','publish_date','created_date',)
    empty_value_display = '-empty-'
    list_filter=('status','author')
    summernote_fields = ('content',)
    #ordering=['-created_date']
    search_fields=['test','content']
class Commentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display=('name','post','approwed','created_date',)
    empty_value_display = '-empty-'
    list_filter=('post','approwed')
    search_fields=['name','post']
admin.site.register(post,Postadmin)
admin.site.register(Category)
admin.site.register(comment,Commentadmin)