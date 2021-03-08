from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post


class DiaryTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        test_user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        test_post = Post.objects.create(
            author=test_user,
            title='diary title',
            content='diary content'
        )

    def test_diary_content(self):
        post = Post.objects.last()

        author = f'{post.author}'
        title = f'{post.title}'
        content = f'{post.content}'

        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'diary title')
        self.assertEqual(content, 'diary content')
