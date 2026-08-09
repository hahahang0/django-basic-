from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True,null=False,default=18)
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    email = models.EmailField()
    YEAR_CHOICES = [
    ("FR", "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ] 
    year = models.CharField(
        max_length=2,
        choices=YEAR_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True,blank=True)

    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE
    )
    class Meta:
        ordering = ["name"] #here (-) use minus sign for descending orders.
        db_table = "students"

    def __str__(self):
        return self.name;