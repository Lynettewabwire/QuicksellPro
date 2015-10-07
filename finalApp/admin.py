from django.contrib import admin
from .models import UserProfile, Category, Admin, Cart, Product
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Admin)

admin.site.register(Cart)
admin.site.register(Product)

# Register your models here.
