from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
#import posts
posts = [
    {
        "id":1,
        "title":'Python is interpreted,high level,general purpose program',
        "content":'Javascript is interpreted , high level,general purpose program'
    },
    {
        "id":2,
        "title":'Let\'s explore Javascript',
        "content":'Javascript is interpreted , high level,general purpose program'
    },
]
# Create your views here.
def home(request):
    html = "" 
    for post in posts :
        html += f'''
            <div>
            <a href = "/post/{post['id']}/">
             <h1>{post['id']} - {post['title']}</h1>
             <p>{post['content']}</p>
        </div>'''
    name = "Jeff Bezos"
    return render(request,'posts/home.html',{})

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post 
            valid_id = True
            break
    if valid_id:
        html = f''' 
                <h1>{post_dict['title']}</h1>
                <p>{post_dict['content']}</p>
            '''
        return HttpResponse(html)
    else:
            return HttpResponseNotFound("Post Not Available😎😥")

def google(request,id):
     url = reverse("post",args=[id])
     return HttpResponseRedirect(url)
 