from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(this):
        return f"{this.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(this):
        return f"{this.first_name} {this.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(to=Tag, related_name="posts")

    def __str__(this):
        return this.title


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, null=True, related_name="comments"
    )

    def __str__(this):
        return f"{this.user_name} Comment"
