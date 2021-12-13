from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import CustomUser
from accounts.forms import *
# Register your models here.
admin.site.site_header = "Ume administration"
admin.site.site_title = "Ume administration"
admin.site.index_title = "Welcome to Ume administration"
class SellerAdditionalInline(admin.TabularInline):
    model = serviceProviderDetails
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
    


    
    
admin.site.register(serviceProviderDetails)
admin.site.register(ServiceProvider,SellerAdmin)
admin.site.register(customer)
admin.site.register(CustomUser,CustomUserAdmin)