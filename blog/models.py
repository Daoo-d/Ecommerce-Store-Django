from django.db import models

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length = 50,null=True)
    last_name = models.CharField(max_length = 50,null=True)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(null=True)
    date = models.DateField(auto_now_add=True)
    excerpt = models.TextField()
    content = models.TextField()
    quote = models.TextField(null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField(unique = True ,null=False)
    tag = models.ManyToManyField(Tag, blank= True)

    def __str__(self) :
        return f"{self.title}  ({self.date})"
    
class Comments(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    post = models.ForeignKey(Post,on_delete = models.CASCADE ,related_name="com_ments")