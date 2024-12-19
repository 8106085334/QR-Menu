from django.shortcuts import render 
from .forms import  QR_Code_Form
import qrcode
import os 
from  django.conf import  settings


def genarate_qr_code(request):
    if request.method == 'POST':
        form = QR_Code_Form(request.POST)
        if form.is_valid():
            rest_nam = form.cleaned_data['resturant_name']
            url = form.cleaned_data['url']
            # check data backend coming or not 
            #print(rest_nam,url) done 

            #Generate QR code 
            qr = qrcode.make(url)
            #print(qr)
            #qr.save('test.qr.png')
            file_name = rest_nam.replace(" ","_").lower()+"_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT,file_name)
            qr.save(file_path)

            #image URL 
            file_url = os.path.join(settings.MEDIA_URL,file_name)
            context = {
                'rest_nam': rest_nam,
                'file_url':file_url,
                'file_name':file_name,
            }
            return render(request,'qr_result.html',context)
    else:
        form =  QR_Code_Form()
        context = {
           'form':form,
        }
        return render(request,"genrate_qr_code.html",context)
