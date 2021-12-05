from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import CustomUser
from accounts.forms import *
# Register your models here.
class SellerAdditionalInline(admin.TabularInline):
    model = serviceProvider
class SellerAdmin(admin.ModelAdmin):
    inlines = (
        SellerAdditionalInline,
    )
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','is_active','is_staff',)
    list_filter = ('email','is_active','is_staff',)

    fieldsets = (
        (None, {
            "fields": (
                'email','phone','type','password',
            ),
        }),
        ('permissions', {
            "fields": (
                'is_staff','is_active',
            ),
    }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('email','phone','type','password1','password2','is_staff','is_serviceProvider','is_serviceBusiness','is_active',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    


    
    



admin.site.register(customer)
admin.site.register(serviceProvider)
admin.site.register(sellerPost)
admin.site.register(seller,SellerAdmin)
admin.site.register(buyer)
admin.site.register(CustomUser,CustomUserAdmin)