from django.db import models
from django.contrib.auth.models import User
from django.urls import resolve


article = 'AR'
news = 'NE'


POSITIONS = [
    (article, 'статья'),
    (news, 'новость'),
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}'

    def update_rating(self):
        post_ratings = self.posts.all().aggregate(models.Sum('rating'))['rating__sum'] * 3
        comment_ratings = self.user.comment_set.all().aggregate(models.Sum('rating'))['rating__sum']
        post_comments_ratings = self.posts.aggregate(models.Sum('comment__rating'))['comment__rating__sum']

        self.rating = post_ratings + comment_ratings + post_comments_ratings
        self.save()


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    choose = models.CharField(max_length=2, choices=POSITIONS, default=article)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.title}: {self.text[:20]}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        if self.rating > 0:
            self.rating -= 1
            self.save()

    def preview(self):
        return f'{self.text[0:124]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        if self.rating > 0:
            self.rating -= 1
            self.save()
