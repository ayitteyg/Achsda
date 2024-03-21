from django.db import models
#from django.contrib.auth.models import User
#from import_export import resources
#from django.db.models import Sum, F



# Create your models here.
mar_status = (('married', 'married'),('single', 'single'),('divorce','divorce'), ('widow(er)','widow(er)'))
cur_status = (('Active', 'Active'),('NonActive', 'NonActive'))
gender = (('M', 'M'),('F', 'F'))
class Member(models.Model):
     name = models.CharField(max_length=250, unique=False)
     contact = models.CharField(max_length=13)
     profession = models.CharField(max_length=250, unique=False)
     residence = models.CharField(max_length=250, unique=False)
     mstatus = models.CharField(choices=mar_status, default='married', max_length=10)
     cstatus = models.CharField(choices=cur_status, default='Active', max_length=10)
     gndr = models.CharField(choices=gender, default='M', max_length=5)
     
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
     
     def get_cstatus(self):
        for k in Member.objects.filter(id=self.id):       
            return k.cstatus
      
     def get_user(self,c):
        for k in Member.objects.filter(contact=c):       
            return k.name  
     


class Notice(models.Model):
     subject = models.CharField(max_length=50, unique=False)
     content = models.CharField(max_length=250)
     date = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
        return self.subject

     def get_subject(self):
        for k in Notice.objects.filter(id=self.id):       
            return k.subject  
    
     def get_content(self):
        for k in Notice.objects.filter(id=self.id):       
            return k.content
     
     def get_date(self):
        for k in Notice.objects.filter(id=self.id):       
            return k.date