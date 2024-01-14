from django.shortcuts import render
from .models import Member

def team(request):
    members = Member.objects.all()
    return render(request, 'team/team.html', {'members': members})