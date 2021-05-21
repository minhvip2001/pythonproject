from django.shortcuts import render, redirect
from .forms import StudentsForm
from .models import Students
# Create your views here.
def std(request):
  if(request.method == "POST"):
    form = StudentsForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('/view')
      except:
        pass
  else:
    form = StudentsForm()
  return render(request, 'index.html', {'form':form})  

