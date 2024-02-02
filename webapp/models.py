from django.db import models
from django.utils import timezone

class Laptop(models.Model):
    images = models.ImageField(upload_to='image/')
    brand = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, blank=True)
    processor = models.CharField(max_length=50, blank=True)
    ram = models.CharField(max_length=50, blank=True)
    storage = models.CharField(max_length=50, blank=True)
    graphics = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=50, unique=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Create Classification
        if self.price and int(self.price) <= 15000:
            classification_type = 'Budget-Friendly'
        elif 15000 < int(self.price) <= 30000:
            classification_type = 'Mid-Range'
        else:
            classification_type = 'High-End'

        # Check if a Classification already exists for this Laptop
        classification, created = Classification.objects.get_or_create(
            laptop=self,
            defaults={'classification_type': classification_type}
        )

        # If Classification already exists, update the classification_type
        if not created:
            classification.classification_type = classification_type
            classification.save()

    def __str__(self):
        return self.brand

class Classification(models.Model):
    laptop = models.OneToOneField(Laptop, on_delete=models.CASCADE, to_field='price')
    classification_type = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return f"{self.laptop.brand} {self.laptop.model} - {self.price_range}"
    
class IDE(models.Model):
    images = models.ImageField(upload_to='ide/', blank=True)
    IDE = models.CharField(max_length=50, null=True)
    Languages = models.TextField(null=True)
    Description = models.TextField(blank=True)
    Features = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.IDE

class Programming_Language(models.Model):
    images = models.ImageField(upload_to='language/', blank=True)
    language = models.CharField(max_length=50, null=True)
    Description = models.TextField(blank=True)
    advantage = models.TextField(blank=True)
    disadvantage = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.language

class Framework(models.Model):
    images = models.ImageField(upload_to='framework/', blank=True)
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    version = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Frontend_Stack(models.Model):
    images = models.ImageField(upload_to='frontend/', blank=True)
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    version = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Contact(models.Model):
    fullname = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    mobile = models.IntegerField(blank=True)
    message = models.TextField(blank=True)
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname