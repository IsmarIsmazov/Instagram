from django.db import models
from users.models import User





class Post(models.Model):
    image = models.ImageField(default=True,
                              upload_to="media",
                              blank=True,
                              verbose_name="Изображение"
                              )
    description = models.TextField(max_length=100,
                                   verbose_name="Описание",
                                   )
    hashtags = models.CharField(max_length=20,
                                verbose_name="Хештег",
                                )
    date = models.DateTimeField(auto_now=True,
                                verbose_name="Дата создания"
                                )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="Автор",
                               max_length=20)


    def __str__(self):
        return str(self.image)




class Likes(models.Model):
    post = models.ForeignKey("media_part.Post",
                             on_delete=models.CASCADE,
                             verbose_name="Пост",
                             )
    username = models.ForeignKey("users.User",
                                 unique=True,
                                 on_delete=models.CASCADE,
                                 verbose_name="Автор",
                                 )


    def __str__(self):
        return f"Пользователю: {self.username} понравилась ваша публикация {self.post}"



