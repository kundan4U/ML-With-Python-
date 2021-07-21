from django.shortcuts import render
import pickle
import os

# Create your views here.
def index(request):
    return render(request,'index.html')
def test(request):
    ppw=int(request.POST['PPW'])
    pn= int(request.POST['PN'])
    mi= int(request.POST['MI'])
    appm= int(request.POST['APPM'])
    modulepath=os.path.dirname(__file__)
    filepath=os.path.join(modulepath,'taxi.pkl')
    model=pickle.load(open(filepath,'rb'))
    res=str(model.predict([[ppw,pn,mi,appm]])[0].round(2))
    return render(request,'index.html',{'res':res})
