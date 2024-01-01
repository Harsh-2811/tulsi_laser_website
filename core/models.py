from functools import update_wrapper
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import EmailField
from django.utils import timezone
from PIL import Image

class Company(models.Model):
    company_name=models.CharField(max_length=50)
    logo_small=models.ImageField(upload_to='uploads/company/',null=True,blank=True)
    logo_big=models.ImageField(upload_to='uploads/company/',null=True,blank=True)
    favicon_icon=models.ImageField(upload_to='uploads/company/',null=True,blank=True)
    contact_number1=models.CharField(max_length=15)
    contact_number2=models.CharField(max_length=15,null=True,blank=True)
    email=models.EmailField( max_length=254,null=True,blank=True)
    address_line1=models.CharField(max_length=50,null=True,blank=True)
    address_line2=models.CharField(max_length=50,null=True,blank=True)
    address_line3=models.CharField(max_length=50,null=True,blank=True)
    map_location=models.TextField(null=True,blank=True)
    map_address_written=models.CharField(max_length=100,null=True,blank=True)
    fb_link=models.CharField(max_length=50,null=True,blank=True)
    insta_link=models.CharField(max_length=50,null=True,blank=True)
    twitter_link=models.CharField(max_length=50,null=True,blank=True)
    establishment_year=models.CharField(max_length=4)
    GSTIN=models.CharField(max_length=20,null=True,blank=True)
    whatsapp_number=models.CharField(max_length=15,blank=True,null=True)
    meta_tags=models.TextField()
    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name_plural = "Company"

class YTVideos(models.Model):
    title = models.CharField(max_length=100)
    YT_code = models.CharField(max_length=100)
    show=models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'YT Video'
        verbose_name_plural = 'YT Videos'
        
    def __str__(self):
        return self.title

class Banner(models.Model):
    name=models.CharField(max_length=20)
    banner_image=models.ImageField(upload_to='upload/banners/')
    alt1=models.CharField(max_length=150,null=True,blank=True)
    heading1=models.CharField(max_length=35,null=True,blank=True)
    heading2=models.CharField(max_length=35,null=True,blank=True)
    heading3=models.CharField(max_length=35,null=True,blank=True)
    element_1_html=models.CharField( max_length=100,null=True,blank=True)
    element_2_html=models.CharField( max_length=100,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    javascript=models.TextField(null=True,blank=True)
    css=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Banners"

class Our_values(models.Model):
    title=models.CharField(max_length=30)
    icon_image=models.ImageField(upload_to='upload/icons/',null=True,blank=True)
    image=models.ImageField(upload_to='upload/images/',null=True,blank=True)
    alt1=models.CharField(max_length=150,null=True,blank=True)
    value=models.CharField( max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Our Values"

class About_us(models.Model):
    title=models.CharField(max_length=25)
    description=models.TextField()
    image_main1=models.ImageField(upload_to='upload/images/',null=True,blank=True)
    alt1=models.CharField(max_length=150,null=True,blank=True)
    image_main2=models.ImageField(upload_to='upload/images/',null=True,blank=True)
    alt2=models.CharField(max_length=150,null=True,blank=True)
    image_main3=models.ImageField(upload_to='upload/images/',null=True,blank=True)
    alt3=models.CharField(max_length=150,null=True,blank=True)
    image_sub1=models.ImageField(upload_to='upload/images/',null=True,blank=True)
    alt_s1=models.CharField(default="Diamond Laser Cutting Machine",max_length=150,null=True,blank=True)
    image_sub2=models.ImageField(upload_to='upload/images/',null=True,blank=True)
    alt_s2=models.CharField(default="Diamond Laser Cutting Machine",max_length=150,null=True,blank=True)
    image_sub3=models.ImageField(upload_to='upload/images/',null=True,blank=True)
    alt_s3=models.CharField(default="Diamond Laser Cutting Machine",max_length=150,null=True,blank=True)

    def save(self):
        super().save()  # saving image first

        if self.image_sub1:
            img1 = Image.open(self.image_sub1.path) # Open image using self
            new_img = (177, 145)
            img1.thumbnail(new_img)
            img1.save(self.image_sub1.path)  # saving image at the same path


        if self.image_sub2:
            img2 = Image.open(self.image_sub2.path) # Open image using self
            new_img = (177, 145)
            img2.thumbnail(new_img)
            img2.save(self.image_sub2.path)  # saving image at the same path

        if self.image_sub3:
            img3 = Image.open(self.image_sub3.path) # Open image using self
            new_img = (177, 145)
            img3.thumbnail(new_img)
            img3.save(self.image_sub3.path)  # saving image at the same path

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "About Us"


class Why_us(models.Model):
    title=models.CharField(max_length=25)
    description=models.TextField()
    fa_icon=models.CharField(max_length=25)
    index=models.IntegerField(default=1)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Why Us"

class Customers(models.Model):
    customer_name=models.CharField(max_length=20)
    customer_photo=models.ImageField(upload_to='upload/customer/')
    company_name=models.CharField(max_length=20)
    compnay_logo=models.ImageField(upload_to='upload/company/')
    customer_comment=models.CharField(max_length=200,null=True,blank=True)
    show_logo_in_client_list=models.BooleanField(default=False)
    show_testimonials=models.BooleanField(default=False)
    testimonials=models.CharField(max_length=300,null=True,blank=True)
    
    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name_plural = "Customer"

class Our_team(models.Model):
    name=models.CharField(max_length=25)
    person_image=models.ImageField(upload_to='upload/team/')
    designation=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=15)
    mail_id=models.EmailField( max_length=254)
    facebook_profile_link=models.URLField(max_length=200,blank=True,null=True)
    linked_in_profile_link=models.URLField(max_length=200,blank=True,null=True)
    skype_profile_link=models.URLField(max_length=200,blank=True,null=True)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Our Team"

class Questions_and_answers(models.Model):
    quetion=models.CharField(max_length=100)
    answer=models.TextField()
    index=models.IntegerField(default=1)
    
    def __str__(self):
        return self.quetion

    class Meta:
        verbose_name_plural = "Q&A"



class News(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    banner_image=models.ImageField(upload_to='upload/banners/')
    alt1=models.CharField(max_length=150,null=True,blank=True)
    category_tag=models.TextField()
    view_count=models.IntegerField(default=0,blank=True,null=True)
    show_in_home_page=models.BooleanField(default=False)
    index=models.IntegerField(default=0)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_on=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Blog"

class News_comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=50)
    created_on=models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return str(self.news)+'-'+str(self.user_name)

    class Meta:
        verbose_name_plural = "News Comment"

class Requests_for_quote(models.Model):
    user_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    contact_number=models.CharField(max_length=15)
    subject=models.CharField(default='Request for quote',max_length=30)
    content=models.TextField()
    created_on=models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = "Request for Quatation"

class Brochure(models.Model):
    title=models.CharField(max_length=15)
    file_to_share=models.FileField( upload_to='upload/files/')
    created_on=models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Brochures"

class Product(models.Model):
    name=models.CharField(max_length=50)
    link=models.SlugField(max_length=100,blank=False,null=False)
    product_type=models.CharField(max_length=50)
    image1=models.ImageField(upload_to='upload/product/')
    alt1=models.CharField(default="Diamond Laser Cutting Machine",max_length=150,null=True,blank=True)
    image2=models.ImageField(upload_to='upload/product/')
    alt2=models.CharField(default="Diamond Laser Cutting Machine",max_length=150,null=True,blank=True)
    image3=models.ImageField(upload_to='upload/product/')
    alt3=models.CharField(default="Diamond Laser Cutting Machine",max_length=150,null=True,blank=True)
    youtube_video_id=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField()
    show=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Products"



class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    show=models.BooleanField(default=True)
    show_in_home_page=models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        
    def __str__(self):
        return self.title

class ProductSpecificationTitle(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    index=models.IntegerField(default=1)

    def __str__(self):
        return str(self.product)+'-'+self.title
    
    class Meta:
        verbose_name_plural = "Products Specs Title"

class ProductSpecificationDetails(models.Model):
    productSpec=models.ForeignKey(ProductSpecificationTitle,on_delete=models.CASCADE)
    proparty=models.CharField(max_length=50)
    values=models.CharField(max_length=100,null=True,blank=True)
    index=models.IntegerField(default=1)

    def __str__(self):
        return str(self.productSpec)+'-'+self.proparty
    
    class Meta:
        verbose_name_plural = "Products Specs Desc"

class ImageGallary(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='upload/galary/')
    alt1=models.CharField(max_length=150,null=True,blank=True)
    show=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Image Gallary"
    