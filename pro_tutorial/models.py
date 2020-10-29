from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200, verbose_name="O\'qtuvchi Ismi:", unique=True)
    teacher_info = models.TextField(verbose_name="O\'qtuvchi haqida:")
    teacher_image = models.ImageField(upload_to="teacher/", blank=True, null=True, verbose_name='Rasm:')
    

    class Meta:
        ordering = ['teacher_name']
        verbose_name = "O\'qituvchi"
        verbose_name_plural = "O\'qituvchilar"

    def __str__(self):
        return self.teacher_name
   

class ProCourseName(models.Model):
    pro_course_image       = models.ImageField(upload_to="pro_course/%Y/%m/%d/", blank=True, null=True, verbose_name='Kurs Rasmi:',)
    pro_course_name        = models.CharField(max_length=200, verbose_name="Kurs Nomi:", unique=True)
    pro_course_description = models.TextField(verbose_name="Kurs Tarifi:")

    class Meta:
        ordering            = ['pro_course_name']
        verbose_name        = "Kurs"
        verbose_name_plural = "Kurslar"
    
    def __str__(self):
        return self.pro_course_name

class ProCourseInfo(models.Model):
    course_name        = models.ForeignKey(ProCourseName, on_delete=models.CASCADE, related_name="payed_course_name", verbose_name="Kurs Nomi:")
    course_teacher     = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL, related_name='teacher_course', verbose_name="Kurs O\'tuvchisi:")
    course_coast       = models.CharField(max_length=200, verbose_name="Kurs Narxi:", blank=True, null=True)
    course_duration    = models.CharField(max_length=300, blank=True, null=True, verbose_name="Kurs Davomiyligi:")
    course_description = models.TextField(verbose_name="Kurs Xaqida:")
    course_published   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['course_published']
        verbose_name        = 'Kurs Haqida'
        verbose_name_plural = 'Kurslar Haqida'

    def __str__(self):
        return f"{self.course_name}"


class Pupil(models.Model):
    pupil_name        = models.CharField(max_length=150, verbose_name="O\'quvchi Ismi:")
    pupil_phonenumber = models.CharField(max_length=13, verbose_name="Tel Raqami:", unique=True)
    pupil_email       = models.EmailField(max_length=100, verbose_name="Email:", blank=True, null=True, unique=True)
    join_date         = models.DateTimeField(auto_now_add=True, verbose_name="Ariza Sanasi:")

    teacher_name = models.ForeignKey(Teacher, related_name='teacher', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="O\'qtuvchi Ismi:")
    course_name  = models.ForeignKey(ProCourseName, related_name='course', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Kurs Nomi:")

    pupil_image   = models.ImageField(upload_to="pupil_image/%Y/%m/%d/", blank=True, null=True, verbose_name='O\'quvchi Rasmi:',)
    pupil_comment = models.TextField(verbose_name="Izox:", blank=True, null=True,)
    
    pupil_male   = models.BooleanField(default=False)
    pupil_female = models.BooleanField(default=False)

    class Meta:
        # abstract            = True
        ordering            = ["course_name"]
        verbose_name_plural = 'O\'quvchilar'

    def __str__(self):
        return f"{self.course_name}"
    @property
    def image_url(self):
        if self.pupil_image and hasattr(self.pupil_image, 'url'):
            return self.pupil_image.url
