from django.contrib import admin
from masterdata.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'review', 'rating')
admin.site.register(Movie, MovieAdmin)

