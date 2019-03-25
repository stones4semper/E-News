from django.db import models
from django.urls import reverse
from django.utils import timezone
from  django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django_mysql.models import EnumField

CATERGORY_CHOICES = (
    ('World', 'World'),
    ('Naija', 'Naija'),
    ('Technology', 'Technology'),
    ('Design', 'Design'),
    ('Culture', 'Culture'),
    ('Business', 'Business'),
    ('Politics', 'Politics'),
    ('Opinion', 'Opinion'),
    ('Science', 'Science'),
    ('Health', 'Health'),
    ('Style', 'Style'),
    ('Travels', 'Travels'),
)
 
class Category(models.Model):
    CatName = EnumField(choices=['World', 'Naija', 'Technology', 'Design', 'Culture', 'Business', 'Politics', 'Opinion', 'Science', 'Health', 'Style', 'Travels'])

class Posts(models.Model):

    title = models.CharField(max_length=100)
    # deyCategory = models.ForeignKey(Category, default="1", on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='blog_pics')
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog-details", kwargs={"pk": self.id})
    
 