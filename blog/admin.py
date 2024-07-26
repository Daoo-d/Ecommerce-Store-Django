from django.contrib import admin
from .models import Post,Author,Tag

class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author",)


# Register your models here.
admin.site.register(Post,AdminPost)
admin.site.register(Author)
admin.site.register(Tag)