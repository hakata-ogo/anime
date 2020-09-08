from django.db import models

# Create your models here.
class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=250)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    pub_date = models.DateField(auto_now_add=False)
    category = models.ManyToManyField(Category, related_name='post')
    description = models.TextField()

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'





    
