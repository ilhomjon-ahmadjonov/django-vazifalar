from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=150)
    mentor = models.CharField(max_length=100, verbose_name="Mentor (Ustoz)")
    duration_months = models.IntegerField(verbose_name="Davomiyligi (oy)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Kurs narxi")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Course"
        verbose_name_plural="Courses"
        db_table = "course"