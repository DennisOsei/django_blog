from django.test import TestCase
from django.http import HttpResponse
from django.urls import reverse


class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)
    
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("post_index"))
        self.assertEquals(response.status_code, 200)

    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("post_index"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_index.html")
   

