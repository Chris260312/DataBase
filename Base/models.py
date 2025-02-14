from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    reaction = models.IntegerField(choices=[(1, 'Лайк'), (-1, 'Дизлайк')])

    def __str__(self):
        return f"Like on {self.post.title}"

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

class Donation(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    image = models.ImageField(upload_to='donations/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Донат"
        verbose_name_plural = "Донаты"