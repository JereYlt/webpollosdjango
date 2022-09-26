from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.core.mail import send_mail
from webempresa.settings import EMAIL_HOST_USER
# Create your views here.
def contact(request):
     
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            #Su emal fue enviado y redireccionado
            email = EmailMessage(
                "La Tienda: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@tienda.com", 
                ["julio@djangoblog.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Su mensaje fue enviado, redireccionar a OK
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo paso,redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/Contact.html", {'form':contact_form})