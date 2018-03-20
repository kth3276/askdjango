# blog/models.py
import re
from django.forms import ValidationError
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
# from imagekit.models import ImageSpecField
# from imagekit.processors import Thumbnail


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')  # 예외 발생


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    # author = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.')  # 길이 제한이 있는 문자열
    # choices = (
    #     ('제목1', '제목1 레이블'),  # 저장될 값, UI에 보여질 레이블
    #     ('제목2', '제목2 레이블'),
    #     ('제목3', '제목3 레이블'),
    # )
    content = models.TextField(verbose_name='내용')  # 길이 제한이 없는 문자열
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d')
    # post_detail.html에서 직접 처리해줌
    # photo_thumbnail = ImageSpecField(source='photo',
    #         processors=[Thumbnail(300, 300)],
    #         format='JPEG',
    #         options={'quality': 60})
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
        validators=[lnglat_validator],  # 함수 호출이 아닌 함수 자체 넘김
        blank=True, help_text='위도/경도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True) # 문자열로 지정 가능(현재 Tag 클래스가 더 밑에 있기 때문), 블랭크 옵션은 필수 항목인지 아닌지
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

# Create, Update가 성공시 넘어가는 url
    def get_absolute_url(self):
        return reverse('blog:post_detail', args={self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
