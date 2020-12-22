from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import requests
import datetime
import shopify as shopifyapi
from .models import shopify as spmodel
from .models import formdata
from django.views.decorators.csrf import csrf_exempt

import json

API_KEY = "cb520b42ea17f760b9afc50dd10f3d0d"
SHARED_SECRET = "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"
# shop_name = "3istore"
API_VERSION = "2020-07"
# SITE_NAME = "https://" + shop_name + ".myshopify.com"


# Replace the following with your shop URL

shop = ""


# Create your views here.
def login(request):
    return render(request, 'login.html')


def createdform(request):
    return render(request, 'CreatedFormDetail.html')


def token(code, shop):
    # print(request.GET)
    ur = "https://" + shop + "/admin/oauth/access_token"
    print("shop is here", shop)
    s = {
        "client_id": API_KEY,
        "client_secret": SHARED_SECRET,
        "code": code
    }
    r = requests.post(url=ur, json=s)
    x = json.loads(r.text)
    return x


def get_token(request):  # if hmac is get then go to welcome.html otherwise go to index.html
    if request.method == "GET":
        if request.GET.get('hmac') is not None:
            code = request.GET.get('code')
            shop = request.GET.get('shop')
            a = token(code=code, shop=shop)

        else:
            HttpResponse("Don't Get HMAC")
    return a


def shopify(request):
    # global main
    if request.method == "POST":
        url = request.POST['shop']
        s_url = url.strip('/')
        # print(s_url)
        api_key = API_KEY
        # print(api_key)
        link = '%s/admin/oauth/authorize?client_id=%s&redirect_uri=https://64b8ed9b2cf6.ngrok.io/final&scope=read_products,write_products,read_customers,write_customers' % (s_url, api_key)
        print(link)
        li = link.strip("/")
        # print(li)
        # URL = li
        redirect = HttpResponseRedirect(f'{li}')
        # ds = redirect
        # print(ds)
    return redirect


def redirect(request):
    if request.GET.get('shop') is not None:
        shop = request.GET.get('shop')
        redir = HttpResponseRedirect(redirect_to='https://' + shop + '/admin/apps/6developerorderapp')
        # if redir.status_code == 302:
        #     return render(request, 'index.html')
    return redir


def getid(setshop, accesstoken):
    my_dict = dict()
    url = "https://" + setshop + "/admin/api/2020-07/shop.json"
    headers = {
        "X-Shopify-Access-Token": accesstoken,
        "Content-Type": "application/json",
        "client_id": API_KEY,
        "client_secret": SHARED_SECRET
    }
    r = requests.get(url, headers=headers)
    # print(r.text)
    result = json.loads(r.text)
    # print(result, "hello id")
    my_dict["id"] = result['shop']['id']
    my_dict["store_name"] = result['shop']['domain']
    return my_dict


@csrf_exempt
def getdata(request):
    if request.method == "POST":
        s = shop
        record = spmodel.objects.filter(shop=s)
        if record:
            access = record[0].access_token
            get_data = getid(setshop=s, accesstoken=access)
            if get_data['store_name'] == s:
                id = get_data['id']
            store_id = id
            data = request.POST['data']
            da = datetime.datetime.now()
        record = formdata()
        record.content = request.POST['data']
        record.store = store_id
        record.build_date = da
        record.delete_date = ""
        record.edit_date = ""
        record.update_date = ""
        record.save()
        return render(request, 'result.html', {'x': access, 'y': data})


@xframe_options_exempt
def create(request):
    return render(request, "Form.html")


# https://4e3c1837379f.ngrok.io/final?hmac=badba2da28460494ac56af5df7fdc23124bbf4aa97f0ea9f460685603e6a2911&locale=en-IN&new_design_language=true&session=47171de9268fd0a4afd3291bc9452ac86704bb6c7b96dad2f6646901573f0ba6&shop=3istore.myshopify.com&timestamp=1603461501


@xframe_options_exempt
def final(request):
    if request.GET.get('hmac') is not None:
        hmac = request.GET.get('hmac')
        global shop
        shop = request.GET.get('shop')
        if request.GET.get('code') is not None:
            code = request.GET.get('code')
            if len(code) != 0:
                record = spmodel.objects.filter(shop=shop)
                if record:
                    get_code = record[0].code

                    get_access_token = record[0].access_token
                    return redirect(request=request)
                else:
                    accesstoken = token(code=code, shop=shop)
                    rec = spmodel()
                    rec.shop = shop
                    rec.code = code
                    rec.hmac = hmac
                    rec.access_token = accesstoken['access_token']
                    rec.save()
                    return redirect(request=request)
                return redirect(request=request)
        else:
            record = spmodel.objects.filter(shop=shop)
            if record:
                getaccess = record[0].access_token
                getshop = record[0].shop
                # get_data = getid(setshop=getshop, accesstoken=getaccess)
                # print(get_data)
                return render(request, 'final.html', {'shop': getshop, 'access': getaccess})
            else:
                return HttpResponse("No Data Found")
    else:
        return render(request, 'login.html')
