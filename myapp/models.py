from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Paper(models.Model):
    CATEGORY_CHOICES = [
        ('internship', 'Internship Paper'),
        ('thesis', 'Thesis Paper'),
        ('term', 'Term Paper'),
        ('project', 'Project Paper'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    content = RichTextField(blank=True, config_name='default')
    image_url = models.URLField(max_length=500, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Guide', 'Guide'),
        ('News', 'News'),
        ('Tips', 'Tips'),
        ('Review', 'Review'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    excerpt = models.TextField()
    content = RichTextField(config_name='default')
    image_url = models.URLField(max_length=500, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Scholarship(models.Model):
    REGION_CHOICES = [
        ('asia', 'Asia'),
        ('north-america', 'North America'),
        ('south-america', 'South America'),
        ('europe', 'Europe'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    country = models.CharField(max_length=100)
    description = models.TextField()
    content = RichTextField(blank=True, config_name='default')
    image_url = models.URLField(max_length=500, blank=True)
    deadline = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
