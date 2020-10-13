from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='teachers/')
    description = models.TextField()

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Kurs nomi')
    short_description = models.TextField(verbose_name='Kurs haqida qisqacha malumot', max_length=100)
    image = models.ImageField(upload_to='course/')
    during = models.PositiveSmallIntegerField(verbose_name='Kurs davomiyligi', help_text='Oy')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name='Kurs narxi', help_text="ming so'm/oyiga")
    description = models.TextField(verbose_name='Kurs haqida malumot')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('course_detail', args=[str(self.id)])
