import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

from django.shortcuts import render
from django.http import JsonResponse

from tasman.models import Data, Freq

def index(request):
    return render(request,'index.html')

def viewtable(request):
	query = Data.objects.all()
	context_dict = {'data':query}
	print('context_dict')
	return render(request,'viewtable.html',context_dict)

def viewjson(request):
    a = list(Data.objects.values())
    return JsonResponse({'data': a})

def viewchart(request):
	query = Data.objects.all()
	context_dict = {'data':query}
	print('context_dict')
	return render(request,'chart.html',context_dict)

def viewchart1(request):
    query = Data.objects.all()
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'chart1.html',context_dict)

def viewchart2(request):
    query = Data.objects.all()
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'chart2.html',context_dict)

def viewchart3(request):
    query = Data.objects.all()
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'chart3.html',context_dict)

def about(request):
    return render(request,'about.html')

def tech_2g(request):
    query = Freq.objects.filter(tech__name__contains="2g")
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'frequency.html',context_dict)

def tech_3g(request):
    query = Freq.objects.filter(tech__name__contains="3g")
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'frequency.html',context_dict)

def tech_4g(request):
    query = Freq.objects.filter(tech__name__contains="4g")
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'frequency.html',context_dict)

def tech_NFC(request):
    query = Freq.objects.filter(tech__name__contains="NFC")
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'frequency.html',context_dict)

def tech_ZigBee(request):
    query = Freq.objects.filter(tech__name__contains="ZigBee")
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'frequency.html',context_dict)

def tech_WiFi(request):
    query = Freq.objects.filter(tech__name__contains="WiFi")
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'frequency.html',context_dict)

def tech_WiMax(request):
    query = Freq.objects.filter(tech__name__contains="WiMax")
    context_dict = {'data':query}
    print('context_dict')
    return render(request,'frequency.html',context_dict)

# view for csv upload

@permission_required('admin.can_add_log_entry')
def data_upload(request):
    template = "upload.html"

    prompt = {
    'order': 'Order of CSV should be salinity,conductivity,temperature,depth'
    }

    if request.method == "GET":
        return render (request, template, prompt)

    csv_file = request.FILES['file']

    # checking file extension

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Data.objects.update_or_create(
            salinity=column[0],
            conductivity=column[1],
            temperature=column[2],
            depth=column[3]
    )
    context = {}
    return render(request, template, context)