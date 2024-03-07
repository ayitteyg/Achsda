from django.db import models
#from django.contrib.auth.models import User
#from import_export import resources
#from django.db.models import Sum, F



# Create your models here.

mar_status = (('married', 'married'),('single', 'single'),('divorce','divorce'), ('widow(er)','widow(er)'))
class Member(models.Model):
     name = models.CharField(max_length=250, unique=False)
     contact = models.CharField(max_length=13)
     profession = models.CharField(max_length=250, unique=False)
     residence = models.CharField(max_length=250, unique=False)
     mstatus = models.CharField(choices=mar_status, default='married', max_length=10)
     def __str__(self):
        return self.name

     def get_name(self):
        for k in Member.objects.filter(id=self.id):       
            return k.name  
    
     def get_contact(self):
        for k in Member.objects.filter(id=self.id):       
            return k.contact
     
     def get_profession(self):
        for k in Member.objects.filter(id=self.id):       
            return k.profession
    
     def get_residence(self):
        for k in Member.objects.filter(id=self.id):       
            return k.residence
    
     def get_mstatus(self):
        for k in Member.objects.filter(id=self.id):       
            return k.mstatus

     
     