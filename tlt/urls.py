"""tlt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import core.views as core_view
from tlt import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_view.home,name='index'),
    path('contact-us/',core_view.contact_us,name='contact_us'),
    path('send-inquiry/',core_view.request_for_queto,name='request_for_queto'),
    path('blog/',core_view.news,name='news'),
    path('blog-artical/<int:id>/',core_view.news_artical,name='news_artical'),
    path('about-us/',core_view.about_us,name='about_us'),
    path('our-team/',core_view.our_team,name='our_team'),
    path('testimonials/',core_view.testimonials,name='testimonials'),
    path('faq/',core_view.faq,name='faq'),
    path('product/<str:url>/',core_view.single_product,name='single_product'),
    path('products/',core_view.products,name='products'),
    path('gallary/',core_view.gallary,name='gallary'),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml',core_view.sitemap,name='sitemap'),
    
]

handler404 = 'core.views.error_404'
#handler500 = 'core.views.error_500'
handler403 = 'core.views.error_403'
handler400 = 'core.views.error_400'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

