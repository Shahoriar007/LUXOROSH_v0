from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        pass
        #return reverse('product:product_list_by_category',args=[self.slug])#filter all the product in the same catagory

def image_dir_path(instance,filename):
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return '{}/{}'.format(instance.id,filename)

class Product(models.Model):
    category=models.ForeignKey(Category, related_name='category',on_delete=models.CASCADE)# A product has a one coteagory but A Catagory has may product
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,blank=True)
    discription=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to=image_dir_path,blank=True,null=True);
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)#when the product is last updated
    class Meta:
        ordering=('-created',)
        index_together=(('id','slug'))
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.stock==0:
            self.available=False
        elif self.stock>=0:
            self.available=True
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        pass 
        #return reverse('product:product_detail',kwargs={'id':self.id,'slug':self.slug})# product details page
