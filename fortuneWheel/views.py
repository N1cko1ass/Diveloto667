from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def fortuneWheel(request):
    return render(request, "fortuneWheel/fortuneWheel.html")
