from django.shortcuts import render,HttpResponse

# Create your views here.
# logica que se ejecuta cuando se hace una peticion en nuestra web

html_base = '''
<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca De</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>

</ul>

'''

def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")




def contact(request):
    return render(request,"core/contact.html")






