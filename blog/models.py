from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'https://blog-image-ngcxy.s3.amazonaws.com/posts/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    # deploy a manager to filter out the published posts
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        # ('private', 'Private'),
    )

    # protect the category from being deleted
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.PNG')
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager, return single one
    postobjects = PostObjects()  # our custom manager, return all published one

    class Meta:
        ordering = ('-published',)  # published time, in descending order

    def __str__(self):
        return self.title
