from django.db import models
from phone_field import PhoneField



class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['desc','price']
 
    def __str__(self):
           return self.desc
    

class Customers(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Phone = models.BigIntegerField(null=True) 
    #PhoneField(blank=True, null=True, help_text='Contact phone number')
    Address = models.CharField(max_length=50,null=True,blank=True)
    Email = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=False,blank=False,default='/placeholder.png')

    fields =['Name','Phone','Address','Email','image']
 

    def __str__(self):
           return self.Name + ' ' + str(self.id)
