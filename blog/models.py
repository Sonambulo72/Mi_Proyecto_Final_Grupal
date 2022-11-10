from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=255)
    content = models.TextField(max_length=3000)
    date_published = models.DateTimeField(auto_now_add=True)
    prize = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="posts", null=True, blank=True) #agregado para imagen
    
    def __str__(self):
        return f"id:{self.id}, title:{self.title}"

class Usuario(models.Model):
    nombre= models.CharField(max_length=20)
    email= models.CharField(max_length=100)
    contraseña= models.CharField (max_length=16)

    def __str__(self):
        return self.nombre

