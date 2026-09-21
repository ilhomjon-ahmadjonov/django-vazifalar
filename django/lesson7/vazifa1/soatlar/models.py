from django.db import models

class Watch(models.Model):
    title = models.CharField(max_length=150)
    model = models.CharField(max_length=100 )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Watch"
        verbose_name_plural = "Watches"
        db_table = "watches"