from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering=['name']

class Marvel(models.Model):
    category =models.ForeignKey(Category,on_delete=models.CASCADE,related_name='cg',null=True,blank=True)
    # user = models.ForeignKey (User ,on_delete=models.SET_NULL,null=True,blank=True)
    movie_name= models.CharField(max_length=100)
    movies_img =models.ImageField(upload_to="movies_img")
    movies =models.FileField(upload_to="movies")

    def __str__(self) -> str:
        return self.movie_name
