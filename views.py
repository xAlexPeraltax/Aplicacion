from django.shortcuts import render
from django.http import HttpResponse
from Inventory.models import autos
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def busqueda_autos(request):
    return render(request,"busqueda_autos.html")

def buscar(request):
    if 'prd' in request.GET and request.GET['prd']:
        guardaprod = request.GET['prd']
        if len(guardaprod) > 20:
            mensaje = "Texto de búsqueda demasiado largo, intenta de nuevo."
            return HttpResponse(mensaje)
        else:
            busca_car = autos.objects.filter(Marca__icontains=guardaprod)
            return render(request, "resultado_busqueda.html", {"autos": busca_car, "query": guardaprod})
    else:
        mensaje = "No has capturado nada para buscar."
        return HttpResponse(mensaje)
    
  #Agregar   registro
def insertar_auto(request):
    if request.method == "POST":
        Marca = request.POST.get("marca")
        Modelo = request.POST.get("modelo")
        Años = request.POST.get("años")
        Precio = request.POST.get("precio")

        if len(Años)!= 4 or not Años.isdigit():
            return HttpResponse("El año debe tener 4 dijitos y ser numerico")
        
        nuevo_auto = autos(Marca=Marca, Modelo=Modelo, Años=Años, Precio=Precio)
        nuevo_auto.save()

        return HttpResponse("Auto guarado correctamente!")
    else:
        return render(request,"insertar_auto.html")
    
#consultar todos
def crud(request):
    todos_los_autos = autos.objects. all()
    return render(request, 'muestra_todos.html',{'autos': todos_los_autos})

#Vista para enviar correo mediante formulario
def contacto (request):
    if request.method == 'POST':

        var_asunto= request.POST["asunto"]
        var_mensaje= request.POST["mensaje"] + " " + request.POST["email"]
        var_email_from= settings.EMAIL_HOST_USER
        receptor = ["alejandro.peraltaperales@cesunbc.edu.mx"]
        send_mail(var_asunto, var_mensaje, var_email_from, receptor)

        return render(request, "gracias.html")
    
    return render(request, "contacto.html")

