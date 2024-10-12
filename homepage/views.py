from django.shortcuts import render

from team.models import TeamModel

from feedback.models import OfferModel


def home_page_view(request):
    teams = TeamModel.objects.all()
    most_viewed_offer = OfferModel.objects.all().order_by('-views_count')[:6]  
    offers = OfferModel.objects.all()
    context = {'teams': teams, 'offers': offers, 'viewed_offer': most_viewed_offer}
    return render(request, 'index.html', context)   


def five_page_view(request):
    return render(request, 'main/404/404.html')

def profil_page_view(request):
    return render(request, 'main/profile/profile.html')