from django.contrib import admin
from .models import Article

# Register your models here.
#admin.site.register(Article)


@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'email')
