from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import QueryForm

import wikidictparser as wdp

parser = wdp.get_parser('pl')


# Create your views here.
def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QueryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('home:query', query=form.cleaned_data['query'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QueryForm()

    return render(request, 'home/home.html', {'form': form})


def info(request):
    context = {}
    return render(request, 'home/info.html', context)

def contact(request):
    context = {}
    return render(request, 'home/contact.html', context)

def query(request, query):
    result = parser.fetch_by_meaning(query)
    context = {'query': query,
                'result': result,}
    return render(request, 'home/query.html', context)