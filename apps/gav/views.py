from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PersonForms, AccessForms, SearchForm
from .models import Personas, Avisitantes
from django.utils import timezone
# Create your views here.

def home(request):
  pass

@login_required
@permission_required('gav.add_personas')
def SearchPerson(request):
    # SE CREA LA VISTA DE BUSQUEDA POR CEDULA
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            try:
                person = Personas.objects.get(dni=dni)
                return redirect('dperson', person.dni)
            except Personas.DoesNotExist:
                request.session['dni_no_registrado'] = dni
                return redirect('cperson')
    else:
        form = SearchForm()
    return render(request, 'person/search.html', { 'form': form})

@login_required
@permission_required('gav.add_personas')
def lperson(request):
    # SE CREA LA LISTA DE PERSONAS
    try:
        persons = Personas.objects.all().order_by('dni')
        paginator = Paginator(persons, 8)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj}
        return render(request, 'person/lperson.html', context)
    except Personas.DoesNotExist:
        return render(request, 'accesss/notfound.html')

@login_required
@permission_required('gav.view_personas')
def dperson(request, dni):
    try:
        # Obtener la persona por su DNI
        person = get_object_or_404(Personas, dni=dni)
        # Obtener los registros de visitas de la persona, ordenados por fecha y hora de entrada
        paccess = Avisitantes.objects.filter(visitor=person).order_by('-entry', '-hours')
        # Configurar la paginación de los registros de visitas
        paginator = Paginator(paccess, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # Preparar el contexto para el template
        context = {
            'person': person,
            'page_obj': page_obj
        }
        # Renderizar el template con el contexto
        return render(request, 'person/dPerson.html', context)
    except Personas.DoesNotExist:
        # Si la persona no existe, renderizar el template de error
        return render(request, 'accesss/notfound.html')

@login_required
@permission_required('gav.add_personas')
def cperson(request):
    # SE CREA EL FORMULARIO DE PERSONAS
    if request.method == "POST":
        form = PersonForms(request.POST, request.FILES)
        if form.is_valid():
            new_person= form.save()
            return redirect('dperson', dni=new_person.dni)
    else:
        form = PersonForms()
    return render(request, 'person/cPerson.html', {'form': form})

@login_required
@permission_required('gav.change_personas')
def eperson(request, dni):
    # SE CREA LA EDICION DE LA PERSONA
    person = get_object_or_404(Personas,dni=dni)
    if request.method == 'POST':
        form = PersonForms(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('dperson', dni=person.dni)
    else:
        form = PersonForms(instance=person)
    return render(request, 'person/ePerson.html', {'person':person,'form': form})



###################################################################################
#######             VISTA DE LOS ACCESO DE LOS VISITANTES                    ######
###################################################################################

@login_required
@permission_required('gav.view_avisitantes')
def laccess(request):
    # SE CREA LA LISTA DE ACCESOS
    try:
        laccess = Avisitantes.objects.all().order_by('-entry','-hours')
        paginator = Paginator(laccess, 10)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj}
        return render(request, 'access/laccess.html', context)
    except Personas.DoesNotExist:
        return render(request, 'accesss/notfound.html')


@login_required
@permission_required('gav.view_avisitantes')
def daccess(request,pk):

        access = get_object_or_404(Avisitantes, pk=pk)
        return render(request, 'access/daccess.html', {'access':access})
   


@login_required
@permission_required('gav.view_avisitantes')
def raccess(request, dni):
    person_access = get_object_or_404(Personas,dni=dni)
    if request.method == 'POST':
        form = AccessForms(request.POST)
        if form.is_valid():
            access = form.save(commit=False)
            now = timezone.localtime()
            if access.entry == now.date():
                access.visitor = person_access
                access.save()
                return redirect('dperson', dni=person_access.dni)
            else:
                form.add_error(None,'La fecha y la hora del acesso deben ser las Actuales')
    else:
        form = AccessForms
    return render(request,'access/raccess.html',{'form':form, 'person_access':person_access})



@login_required
@permission_required('gav.view_avisitantes')
def eaccess(request,pk):
    # SE CREA LA EDICION DE ACCESO
    ecc = get_object_or_404(Avisitantes, pk=pk)
    if request.method =='POST':
        form = AccessForms(request.POST, instance=ecc)
        if form.is_valid():
            form.save()
            return redirect('laccess')
    else:
        form = AccessForms(instance=ecc)
    return render(request, 'access/eaccess.html', {'acc':ecc, 'form':form})

