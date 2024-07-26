from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    list_display = ("title", "author", "date")
    list_filter = ("author", "tags", "date")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")
    list_filter = ("first_name", "last_name", "email_address")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)
    list_filter = ("caption",)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
