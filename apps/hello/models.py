from django.db import models

class MyInfo(models.Model):
    name = models.CharField(max_length = 200)
    surname = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    bio = models.TextField(blank = True)
    birthday = models.DateField()
    image = models.ImageField(upload_to = 'photos',blank = True,null=True)

    def __unicode__(self):
        return '%s %s'%(self.name,self.surname)