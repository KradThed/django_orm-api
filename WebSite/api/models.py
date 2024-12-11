from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Для добавления доп. полей"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'User profile {self.user.username}'
    
class Category(models.Model):
    """Модель для постов"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name 
    
class Post(models.Model):
    """Модель поста"""

    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['published']
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    """Модель коментария"""

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return f'Коментарий от {self.author.username} на {self.post.title}'
    


