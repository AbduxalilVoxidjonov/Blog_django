from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text='Yangiliklar sayti')

    def test_text_content(self):
        post = Post.objects.get(pk=1)  # PK orqali olish
        self.assertEqual(post.title, 'Mavzu')
        self.assertEqual(post.text, 'Yangiliklar sayti')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu 2', text='boshqa yangiliklar')

    def test_url_exists_at_root(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template_used(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
