from django.contrib import admin
from .models import Game, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin (SummernoteModelAdmin):
    summernote_fields = ('content')


# Register your models here.
admin.site.register(Game)
