from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    likes=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

    def my_slugify(self,value):
        plusText=value.replace("+", "plus")
        return slugify(plusText.replace("#", "sharp"))


    def save(self, *args, **kwargs):
        self.slug = self.my_slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        # OR  super().save(*args, **kwargs)


class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
