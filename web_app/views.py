
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context
from django.http.request import HttpRequest
from url_model.models import Meta_info

from HTMLParser import HTMLParser
from url_model.models import Meta_info
from django.shortcuts import redirect
req_url=""
import urllib2 as ulib2

class Parse(HTMLParser):
    def __init__(self,which_tag):
        self.data_avail=False
        self.meta_data=list()
        self.which_tag=which_tag
        self.attr=list()
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag==self.which_tag:
            self.data_avail=True
            
            for a in attrs:
                self.attr.append(a[1])
                            
    
    def handle_endtag(self, tag):
        if tag==self.which_tag:
            self.data_avail=False

    def handle_data(self, data):
        if self.data_avail:
            self.meta_data.append(data)
        



def welcome(Request):
    submitted=False
    template=get_template('home.html')
    out=template.render(Context({'title':'L3 Assignment'}))
    return HttpResponse(out)

def store_db(Request):
    global req_url
    
    metadata=Request.POST['meta']
    title=Request.POST['title']
    print req_url,metadata,title
    title=title.encode('utf8')
    metadata=metadata.encode('utf8')
    obj=Meta_info(url=req_url,title=title,meta=metadata)
    obj.save()
    
    return redirect('/')
    
    

def get_url(Request):
    global req_url
    submitted=True
    template=get_template('home.html')
    
    parse_title=Parse('title')
    parse_meta=Parse('meta')
    
    str1=str2=""
    try:
        req_url=Request.POST['url']
        con=ulib2.urlopen(req_url)
        html=con.read()
        parse_title.feed(html)
        parse_meta.feed(html)
        
        for i in parse_title.meta_data:
            str1=str1+i
            
        for i in parse_meta.attr:
            str2=str2+i
        print str2    
    except KeyError, ke:
        print 'URL not submitted',ke
    out=template.render(Context({'title_found':str1,'meta_found':str2}))
    
    return HttpResponse(out)
        
    
    
