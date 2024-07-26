from django.contrib import admin
from .models import Post, Author, Tag, Comment

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

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post", "user_email")
    list_filter = ("user_name", "user_email")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
