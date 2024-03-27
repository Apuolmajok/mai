from django.contrib import admin
from .models import Category, Customer, Product, Order, banner, Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(banner)
admin.site.register(Profile)


#mix profile info and user info 
class ProfileInline(admin.StackedInline):
    model=Profile

class UserAdmin(admin.ModelAdmin):
    model=User
    field=["username", "first_name", "last_name", "email", ]
    inlines=[ProfileInline]

#Unregister the old way
admin.site.unregister(User)

#Reregister thr new way
admin.site.register(User, UserAdmin)