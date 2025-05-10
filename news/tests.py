from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text='Yangiliklar sayti', author='<NAME>')

    def test_text_content(self):
        post = Post.objects.get(pk=1)  # PK orqali olish
        self.assertEqual(post.title, 'Mavzu')
        self.assertEqual(post.text, 'Yangiliklar sayti')
        self.assertEqual(post.author, 'Abduxalil')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu 2', text='boshqa yangiliklar', author='Abduxalil')

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
