from django.contrib import admin

from .models import Movie, Anime, Book, Software, Movie_genre


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'author')
    list_filter = (
        'create_date', 'author'
    )


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'author')
    list_filter = (
        'create_date', 'author'
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'author')
    list_filter = (
        'create_date', 'author'
    )


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'author')
    list_filter = (
        'create_date', 'author'
    )


admin.site.register(Movie_genre)
