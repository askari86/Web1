#makemigrations و migrate
from django.db import models

# Create your models here.
class post(models.Model):
    #image
    #author
    test=models.CharField(max_length=255)
    content=models.TextField()
    #tag
    #category
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    publish_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} {}'.format(self.test,self.id)
    def increment_view_count(self):
        self.counted_view += 1
        self.save()
    class Meta:
        ordering=['-created_date']