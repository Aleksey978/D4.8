user1 = User.objects.create_user('Иванов Иван Иванович')
user2 = User.objects.create_user('Петров Петр Петрович')
author1 = Author.objects.create(user=user1)
cat1 = Category.objects.create(category_name='Спорт')
cat2 = Category.objects.create(category_name='Отдых')
cat3 = Category.objects.create(category_name='Про космос')
cat4 = Category.objects.create(category_name='Политика')
post1 = Post.objects.create(author=author1, choose='AR', title='Заголовок1', text='текст статьи1')
post2 = Post.objects.create(author=author1, choose='AR', title='Заголовок2', text='текст статьи2')
post3 = Post.objects.create(author=author1, choose='NE', title='Заголовок3', text='текст статьи3')
post1.category.add(cat3, cat4)
post2.category.add(cat1, cat4)
post3.category.add(cat1, cat3)
com1 = Comment.objects.create(post=post1, user=user1, text='Тексе коментария')
com2 = Comment.objects.create(post=post2, user=user2, text='Тексе коментария2')
com3 = Comment.objects.create(post=post3, user=user2, text='Тексе коментария3')
com4 = Comment.objects.create(post=post3, user=user1, text='Тексе коментария4')
Post.like(post1)
Post.dislike(post1)
Comment.like(com3)
Comment.dislike(com3)
Author.update_rating(author1)
Author.objects.all().order_by('rating').last().user
Author.objects.all().order_by('rating').last().rating
top_post = Post.objects.all().order_by('rating').last()
data = {
    'title': top_post.title,
    'author': top_post.author.user,
    'rating': top_post.rating,
    'time_in': top_post.time_in,
    'prew': top_post.preview(),
}

comments = Comment.objects.filter(post=top_post)
comments_info = []

for comment in comments:
    comment_info = {
        'user': comment.user,
        'text': comment.text,
        'time_in': comment.time_in,
        'rating': comment.rating
    }
    comments_info.append(comment_info)

comments_info

