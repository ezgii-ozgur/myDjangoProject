from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author':'Ezgi Özgür',
#         'title':'PRINCESS EZGI',
#         'content':'Ezgi is a best princess in the MEPSAN',
#         'date_posted':"July 14, 1998"
#     },
#     {
#         'author':'Kasım Boydas',
#         'title':'FRISOR KASIM ',
#         'content':'Kasım ar baste frisor i Goteborg',
#         'date_posted':"July 14, 1998"
#     }
# ]


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context )


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})