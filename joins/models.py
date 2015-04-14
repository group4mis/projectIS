from django.db import models

# Create your models here.

class Join(model.Model):
    username=models.charfield()
    firstname=models.charfield
    lastname=models.charfield
    email=models.emailfield

    def__unicode__(self):
    return self.username
