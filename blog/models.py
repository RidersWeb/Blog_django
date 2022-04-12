from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    description = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    author = models.CharField(max_length=50, default='Admin')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
