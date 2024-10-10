from django.db import models

class TeamModel(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    inf = models.TextField()
    avatar = models.ImageField(upload_to='team/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"