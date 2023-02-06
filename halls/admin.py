from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Hall)
admin.site.register(Sub_Hall)

"""@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','active')
    list_filter = ('active',)
    list_fields = ('name','email',' body')
"""

admin.site.register(kgaa)
admin.site.register(regista_pics)
admin.site.register(clearancepicz)
admin.site.register(how_picz)
admin.site.register(workz)
admin.site.register(reg_ex)
admin.site.register(home_img)
admin.site.register(about_picz_memebers)