from django.db import models

# Create your models here.
class Blog(models.Model):
    headline = models.CharField()
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline


    # author_email = models.modelfield(
    # null=true, makes a column optional, Database-specific feature
    # default="any_author@gmail.com", the fixed data that is used when the input is not provided
    # blank=true, form specific
    # unique=true, if true, provision of the same data twice is unacceptable
    # max_length=10, enforces the maximum number of characters
    # choices={"test@gmail.com": "author test email"}
    # )