from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import User


class PostTests(TestCase):

    def setUp(self):
        me = User.objects.create(username='James')
        Post.objects.create(author=me, title= "Sample Test", text='just a test')

    def test_text_content(self):
        post = Post.objects.get(title="Sample Test")
        expected_object_name = f'{post.text}'
        self.assertEquals(expected_object_name, 'just a test')

    def test_post_index_view(self):
        response = self.client.get(reverse('post_index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_index.html')