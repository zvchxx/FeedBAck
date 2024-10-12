from django.shortcuts import redirect, render

from feedback.models import OfferModel, ProblemModel

from django.db.models import F

from feedback.form import OfferForm, ProblemForm


def show_offers_views_page(request):
    search_query = request.GET.get('q', '') 
    offers = OfferModel.objects.all()
    
    if search_query:
        offers = offers.filter(title__icontains=search_query)  

    total_views = sum(offer.views_count for offer in offers)

    
    for offer in offers:
        offer.views_count += 1 
        offer.save() 

    context = {
        'offers': offers,
        'total_views': total_views
    }
    return render(request, 'main/offers/offer.html', context=context)


def show_problems_views_page(request):
    search_query = request.GET.get('q', '')  
    problems = ProblemModel.objects.all()
    
    if search_query:
        problems = problems.filter(title__icontains=search_query) 

    total_views = sum(problem.views_count for problem in problems)

    for problem in problems:
        problem.views_count += 1  
        problem.save() 

    context = {
        'problems': problems,
        'p_total_views': total_views
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
        form = ProblemForm()  
    return render(request, 'main/offers/offer-form.html', {'form': form})