from django.db import models



class Student(models.Model):

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True)


    def __str__(self):
        return self.name
