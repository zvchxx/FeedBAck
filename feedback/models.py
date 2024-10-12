from django.db import models

from django.contrib.auth.models import User

from slugify import slugify


class OfferModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=64)
    views_count = models.PositiveBigIntegerField(default=0)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"


class ProblemModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=64)
    views_count = models.PositiveBigIntegerField(default=0)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"