from django.db import models

# Create your models here.



class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=13)
    email=models.EmailField(max_length=100)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return 'Message From '+self.name +'  -  '+self.email


class Record3(models.Model):
    uid=models.IntegerField()
    name=models.CharField(max_length=250,default='')
    
    email=models.EmailField( max_length=254,default='')
    timestamp=models.DateTimeField(auto_now=True,blank=True)
    result=models.CharField(max_length=50,default='')
    def __str__(self):
        return self.name+'   -     '+' User ID : '+str(self.uid)

    

     