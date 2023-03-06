from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Search(models.Model):
    query = models.CharField(max_length=250)
    
class Hall(models.Model):
    
    #Canonical Url in django
   
    def get_absolute_url(self):
        return reverse('halls:hall_list_by_category', args=[self.slug])

    # Halls name and description
    name = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='halls/%Y/%m/%d')
    short_description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'hall'
        verbose_name_plural = 'halls'
    def __str__(self):
        return self.name

    #### Step two

class Sub_Hall(models.Model):
    
    #Canonical Url in django

    def get_absolute_url(self):
        return reverse('halls:hall_detail', args=[self.id, self.slug])

    id = models.AutoField(primary_key=True)
    hall = models.ForeignKey(Hall, related_name='sub_halls', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    name2 = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=200)
    
    image = models.ImageField(upload_to='halls/%Y/%m/%d', blank=True ,null=True)
    image1 = models.ImageField(upload_to='halls/%Y/%m/%d', blank=True  ,null=True)
    image2 = models.ImageField(upload_to='halls/%Y/%m/%d', blank=True  ,null=True)
    image3 = models.ImageField(upload_to='halls/%Y/%m/%d', blank=True  ,null=True)
    image4 = models.ImageField(upload_to='halls/%Y/%m/%d', blank=True  ,null=True)
    image5 = models.ImageField(upload_to='halls/%Y/%m/%d', blank=True  ,null=True)
    image6 = models.ImageField(upload_to='halls/%Y/%m/%d', blank=True  ,null=True)
    image7 = models.ImageField(upload_to='halls/%Y/%m/%d', blank=True  ,null=True)
    available = models.BooleanField(default=True)
    # Description of  the halls
    full_description = models.TextField(blank=True)
    # others 
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'))
    def __str__(self):
        return self.name

class regista_pics(models.Model):
    name = models.TextField(max_length=3000)
    description = models.TextField(max_length=3000)
    picz = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)
    picz1 = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)
    picz2 = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)
    picz3 = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)
    picz4 = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)
    picz5 = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)
    picz6 = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)
    picz7 = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)
    picz8 = models.ImageField(upload_to='regista_pics', blank=True  ,null=True)   
    
    def __str__(self):
        return self.name

class clearancepicz(models.Model):
    id = models.AutoField(primary_key=True)
    clearpicz = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    clearpicz1 = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    clearpicz2 = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    clearpicz3 = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    clearpicz4 = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    clearpicz5 = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    clearpicz6 = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    clearpicz7 = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    clearpicz8 = models.ImageField(upload_to='clearancepicz', blank=True  ,null=True)
    name = models.TextField(max_length=1000)
    full_description = models.TextField(max_length=3000)

    def __str__(self):
        return self.name       

class how_picz(models.Model):

    name = models.TextField(max_length=1000)
    picz = models.ImageField(upload_to='howto', blank=True, null=True)
    picz1 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz2 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz3 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz4 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz5 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz6 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz7 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz8 = models.ImageField(upload_to='howto', blank=True , null=True)  
    picz9 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz10 = models.ImageField(upload_to='howto', blank=True , null=True)
    picz11 = models.ImageField(upload_to='howto', blank=True , null=True)  
    description = models.TextField(max_length=6000)
    
    
    def __str__(self):
        return self.name        


class workz(models.Model):
    foot_title = models.CharField(max_length=300)
    foot_body = models.CharField(max_length=5000)
    picz1 = models.ImageField(upload_to='work', blank=True, null=True)
    picz2 = models.ImageField(upload_to='work', blank=True, null=True)

class home_img(models.Model):
    title = models.TextField(max_length=300)
    picz = models.ImageField(upload_to='homeshit', blank=True , null=True)
    datez = models.DateTimeField(auto_now_add=True)
    header = models.TextField(max_length=800)
    story = models.TextField(max_length=10000)

    def __str__(self):
        return self.title

class about_picz_memebers(models.Model):
    name = models.TextField(max_length=700)
    picz = models.ImageField(upload_to='aboutpicz', blank=True  ,null=True) 
    about_creators = models.TextField(max_length=3000)
    
    def __str__(self):
        return self.name

class reg_ex(models.Model):
    name = models.TextField(max_length=300)
    body = models.TextField(max_length=2000)

class kgaa(models.Model):
    title = models.CharField(max_length=500, blank=False)
    concept = models.CharField(max_length=1000)
    picz = models.ImageField(upload_to='greatness_art' ,blank=False)
    price_tag = models.CharField(max_length=100)    