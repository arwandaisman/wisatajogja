from django.db import models  
class Admin(models.Model):  
    id_admin = models.CharField(max_length=20,null=True,blank=False)
    nama_admin = models.CharField(max_length=100,null=True,blank=False)  
    email_admin = models.EmailField(null=True,blank=False)  
    no_hp_admin = models.CharField(max_length=15,null=True,blank=False)  
