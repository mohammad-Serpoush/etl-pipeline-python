from django.db import models

# Create your models here.

class Social(models.Model):
    source = models.CharField(max_length=32)
    shares = models.IntegerField(null= True, blank=True)
    likes = models.IntegerField(null= True, blank=True)
    comments = models.IntegerField(null= True, blank=True)


class Thread(models.Model):
    social = models.ForeignKey(Social , related_name="socials" , on_delete=models.CASCADE)
    site_full = models.CharField(max_length=255 , null=True, blank=True)
    main_image = models.CharField(max_length=512,null= True, blank=True)
    site_section = models.CharField(max_length=255,null= True, blank=True)
    section_title = models.CharField(max_length=255,null= True, blank=True)
    url = models.CharField(max_length=512,null= True, blank=True)
    country = models.CharField(max_length=16,null= True, blank=True)
    title = models.TextField(null= True, blank=True)
    performance_score = models.IntegerField(null= True, blank=True)
    site = models.CharField(max_length=255,null= True, blank=True)
    participants_count = models.IntegerField(null= True, blank=True)
    title_full = models.TextField(null= True, blank=True)
    spam_score = models.FloatField(null= True, blank=True)
    site_type = models.CharField(max_length=64,null= True, blank=True)
    published = models.DateTimeField(null= True, blank=True)
    replies_count = models.IntegerField(null= True, blank=True)
    uuid = models.CharField(max_length=42)

    

class News(models.Model):
    uuid = models.CharField(max_length=42)
    thread = models.ForeignKey(Thread , related_name="threads" ,  on_delete=models.CASCADE)
    
