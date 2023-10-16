from django.contrib import admin
from .models import Game, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin (SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'username', 'game', 'created_on')
    search_fields = ['title', 'game', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')   
    summernote_fields = ('content')


# Register your models here.
admin.site.register(Game)
