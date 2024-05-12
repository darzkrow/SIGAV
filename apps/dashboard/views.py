from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

from apps.gav.models import Personas, Avisitantes
# Create your views here.

@login_required
def Dashboard(request):
    pcount = Personas.objects.all().count
    acount= Avisitantes.objects.all().count()
  
    return render(request,'dashboard/home.html', {'pcount':pcount, 'acount':acount})



@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {'profile': profile}
    return render(request, 'dashboard/profile_detail.html', context)

@login_required
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', pk=profile.pk)  # Redirect to detail view
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'dashboard/edit_profile.html', context)


@login_required
def current_user_profile(request):
    user = request.user  
    profile = user.profile
    context = {'profile': profile}
    return render(request, 'dashboard/profiles.html', context)