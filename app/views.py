from django.http.response import HttpResponse
from django.shortcuts import render
from app.models import Childdetails
from . import Childregform
import datetime
import timeit


# Create your views here.
def time(func):
    def datime(request):
        time = datetime.datetime.now()
        msg = 'now the server date and time is::-' + str(time)
        return msg
        # return render(request,"Home.html", {"msg":msg})

def home(request):
        # return render(request,"Home.html")
        # def home(request):
        #     time = datetime.datetime.now()
        #     msg = '<h1> now the server date and time is::-' + str(time)
    msg = time(request)
    return render(request, "base.html.html", {"msg": msg})


def childhome(request):
    return render(request, "childrens.html")


def childmodels(request):
    view = Childdetails.objects.all()
    d = {"view": view}
    return render(request, "childview.html", context=d)


def details(req):
    view = Childregform.Mmeta
    d = {"view": view}
    return render(req, "childregform.html", context=d)


def childregtable(request):
    sno = request.POST.get("Sno")
    Child_Name = request.POST.get("Child_Name")
    Child_UIDNo = request.POST.get("Child_UIDNo")
    Gender = request.POST.get("Gender")
    Mother_Name = request.POST.get("Mother_Name")
    Mother_UIDNo = request.POST.get("Mother_UIDNo")
    Father_Name = request.POST.get("Father_Name")
    Father_UIDNo = request.POST.get("Father_UIDNo")
    Ration_CardNo = request.POST.get("Ration_CardNo")
    Mobile_No = request.POST.get("Mobile_No")
    Childdetails(Sno=sno, Child_Name=Child_Name, Child_UIDNo=Child_UIDNo, Gender=Gender, Mother_Name=Mother_Name,
                 Mother_UIDNo=Mother_UIDNo, Father_Name=Father_Name, Father_UIDNo=Father_UIDNo,
                 Ration_CardNo=Ration_CardNo, Mobile_No=Mobile_No).save()
    return render(request, "reg.html")


def homeview(request):
    return render(request, "home.html")

def childview(request):
    return render(request, "childrens.html")


def childview1(request):
    return render(request, "childview.html")

def childform(request):
    return render(request, "childregform.html")

