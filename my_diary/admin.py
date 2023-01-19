from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')
    search_fields = ['title', 'body']
    list_display = ('title', 'slug', 'intro', 'body')
