from django.db import models
from django.forms import widgets
from django.core.validators import validate_email
from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.core.validators import RegexValidator
from django_countries.fields import CountryField

class UserProfile(models.Model):
   # user= models.OneToOneField(User)
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    date_of_birth=models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    country = CountryField(blank_label='(select country)')
    city=models.CharField(max_length=30 ,default='kampala')
    address=models.CharField(max_length=100)
    email = models.EmailField(default='')
    password = models.CharField(max_length=30, default='' )
    confirm_password = models.CharField(max_length=30, default='')


    def __unicode__(self): 
        return self.first_name



class Admin(models.Model):
      username = models.CharField(max_length =30)
      email = models.EmailField(unique=True, blank=False, validators=[validate_email,], null=True)

      def __unicode__(self):
            return self.username

class Category(models.Model):
      name =models.CharField(max_length=50)
      slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product')
      description= models.TextField()
      is_active =models.BooleanField(default=True)
      created_at =models.DateTimeField(auto_now_add =True)
      updated_at =models.DateTimeField(auto_now =True)
      image= models.ImageField(upload_to='images/', blank=True)
      
      class Meta:
            db_table ='categories'
            ordering =['-created_at']
            verbose_name_plural ='Categories'
      def __unicode__(self):
            return self.name

class Product(models.Model):
      stock_item=models.CharField(max_length=30)
      slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product')
      brand =models.CharField(max_length=50)
      description= models.TextField()
      price= models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
      old_price= models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
      image = models.ImageField(upload_to='images/products/main')
      is_active= models.BooleanField(default=True)
      is_bestseller =models.BooleanField(default=True)
      is_featured =models.BooleanField(default=False)
      quantity =models.IntegerField()
      description=models.TextField()
      created_at =models.DateTimeField(auto_now_add =True)
      updated_at =models.DateTimeField(auto_now =True)
      categories= models.ManyToManyField(Category)
      class Meta:
            db_table= 'products'
            ordering =['-created_at']
      def __unicode__(self):
            return self.stock_item

      def sale_price(self):
            if self.old_price > self.price:
                  return self.price
            else:
                  return None


class Cart(models.Model):
      items =models.CharField(max_length=100)
      def __unicode__(self):
            return self.items

# class Images(models.Model):
#       caption = models.CharField(max_length=64, blank=True)
#       blob =ImageField(
#             upload_to='BlobStorage',
#             storage=AppEngineBlobStorage(),
#             max_length=225,
#             blank=False,
#             )
#             serving_url =models,URLf






# Create your models here.


# Create your models here.
