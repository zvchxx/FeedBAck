from django.shortcuts import redirect, render

from feedback.models import OfferModel

# from django.shortcuts import render, get_object_or_404

from django.db.models import F

from feedback.form import OfferForm, ProblemForm

# def show_offer_problem_page_view(request):
#     return render(request, 'main/offers/offer.html')


def show_offers_views_page(request):
    offers = OfferModel.objects.all()
    total_views = sum(offer.views_count for offer in offers) 
    context = {
        'offers': offers,
        'total_views': total_views, 
    }
    return render(request, 'main/offers/offer.html', context=context)

def offer_page_view(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user  
            offer.save()
            return redirect('/')  
    else:
        form = OfferForm()
    return render(request, 'main/offers/offer-form.html', {'form': form})


def problem_page_view(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user  
            problem.save()
            return redirect('/')  
    else:
        form = ProblemForm()  # To'g'ri forma olish
    return render(request, 'main/offers/offer-form.html', {'form': form})


