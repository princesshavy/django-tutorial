from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloWorld(request):
    html = "" 
    for post in posts :
     html += f'''
        <div>
             <h1>{post.id} - {post.title}</h1>
             <p>{post.content}</p>
        </div>  
    '''
    return HttpResponse("<h1>Hello World!</h1>")