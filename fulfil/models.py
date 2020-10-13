from django.db import models



class English(models.Model):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    telefon_raqam = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)


    def __str__(self):
        return self.ism
    

class Smm_course(models.Model):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    telefon_raqam = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)


    def __str__(self):
        return self.ism


class Frontend(models.Model):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    telefon_raqam = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)


    def __str__(self):
        return self.ism   


class Backend(models.Model):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    telefon_raqam = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)


    def __str__(self):
        return self.ism   


class Python(models.Model):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    telefon_raqam = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)


    def __str__(self):
        return self.ism    


class Android(models.Model):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    telefon_raqam = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)


    def __str__(self):
        return self.ism  