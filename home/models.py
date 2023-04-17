from django.db import models




# Create your models here.


    
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class Courier(models.Model):
    Sname = models.CharField(max_length=122) 
    Sphone = models.CharField(max_length=12)
    pick = models.CharField(max_length=122)
    Rname = models.CharField(max_length=122)
    Rphone = models.CharField(max_length=12)
    drop = models.CharField(max_length=122)
    package = models.CharField(max_length=122) 
    date = models.DateField()

    def __str__(self):
        return self.Sname

    


class Orders(models.Model):
    name = models.CharField(max_length=122) 
    phone = models.CharField(max_length=12)
    product= models.CharField(max_length=122)
    Quantity = models.CharField(max_length=122)
    details = models.CharField(max_length=122)
    Address = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    


class Reserve (models.Model):
    name = models.CharField(max_length=122) 
    email = models.CharField(max_length=12)
    plan = models.CharField(max_length=122)
    occasion = models.CharField(max_length=122)
    Address = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

    

    