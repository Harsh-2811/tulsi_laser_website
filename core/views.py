from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from core.models import *
from django.http import HttpResponse,JsonResponse
from datetime import date
import smtplib
  
def send_mail(body_msg):
    gmail_user = 'tulsilaser.tech@gmail.com'
    gmail_password = 'TulsiLaser@1234'

    sent_from = gmail_user
    to = ['tulsilasertec@gmail.com',]
    subject = 'Query Message In Website'
    body = body_msg

    email_text = """\
    From: %s \n
    To: %s \n
    Subject: %s \n\n 
 %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except Exception as e:
        print('Something went wrong...',e)

def get_company_data(data):
    data['company']=Company.objects.all()[0]

    try:
        data['total_year']=int(date.today().year)-int(data['company'].establishment_year)
    except:
        data['total_year']=int(date.today().year)-2017
    data['products_list']=Product.objects.filter(show=True)
    data['index_page']=False
    return data

def sitemap(request):
    #printBASE_DIR)
    return HttpResponse(open('sitemap.xml').read() ,content_type="text/xml; charset=utf-8")



def get_index_page_data(data):
    data['values']=Our_values.objects.all()
    data['about_us']=About_us.objects.filter(title='home_about_us')[0]
    data['testimonial']=Customers.objects.filter(show_testimonials=True)
    data['customers']=Customers.objects.filter(show_logo_in_client_list=True)
    data['news']=News.objects.filter(show_in_home_page=True).order_by('index')
    data['videos']=Videos.objects.filter(show_in_home_page=True)
    data['yt_videos']=YTVideos.objects.filter(show=True)
    data['index_page']=True
    return data

@csrf_exempt
def request_for_queto(request):
    if request.method == "POST":
        if request.POST.get("contact_num"):
            contact_num=str(request.POST.get("contact_num")).strip()
            name=str(request.POST.get("name")).strip()
            email=str(request.POST.get("email")).strip()
            subject=str(request.POST.get("subject"))
            content=str(request.POST.get("content"))
            if name== '' or contact_num=='' or email=='' or subject=='':
                data={}
                data['sended']='0'
                return JsonResponse(data)
            
            check_c_exists=Requests_for_quote.objects.filter(contact_number=contact_num)
            if len(check_c_exists)<=2:
                obj=Requests_for_quote()
                obj.user_name=name
                obj.contact_number=contact_num
                obj.email=email
                obj.subject=subject
                obj.content=content
                obj.save()
                send_mail('Hey, Got the mail from '+name+' \n contact number: '+ contact_num+
                ' \n Email: '+email+' \n Subject: '+subject+' \n Message: '+ content)
            else:
                data={}
                data['sended']='2'
                return JsonResponse(data)        
            data={}
            data['sended']='1'
            return JsonResponse(data)        
    data={}
    data['sended']='0'
    return JsonResponse(data)

def home(request):
    data={}
    get_company_data(data)
    get_index_page_data(data)
    return render(request,'core/index.html',context=data)

def contact_us(request):
    data={}
    get_company_data(data)
    return render(request,'core/contact-us2.html',context=data)

def about_us(request):
    data={}
    get_company_data(data)
    data['about_us']=About_us.objects.filter(title='about_us_page')[0]
    data['news']=News.objects.all().order_by('index')
    data['why_us']=Why_us.objects.all().order_by('index')
    data['team_member']=Our_team.objects.all()
    return render(request,'core/about_us.html',context=data)


def our_team(request):
    data={}
    get_company_data(data)
    data['team_member']=Our_team.objects.all()
    return render(request,'core/our_team.html',context=data)

def testimonials(request):
    data={}
    get_company_data(data)
    data['testimonials']=Customers.objects.filter(show_testimonials=True)
    return render(request,'core/testimonials.html',context=data)

def news(request):
    data={}
    get_company_data(data)
    data['news']=News.objects.all().order_by('index')
    return render(request,'core/news-big.html',context=data)

def faq(request):
    data={}
    get_company_data(data)
    data['faq']=Questions_and_answers.objects.all().order_by('index')
    return render(request,'core/our_faq.html',context=data)

def news_artical(request,id):
    data={}
    get_company_data(data)
    data['news']=News.objects.get(id=id)
    data['all_news']=News.objects.all().order_by('index')
    return render(request,'core/news-single.html',context=data)

def single_product(request,url):
    data={}
    get_company_data(data)
    p=Product.objects.get(link=url)
    data['product']=p
    ps=ProductSpecificationTitle.objects.filter(product=p).order_by('index')
    _ps={}
    for i in ps:
        tmp=ProductSpecificationDetails.objects.filter(productSpec=i).order_by('index')
        lst={}
        for ik in tmp:
            lst[ik.proparty]=ik.values
        _ps[i.title]=lst
    print(_ps)
    data['product_spec_title']=_ps
    return render(request,'core/single_product.html',context=data)

def products(request):
    data={}
    get_company_data(data)
    data['products']=Product.objects.all()
    
    return render(request,'core/products.html',context=data)

def gallary(request):
    data={}
    get_company_data(data)
    data['images']=ImageGallary.objects.filter(show=True)
    print(data)
    return render(request,'core/gallary.html',context=data)

def error_404(request, exception):
        data = {}
        return render(request,'core/404.html', data)

def error_500(request,  exception):
        data = {}
        return render(request,'core/500.html', data)

def error_400(request, exception):
        data = {}
        return render(request,'core/404.html', data)

def error_403(request,  exception):
        data = {}
        return render(request,'core/404.html', data)
