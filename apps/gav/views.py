from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PersonForms, AccessForm, SearchForm
from .models import Personas, Avisitantes
from django.utils import timezone
# Create your views here.

def home(request):
  pass


@permission_required('gav.add_personas', raise_exception=False)
def SearchPerson(request):
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
    persons = Personas.objects.all().order_by('-dni')
    paginator = Paginator(persons, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'person/lperson.html', {'page_obj': page_obj})


@login_required
@permission_required('gav.view_personas')
def dperson(request, dni):
   # SE CREA EL DETALLE DE LA PERSONA
   person = get_object_or_404(Personas, dni=dni)   
   return render(request,'person/dPerson.html', {'person':person})

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

@permission_required('gav.change_personas', login_url='home')
def eperson(request, dni):
    person = get_object_or_404(Personas,dni=dni)
    if request.method == 'POST':
        form = PersonForms(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('dperson', dni=person.dni)
    else:
        form = PersonForms(instance=person)
    return render(request, 'person/ePerson.html', {'person':person,'form': form})


