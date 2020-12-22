from django.db import models


# Create your models here.
class shopify(models.Model):
    hmac = models.CharField(max_length=2000)
    shop = models.CharField(max_length=2000)
    code = models.CharField(max_length=2000, default="")
    access_token = models.CharField(max_length=2000, default="")


class formdata(models.Model):
    content = models.CharField(max_length=2000)
    store = models.CharField(max_length=500, default="", editable=False)
    build_date = models.CharField(max_length=500, default="")
    edit_date = models.CharField(max_length=500, default="", null=True)
    delete_date = models.CharField(max_length=500, default="", null=True)
    update_date = models.CharField(max_length=500, default="", null=True)