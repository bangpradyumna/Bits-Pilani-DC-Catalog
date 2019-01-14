from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.


class Stuff(models.Model):
    title = models.CharField(max_length=250, default=None)
    publish_date = models.DateTimeField(default=timezone.now)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    magnetic_link = models.CharField(max_length=250, default=None)
    cover_img_link = models.CharField(max_length=250, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        abstract = True


# Comment on a post
class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.PROTECT, default=None, related_name='comment_on_post')
    comment_text = models.TextField(default=None)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, default=None)
    object_id = models.PositiveIntegerField(default=None)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment_text

    def reply_to_this_comment(self):
        return ReplyToComment.objects.all().filter(comment=self)


# Reply to any comment
class ReplyToComment(models.Model):
    reply_to_comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_to_comment',
                                                default=None)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply_to_comment')
    reply_text = models.TextField(default=None)


class Movie_genre(models.Model):
    genre_name = models.CharField(max_length=250)

    def __str__(self):
        return self.genre_name


class Movie(Stuff):
    movie_quality = models.CharField(max_length=250, default=None)
    movie_size = models.CharField(max_length=250, default=None)
    movie_genre = models.ManyToManyField(Movie_genre)

    def get_absolute_url(self):
        return reverse('Movies-detail', args=[str(self.id)])


class Anime(Stuff):
    anime_video_quality = models.CharField(max_length=250, default=None)
    anime_video_size = models.CharField(max_length=250, default=None)

    def get_absolute_url(self):
        return reverse('Anime-detail', args=[str(self.id)])


class Book(Stuff):
    book_formatchoices = (
        ('EPUB', 'epub'),
        ('PDF', 'pdf'),
        ('DOC', 'doc'),
    )

    book_format = models.CharField(
        max_length=250,
        choices=book_formatchoices,
        default='PDF',
    )

    book_author = models.CharField(
        max_length=250,
        default=None,
    )

    def get_absolute_url(self):
        return reverse('Books-detail', args=[str(self.id)])


class Software(Stuff):
    software_os_choices = (
        ("Windows", 'windows'),
        ("Linux", 'linux'),
        ("Mac", 'mac'),
    )

    software_os = models.CharField(
        max_length=250,
        choices=software_os_choices,
        default='Windows',
    )

    software_size = models.CharField(max_length=250, default=None)

    def get_absolute_url(self):
        return reverse('Software-detail', args=[str(self.id)])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    dc_username = models.CharField(max_length=40, default=None, blank=True, null=True)
    something = models.TextField(max_length=500, default=None, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username

    def get_user_movies(self):
        return Movie.objects.all().filter(author=self.user)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'username': self.user.username}
