from django.db import models
from django.utils.text import slugify


class PostTag(models.Model):
    title = models.CharField(max_length=20, db_index=True)
    url_title = models.CharField(max_length=20, db_index=True, null=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title
    

class Author(models.Model):
    JUNIOR = 'JR'
    SENIOR = 'SR'
    AUTHOR_LEVEL_CHOICES = [
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior')
    ]

    name = models.CharField(max_length=30)
    level = models.CharField(max_length=2, choices=AUTHOR_LEVEL_CHOICES, default=JUNIOR)
    bio = models.TextField()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(PostTag, verbose_name='Post tags', blank=True)
    is_active = models.BooleanField(default=False, verbose_name='Active')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, editable=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs): # Save function is used to save the arguments in the database.
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
