from django.db import models

# Create your models here.
class clearanceForm(models.Model):
   name = models.CharField(max_length=300, blank=False)
   reg_no = models.CharField(max_length=300, blank=False)
   email = models.EmailField(max_length=300, blank=False)
   phone = models.BigIntegerField()
   department = models.CharField(max_length=200, blank=False)
   level = models.CharField(max_length=100, blank=False) 
   school = models.CharField(max_length=500, blank=True)
class registrationForm(models.Model):
   name = models.CharField(max_length=200, blank=False)
   app_no = models.CharField(max_length=300, blank=False)
   email = models.EmailField(max_length=300, blank=False)
   phone = models.BigIntegerField()
   department = models.CharField(max_length=300)
   level = models.CharField(max_length=30, blank=False)
   school = models.CharField(max_length=500, blank=True) 

class examForm(models.Model):
   name = models.CharField(max_length=200, blank=False)
   reg_no = models.CharField(max_length=200, blank=False)
   email = models.EmailField(max_length=200, blank=False)
   phone = models.BigIntegerField()
   department = models.CharField(max_length=200, blank=False)
   description  = models.CharField(max_length=7000, blank=False) 
   school = models.CharField(max_length=500, blank=True)   

class regular_assessmentForm(models.Model):
   name =  models.CharField(max_length=300, blank=False)
   reg_no = models.CharField(max_length=200, blank=False)
   email =  models.CharField(max_length=200, blank=False)
   phone = models.BigIntegerField()
   department = models.CharField(max_length=200, blank=False)
   description = models.CharField(max_length=5000, blank=False)
   school = models.CharField(max_length=500, blank=True)

class contactz_form(models.Model):
    name = models.CharField(max_length=200, blank=False )
    email = models.EmailField(max_length=200 ,blank=False)
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=300,blank=False)
    suggestion = models.CharField(max_length=5000, blank=False)
    message = models.CharField(max_length=2000, blank=False)

class projectForm(models.Model):
   name = models.CharField(max_length=200)
   regno = models.CharField(max_length=300)
   email = models.EmailField(max_length=300)
   department = models.CharField(max_length=300)
   phone = models.BigIntegerField()
   message = models.CharField(max_length=2000)
   project_topic = models.CharField(max_length=2000)
   school = models.CharField(max_length=500, blank=True)    


class pd(models.Model):
   title = models.CharField(max_length=300, blank=True )
   body =  models.CharField(max_length=4000 , blank=True )

   def __str__(self):
      return self.title

#.................. for hot clearacnce Page .........................
class clearances_expalain(models.Model):
   title = models.CharField(max_length=100 , blank=True )
   body =  models.CharField(max_length=2000 , blank=True )

   def __str__(self):
      return self.title   

#.................. for how to's Page .............................                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
class howtoz(models.Model):
   title = models.CharField(max_length=100,  blank=True )
   body =  models.CharField(max_length=2000, blank=True )

   def __str__(self):
      return self.title 

