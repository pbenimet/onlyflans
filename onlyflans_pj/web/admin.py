from django.contrib import admin
from .models import Flan, ContactForm, ContactFormModelForm

# Register your models here.

admin.site.register(Flan)
admin.site.register(ContactForm)
admin.site.register(ContactFormModelForm)