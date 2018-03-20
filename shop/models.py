from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
        # user.post_set.all() 을 쓰지 않겠다고 설정하는 대신 Post라고 똑같이 쓸 수 있음
        # shop.models.Post.objects.filter(user=user) 는 사용 가능
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)