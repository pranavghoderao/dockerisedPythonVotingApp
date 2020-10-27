from django.shortcuts import render ,redirect
from django.views.generic import TemplateView

from votingApp.models import VotingDetails
# Create your views here.

def vote(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        details= VotingDetails.objects.get(name=name)
        details.votes = details.votes + 1
        details.save()

        details_sona= VotingDetails.objects.get(name='Sona')
        details_panda= VotingDetails.objects.get(name='Panda')
        print(details_sona.name)
        print(details_sona.votes)
        print(details_panda.name)
        print(details_panda.votes)
        leader =''
        if details_panda.votes > details_sona.votes:
            leader = details_panda.name
        else:
            leader = details_sona.name
        lead =abs(details_panda.votes - details_sona.votes)
        print(lead)
        return render(request,"home.html",{'sona':details_sona.votes,'panda':details_panda.votes,'lead':lead,'leader':leader})
    return render(request,"home.html")
