from django.contrib import admin
from .models import Meme # add this

class MemeAdmin(admin.ModelAdmin):  # add this
  list_display = ('name', 'caption', 'url') # add this

# Register model Meme 
admin.site.register(Meme, MemeAdmin) # add this