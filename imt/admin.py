from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(pd)
admin.site.register(contact_info)
# for  hot  clearance 
admin.site.register(clearances_expalain)
# for   how to's 
admin.site.register(howtoz)

# all forms 
admin.site.register(examForm)
admin.site.register(registrationForm)
admin.site.register(clearanceForm)
admin.site.register(regular_assessmentForm)
admin.site.register(projectForm)
