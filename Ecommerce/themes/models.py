from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete')
    )
    banner = models.ImageField(upload_to='media/site/')
    caption = models.CharField(max_length=200)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title