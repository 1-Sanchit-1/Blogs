from django.db import models
# from tinymce.models import HTMLField
# Create your models here.



class categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=1000)
    description=models.TextField()
    url=models.CharField(max_length=50)
    image=models.ImageField(upload_to ='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    
    def __str__(self):
        return self.title
    
  

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    url=models.CharField(max_length=50)
    cat=models.ForeignKey(categories,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')

     
    def __str__(self):
        return self.title


    
class contactus(models.Model):
    first_name = models.CharField(max_length = 200) 
    last_name = models.CharField(max_length = 200) 
    email = models.EmailField() 
    subject=models.CharField(max_length=1000) 
    Message=models.CharField(max_length=5000) 


    class Meta:
        verbose_name = ("Contact-form")

    def __str__(self):
        return self.first_name + " " + self.last_name
