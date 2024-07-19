from django.shortcuts import render, get_object_or_404, redirect
from .models import Obituary
from .forms import ObituaryForm

def obituary_list(request):
    obituaries = Obituary.objects.all()
    return render(request, 'obituary/obituary_list.html', {'obituaries': obituaries})

def obituary_detail(request, pk):
    obituary = get_object_or_404(Obituary, pk=pk)
    return render(request, 'obituary/obituary_detail.html', {'obituary': obituary})

def obituary_create(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('obituary_list')
    else:
        form = ObituaryForm()
    return render(request, 'obituary/obituary_form.html', {'form': form})
