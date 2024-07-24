from django.shortcuts   import render
from django.http        import HttpResponse, HttpResponseRedirect
from .models            import Flan, ContactForm, ContactFormModelForm
from .forms             import ContactFormForm, ContactFormModelFormForm

# Create your views here.

def index(request):    
    flanes_publicos             = Flan.objects.filter(is_private = False)
    cant_pub                    = len(flanes_publicos)
    context                     =   {
            'title'             :       'onlyflans'     ,
            'flanes_pub'        :       flanes_publicos ,
            'cant_pub'          :       cant_pub        ,       
                                    }
    return render(request, 'index.html', context)


def about(request):
    context                     =   {
            'title':'Sobre Nosotros',
                                    }
    return render(request, 'about.html', context)


def welcome(request):
    flanes_privados             = Flan.objects.filter(is_private = True)
    cant_priv                   = len(flanes_privados)                  
    context                     =   {
            'title':'Bienvenido a Onlyflans',
            'flanes_priv'       :       flanes_privados,
            'cant_priv'         :       cant_priv,
                                    }
    return render(request, 'welcome.html', context)


def contact(request):
    if request.method           == 'POST':
        form                    =   ContactFormModelFormForm(request.POST)
                                    
        if form.is_valid():
            contact_form        =   ContactFormModelForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('contactok/')        
    else:
        form                    =   ContactFormModelFormForm()       
    context                     =   {
            'title' :   'Contacto',
            'form'  :   form
                                    }
    return render(request, 'contact.html', context)

def successcontact(request):    
    context                     =   {
            'title' :   'Contacto OK',
                                    }
    return render(request, 'successcontact.html', context)