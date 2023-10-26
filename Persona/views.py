from django.shortcuts import render,redirect
from .models import Persona,Contacto
from .forms import FormPersona,ContactoForm
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.

def index(request):
    return render(request, 'persona\index.html')

def listado(request):
    personas = Persona.objects.all();
    return render(request, 'persona\listado.html',{"personas":personas})

def nueva(request):
    if request.method == "POST":
        formpersona = FormPersona(request.POST)
        if formpersona.is_valid():
            formpersona.save()
            return redirect('listado')
    else:
        formpersona = FormPersona()
    return render(request,'persona/nueva.html',{"formpersona":formpersona})

def editar(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if(request.method == "POST"):
        formpersona = FormPersona(request.POST, instance = persona)
        if formpersona.is_valid():
            formpersona.save()
            return redirect('listado')    
    else:
        formpersona = FormPersona(instance=persona)
    return render(request, 'persona/editar.html', {"formpersona": formpersona})


def contacto(request):
    form_contacto= ContactoForm()
    if request.method == 'POST':
        form_contacto = ContactoForm(request.POST)
        if form_contacto.is_valid(): 
            nombre = request.POST['nombre']
            email = request.POST['email']
            mensaje = request.POST['mensaje']
            send_mail(
                'Contacto - Sub Gerencia de Seguros',
                f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                'tu_email@dominio.com',  # Dirección de correo electrónico del remitente
                ['correo_destino@dominio.com'],  # Lista de destinatarios o solo 1
                fail_silently=False,
            )
            messages.success(request, 'Correo enviado con éxito.')
        else:
            messages.error('Error. Por favor verifica que los datos esten correctos.') 

    return render(request, 'persona/contacto.html', {'form_contacto':form_contacto})

        
def lista_personas(request):
    personas = Persona.objects.all();
    page = request.GET.get('page', 1)
    paginator = Paginator(personas, 2)  #  paginate_by 5
    try:
        personas = paginator.page(page)
    except PageNotAnInteger:
        personas = paginator.page(1)
    except EmptyPage:
        personas = paginator.page(paginator.num_pages)
    return render(request, "persona/Lista_Personas.html", {"personas": personas})    