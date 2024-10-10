from django.shortcuts import render

from feedback.models import OfferModel

def offer_problem_page_view(request, pk):
    offer = OfferModel.objects.filter(pk=pk)
    if offer.exists():
        offer = offer.first()
        offer.views_count += 1
        offer.save()
        context = {"offer": offer}
        return render(request, 'main/offers/offer-form.html', context)
    return render(request, '404.html')

def show_offer_problem_page_view(request):
    return render(request, 'main/offers/offer.html')