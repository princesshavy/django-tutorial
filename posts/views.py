from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "id":0,
        "title":'Python is interpreted,high level,general purpose program',
    },
    {
        "id":1,
        "title":'Let\'s explore Javascript',
        "content":'Javascript is interpreted , high level,general purpose program'
    }
    ]
import posts
# Create your views here.
def helloWorld(request):
    html = "" 
    for post in posts :
        html += f'''
        <div>

             <h1>{post['id']} - {post['title']}</h1>
             <p>{post['content']}</p>
        </div>  
    '''
    return HttpResponse(html)

def post(request,id):
    for post in posts:
        if post['id'] == id :
            post_dict = post 
            break
    html = f''' 
    <h1>{post_dict['title']}</h1>
    <p>{post_dict['content']}</p>'''
    return HttpResponse(html)

