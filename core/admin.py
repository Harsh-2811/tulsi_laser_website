from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from core.models import *

admin.site.register(Company)
admin.site.register(Our_values)
admin.site.register(Customers)
admin.site.register(Our_team)
admin.site.register(News_comment)
admin.site.register(Requests_for_quote)
admin.site.register(Brochure)
admin.site.register(ProductSpecificationTitle)
admin.site.register(ProductSpecificationDetails)
admin.site.register(ImageGallary)
admin.site.register(Videos)
admin.site.register(YTVideos)



class AboutUsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    #summernote_fields = '__all__'
    summernote_fields = 'description'
admin.site.register(About_us,AboutUsAdmin)

class WhyUsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    #summernote_fields = '__all__'
    summernote_fields = 'description'
admin.site.register(Why_us,WhyUsAdmin)

class NewsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    #summernote_fields = '__all__'
    summernote_fields = 'content'
admin.site.register(News,NewsAdmin)


class ProductAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    #summernote_fields = '__all__'
    summernote_fields = 'description'
admin.site.register(Product,ProductAdmin)


class QnAAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    #summernote_fields = '__all__'
    summernote_fields = 'answer'
admin.site.register(Questions_and_answers,QnAAdmin)


# Register your models here.
