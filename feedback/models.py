from django.db import models

from django.contrib.auth.models import User

from slugify import slugify


class OfferModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    views_count = models.PositiveBigIntegerField(default=0)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"


class ProblemModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    views_count = models.PositiveBigIntegerField(default=0)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"



def save(self, *args, **kwargs):
    if self.slug is None:
        self.slug = slugify(self.title)

        obj = OfferModel.objects.filter(slug=self.slug)
        counter = 1
        while obj.exists():
            self.slug = f"{self.slug}-{counter}"
            counter += 1
            obj = OfferModel.objects.filter(slug=self.slug)

            super().save(*args, **kwargs)


    def __str__(self):
            return self.title

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"