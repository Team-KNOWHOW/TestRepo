from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import CBCodeHdr, CBCodeDtl
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "home.html")

def cb_code(request):
    context = {}

    if 'type_cd' in request.GET:
        typecd = request.GET['type_cd']
        rsCode = CBCodeDtl.objects.filter(type_cd=typecd, usage_fg='Y')
    else:
        typecd = None
        rsCode = None

    context["type_cd"] = typecd

    rsHeader = CBCodeHdr.objects.filter(usage_fg='Y')
    context["rsHeader"] = rsHeader
    context["rsCode"] = rsCode

    return render(request, "cb_code.html", context)

@csrf_exempt
def codetype_insert(request):
    context = {}

    typecd = request.GET['typecd']
    typename = request.GET['typename']

    if CBCodeHdr.objects.filter(type_cd=typecd).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type code exists..."
        return JsonResponse(context, content_type="application/json")

    if CBCodeHdr.objects.filter(type_nm=typename).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type name exists..."
        return JsonResponse(context, content_type="application/json")

    CBCodeHdr.objects.create(type_cd=typecd,
                             type_nm=typename,
                             )

    context["flag"] = "0"
    context["result_msg"] = "Type insert success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def codetype_update(request):
    context = {}

    typeid = request.GET['typeid']
    tvalue = request.GET['tvalue']

    if CBCodeHdr.objects.filter(type_nm=tvalue).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type name exists..."
        return JsonResponse(context, content_type="application/json")

    rsHeader = CBCodeHdr.objects.get(id=typeid)
    rsHeader.type_nm = tvalue
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "Type update success..."
    return JsonResponse(context, content_type="application/json")

@csrf_exempt
def codetype_delete(request):
    context = {}

    typeid = request.GET['typeid']

    rsHeader = CBCodeHdr.objects.get(id=typeid)
    rsHeader.usage_fg = 'N'
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "Type delete success..."
    return JsonResponse(context, content_type="application/json")
