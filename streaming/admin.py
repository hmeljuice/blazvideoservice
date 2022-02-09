# from django.contrib import admin
# from .models import Video
#
# # Register your models here.
# admin.site.register(Video)


from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import Video

@admin.register(Video)
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
