from .models import Offer
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import json
from django.http import HttpResponse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import CarMake, Offer
from .models import CarModel
from .forms import NameForm
# Create your views here.


def setLocation(location, request):
    # do Something
    if location == None:
        if not request.session.get('offerlocation'):
            request.session['offerlocation'] = 'Ontario'
    else:
        request.session['offerlocation'] = location
    

def home_view(request, *args, **kwargs):
    setLocation(request.GET.get('location'), request)

    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    setLocation(request.GET.get('location'), request)

    return render(request, "about.html", {})


def search_view(request, *args, **kwargs):
    setLocation(request.GET.get('location'), request)
    mycontext = {
        "my_title": "Search by Make or Model",
        "my_list": [1, 2, 3]
    }
    return render(request, "search.html", mycontext)


def make_view(request):
    setLocation(request.GET.get('location'), request)
    obj = Offer.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "make.html", context)


def allmakes_list_view(request):
    setLocation(request.GET.get('location'), request)

    queryset = Offer.objects.filter(offerlocation=request.session.get(
        'offerlocation')).order_by('carmake').distinct("carmake")
    context = {'object_list': queryset}
    return render(request, "allmakes.html", context)

# def model_list_view(request,carmake):
#     print (request.path)
#     queryset = Offer.objects.filter(carmake=carmake).order_by('offerstartdate','carmodel')
#     context = {'object_list': queryset}
#     return render(request, "make.html", context)


class Model_list_view(ListView):
    template_name = 'make.html'
    queryset = Offer.objects.all().order_by('offerstartdate', 'carmodel')

    def get_context_data(self, **kwargs):
        #queryset = Offer.objects.filter(carmake=self.kwargs['carmake']).order_by('offerstartdate','carmodel')
        # Call the base implementation first to get a context
        setLocation(self.request.GET.get('location'), self.request)
        context = super().get_context_data(**kwargs)
        context['offerlocation'] = self.request.session['offerlocation']

        # Add in a QuerySet of all the books
        context['distinctmodels'] = Offer.objects.filter(
            offerlocation=context['offerlocation'], carmake=self.kwargs['carmake']).order_by('carmodel').distinct("carmodel")
        context['makeoffers'] = Offer.objects.filter(
            offerlocation=context['offerlocation'], carmake=self.kwargs['carmake']).order_by('offerstartdate', 'carmodel')
        context['carmake'] = self.kwargs['carmake']

        return context


def offersbymodel_list_detail_view(request, carmake, carmodel, offerlocation):
    setLocation(request.GET.get('location'), request)
    queryset = Offer.objects.filter(carmake=carmake, carmodel=carmodel, offerlocation=request.session.get(
        'offerlocation')).order_by('offerstartdate', 'carmodel')
    context = {'object_list': queryset}
    return render(request, "offersbymodel.html", context)


class Offersbymodel_list_detail_view(ListView):
    template_name = 'offersbymodel.html'
    queryset = Offer.objects.all().order_by('offerstartdate', 'carmodel')

    def get_context_data(self, **kwargs):
        #queryset = Offer.objects.filter(carmake=self.kwargs['carmake']).order_by('offerstartdate',self.kwargs['carmodel'])
        # Call the base implementation first to get a context
        setLocation(self.request.GET.get('location'), self.request)
        context = super().get_context_data(**kwargs)
        context['offerlocation'] = self.request.session['offerlocation']

        # Add in a QuerySet of all the books
        context['offers'] = Offer.objects.filter(carmake=self.kwargs['carmake'], carmodel=self.kwargs['carmodel'],
                                                 offerlocation=context['offerlocation']).order_by('offerlocation', 'carmodel', 'caryear', 'offerstartdate')
        context['carmodel'] = self.kwargs['carmodel']
        context['carmake'] = self.kwargs['carmake']
        return context


class Offersbymodelandoffertype_list_detail_view(ListView):
    template_name = 'offersbymodel.html'
    queryset = Offer.objects.all().order_by('offerstartdate', 'carmodel', 'cartrim')

    def get_context_data(self, **kwargs):
        #queryset = Offer.objects.filter(carmake=self.kwargs['carmake']).order_by('offerstartdate',self.kwargs['carmodel'])
        # Call the base implementation first to get a context
        setLocation(self.request.GET.get('location'), self.request)
        context = super().get_context_data(**kwargs)
        context['offerlocation'] = self.request.session['offerlocation']
        context['offertype'] = self.kwargs['offertype']

        # Add in a QuerySet of all the books
        context['offers'] = Offer.objects.filter(carmake=self.kwargs['carmake'], carmodel=self.kwargs['carmodel'], offerlocation=context['offerlocation'],
                                                 offertype=context['offertype']).order_by('offerlocation', 'carmodel', 'caryear', 'offerstartdate')
        context['carmodel'] = self.kwargs['carmodel']
        context['carmake'] = self.kwargs['carmake']
        context['offertype'] = self.kwargs['offertype']
        return context

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getModelsAjax(request):
    selectedmake = request.POST['selectedmake']
    print("ajax country_name ", selectedmake)
    selectedmake = selectedmake.strip()
    result_set = []
    
    request.session['make'] = selectedmake

    availmodels = Offer.objects.filter(carmake=selectedmake).order_by(
        "carmodel").distinct("carmodel")
    print("selected country name ", selectedmake)

    for availmodel in availmodels:
        print("city name", availmodel.carmodel)
        result_set.append({'name': availmodel.carmodel})
    return HttpResponse(json.dumps(result_set), content_type='application/json')

@csrf_exempt
def setLocationAjax(request):
    selectedLocation = request.POST['selectedLocation']
    print("ajax setting location to: ", selectedLocation)
    selectedLocation = selectedLocation.strip()
    result_set = []
    request.session['offerlocation'] = selectedLocation
    return HttpResponse(json.dumps(result_set), content_type='application/json')

@csrf_exempt
def setModelAjax(request):
    selectedModel = request.POST['selectedModel']
    print("ajax setting model to: ", selectedModel)
    selectedModel = selectedModel.strip()
    result_set = []
    request.session['model'] = selectedModel
    return HttpResponse(json.dumps(result_set), content_type='application/json')
