from django.shortcuts import render


def index(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def about(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'about.html', context=context)


def products(request):
    """View function for home page of site."""
    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'products.html', context=context)


def store(request):
    """View function for home page of site."""
    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'store.html', context=context)


# Create your views here.
