from django.contrib import admin
from .models import enquiry
from .models import application
from .models import payment
from .models import post

admin.site.site_header = 'Skyline University Website'


admin.site.register(enquiry)

admin.site.register(application)

admin.site.register(payment)

admin.site.register(post)

