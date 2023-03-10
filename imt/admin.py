from django.contrib import admin
from .models import *
from .forms import *


# Register your models here.
admin.site.register(pd)
# for  hot  clearance 
admin.site.register(clearances_expalain)
# for   how to's 
admin.site.register(howtoz)

# all forms 
@admin.register(regular_assessmentForm)
class regular_assessmentFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'reg_no', 'phone','school')
    list_filter = ('name', 'reg_no', 'email')
    search_fields = ('name', 'email', 'phone')

@admin.register(examForm)
class examFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'reg_no', 'phone','school')
    list_filter = ('name', 'reg_no', 'email')
    search_fields = ('name', 'email', 'phone')


@admin.register(registrationForm)
class registrationFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',  'phone','school')
    list_filter = ('name',  'phone', 'email')
    search_fields = ('name', 'email', 'phone')


@admin.register(clearanceForm)
class clearanceFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',  'phone','school')
    list_filter = ('name',  'phone', 'email')
    search_fields = ('name', 'email', 'phone')


@admin.register(contactz_form)
class contactz_formAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',  'phone')
    search_fields = ('name', 'email', 'phone')


@admin.register(projectForm)
class projectFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',  'phone')
    list_filter = ('name',  'phone', 'email')
    search_fields = ('name', 'email', 'phone')

