
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context

def hello(Request):
    template=get_template('home.html')
    out=template.render(Context({'title':'Akash'}))
    return HttpResponse(out)
    
