from django.shortcuts import render, redirect
#Importa funciones para renderizar plantillas y redirigir a otras vistas
from django.http import HttpResponse
#Permite enviar respuestas HTTP directamente al cliente
from Gestion.models import Autos
#Importa el modelo `Autos` definido en el archivo `models.py`
from django.db.models import Q  
#Proporciona soporte para consultas complejas con condiciones "OR"
from django.conf import settings
#Permite acceder a la configuración del proyecto, como credenciales de correo
from django.core.mail import send_mail
#Función para enviar correos electrónicos

# Create your views here.

def busqueda_autos(request):
    return render(request, "busqueda_autos.html")

def buscar(request):
    if request.GET.get("prd", ""):  
        #Obtiene el valor ingresado en el campo de búsqueda (parámetro "prd")
        guardaprod = request.GET["prd"]
        if len(guardaprod) > 20:
            #Verifica que el texto no supere los 20 caracteres
            mensaje = 'Texto de búsqueda demasiado largo, vuelve a intentar'
        else:
        #Realiza una búsqueda en la tabla `Autos`
            buscar_auto = Autos.objects.filter(
                Q(marca__icontains=guardaprod) |
                Q(modelo__icontains=guardaprod) |
                Q(año__icontains=guardaprod) |
                Q(precio__icontains=guardaprod) |
                Q(color__icontains=guardaprod)
            )
            return render(request, "resultado_busqueda.html", {"Autos": buscar_auto, "query": guardaprod})
    else:
        #Si no se ingresó texto de búsqueda, muestra un mensaje.
        mensaje = 'No has capturado nada'
    return HttpResponse(mensaje)


def contacto(request):
    if request.method=='POST':
        #Verifica si el formulario fue enviado mediante POST
        var_asunto= request.POST["asunto"]
        #Obtiene el asunto ingresado en el formulario
        var_mensaje= request.POST["mensaje"] + " " + request.POST["email"]
        #Crea el mensaje concatenando el texto del mensaje y el email del remitente
        var_email_from= settings.EMAIL_HOST_USER
        #Obtiene el email configurado como remitente
        receptor = ["victor.salazarlopez@cesunbc.edu.mx"]
        #Define el email del receptor
        send_mail(var_asunto, var_mensaje, var_email_from, receptor)
        #Envía el correo utilizando los datos obtenidos
        return render(request, "gracias.html")
    return render(request, "contacto.html")

def crud(request):
    autos = Autos.objects.all()
    #Obtiene todos los registros de la tabla `Autos`
    print(autos) 
    #Imprime los autos en la consola (para depuración)
    return render(request, 'muestra_todo.html', {'Autos': autos})

def insertar_auto(request):
    if request.method == 'POST':
        #Verifica si el formulario fue enviado mediante POST
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        año = request.POST.get('año')
        precio = request.POST.get('precio')
        color = request.POST.get('color')
        #Obtiene los valores ingresados en el formulario
        nuevo_auto = Autos(
            marca=marca,
            modelo=modelo,
            año=año,
            precio=precio,
            color=color
        )
        #Crea una nueva instancia del modelo `Autos` con los valores obtenidos
        nuevo_auto.save() 
        #Guarda el nuevo auto en la base de datos. 
        return redirect('crud')  
    return render(request, 'insertar_auto.html')  
