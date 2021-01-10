from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .models import Item
from .models import AppleCartadmin
from .models import Order
from django.shortcuts import reverse
import datetime
from django.db.models import Q
import random as rn
def shop(request):   
    try:
        products=Item.objects.filter(item_p=1)
        params={'item':products} 
        return render(request,"client/client.htm",params)   
    except:
        print("hello")  
def about(request):
    try:
        return render(request,"client/about.htm")
    except:
        print("hello")


def details(request):
    try:
        return render(request,"client/details.htm")
    except:
        print("hello")    
def entry(request):
    try:
        email=request.POST.get('email',False)
        password=request.POST.get('password',False)
        name=request.POST.get('name',False)
        ur=User(email=email,password=password,name=name)
        ur.save()
        return render(request,"client/clientLogin.htm")
    except:
        print("hello")    
def buy(request):
    try:
        product_name=request.POST.get('pro_name')
        product_image=request.POST.get('pro_image')
        product_desc=request.POST.get('pro_desc')
        product_price=request.POST.get('pro_price')
        name=request.POST.get('name')
        email=request.POST.get('email')
        datentime=datetime.datetime.now()
        datentime=str(datentime)
        lis=list(datentime.split(" "))
        t=lis[0]
        li=list(t.split('-'))
        Date=li[2]+"-"+li[1]+"-"+li[0]
        if(product_image==None or product_name==None or product_desc==None or product_price==None):
            return render(request,"client/error.htm")
    
        params={'name':product_name,'image':product_image,'desc':product_desc,'price':product_price,'Uname':name,'email':email,'date':Date,'time':lis[1]}
        return render(request,"client/buy.htm",params)
    except:
        return render(request,"client/error.htm")   
def server(request):
    try:
        return render(request,"client/admin.htm")
    except:
      return render(request,"client/error.htm")   
def control(request):
    try:
        all_orders=Order.objects.all()
        all_products=Item.objects.all()
        params={'items':all_products,'orders':all_orders}
        email=request.POST.get('email',False)
        password=request.POST.get('password',False)
        if request.method=="POST":
            if(AppleCartadmin.objects.filter(email__exact=email,password__exact=password)):
                return render(request,"client/adminHome.htm",params)     
            else:
                context={"error":"who are you? your not a admin of AppleCart"}
                return  render(request,"client/admin.htm",context) 
    except:
       return render(request,"client/error.htm")        
def order(request):
    try:
        uname=request.POST.get('name')
        email=request.POST.get('email')
        item_name=request.POST.get('item_name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        area=request.POST.get('area')
        city=request.POST.get('city')
        landmark=request.POST.get('landmark')
        pincode=request.POST.get('pincode')
        district=request.POST.get('district')
        state=request.POST.get('state')
        date=request.POST.get('date')
        time=request.POST.get('time')
        phno=request.POST.get('phno')
        userdate=request.POST.get('userdate')
        count=0
        if (uname=="" or email=="" or uname=="None" or email=="None"):
            return render(request,"client/problem.htm") 
        if(str(userdate)==str(date)):
            scam=""
        else:
            scam="you change today's date you cannot cheat ApppleCart Developers! Last Warning for you "
            count=1
            date=str(date) 
        lis=list(date.split("-"))
        dATE=lis[0]+"-"+lis[1]+"-"+lis[2]
        number=rn.randint(3,6)
        dlv=int(lis[0])+number
        del_date=str(dlv)+"-"+lis[1]+"-"+lis[2]       
        con=Order(user_name=uname,user_email=email,user_number=phno,area=area,Landmark=landmark,pincode=pincode,city=city,district=district,state=state,order_date=dATE,order_time=time,item_name=item_name,item_price=price,item_desc=desc,delivery_date=del_date)
        con.save()
        params={'name':uname,'item':item_name,'email':email,'price':price,'scam':scam,'count':count,'del':del_date}
        return render(request,"client/order.htm",params)
    except:
        return render(request,"client/error.htm")   
def delete(request):
    try:
        if request.method=="POST":
            item=request.POST.get('search')
            con=Item.objects.get(item_name__exact=item)
            con.delete()
            return render(request,"client/adminHome.htm")
    except:
        return render(request,"client/error.htm")         
def save(request):
    try:
        name=request.POST.get('name')
        price=request.POST.get('price')
        item_p=request.POST.get('item_p')
        desc=request.POST.get('desc')
        image=request.POST.get('image')
        con=Item(item_name=name,price=price,item_p=item_p,item_desc=desc,item_image=image)
        con.save()
        return HttpResponse("<h3>item inserted</h3>")
    except:
        print("hello")        
def login(request):
    try:
        return render(request,"client/clientLogin.htm")
    except:
       return render(request,"client/error.htm") 
def val(request):
    try:
        email=request.POST.get('email',False)
        password=request.POST.get('password',False)
        if(User.objects.filter(email__exact=email,password__exact=password)):
            name=User.objects.filter(email__exact=email,password__exact=password)
            myname=name[0].name
            myemail=name[0].email
            prams={'name':myname,'email':myemail}
            return render(request,"client/return.htm",prams)   
        else:
            context={"error":"No account found for this email"}
            return  render(request,"client/clientLogin.htm",context)    
    except:
        print("hello")
def search(request):
    try:
        search_key=request.POST.get('search')
        items=Item.objects.filter(item_name__contains=search_key) | Item.objects.filter(item_desc__contains=search_key) |Item.objects.filter(price__contains=search_key)
        if(len(items)==0):
            return render(request,"client/search.htm")
        params={'item':items}
        return render(request,"client/client.htm",params)
    except:
        return render(request,"client/error.htm")      
def logout(request):
    try:
        return render(request,"client/logout.htm") 
    except:
        print("hello")       
def cart(request):
    try:
        return render(request,"client/cart.htm")
    except:
        return render(request,"client/error.htm")    
def catogories_1(request):
    try:
        catagory="vagitables"
        items=Item.objects.filter(item_catagory__exact=catagory)
        if(len(items)==0):
            return render(request,"client/search.htm")
        params={'item':items}
        return render(request,"client/client.htm",params)
    except:
        print("hello")   
def catogories_2(request):
    try:
        catagory="meat"
        items=Item.objects.filter(item_catagory__exact=catagory)
        if(len(items)==0):
            return render(request,"client/search.htm")
        params={'item':items}
        return render(request,"client/client.htm",params)
    except:
       return render(request,"client/error.htm")      
def catogories_3(request):
    try:
        catagory="snacks"
        items=Item.objects.filter(item_catagory__exact=catagory)
        if(len(items)==0):
            return render(request,"client/search.htm")
        params={'item':items}
        return render(request,"client/client.htm",params)
    except:
        print("hello")      
def catogories_4(request):
    try:
        catagory="beverages"
        items=Item.objects.filter(item_catagory__exact=catagory)
        if(len(items)==0):
            return render(request,"client/search.htm")
        params={'item':items}
        return render(request,"client/client.htm",params)
    except:
       return render(request,"client/error.htm")   
def catogories_5(request):
    try:
        catagory="bakery"
        items=Item.objects.filter(item_catagory__exact=catagory)
        if(len(items)==0):
            return render(request,"client/search.htm")
        params={'item':items}

        return render(request,"client/client.htm",params)
    except:
        return render(request,"client/error.htm")     
def catogories_6(request):
    try:
        catagory="masala"
        items=Item.objects.filter(item_catagory__exact=catagory)
        if(len(items)==0):
            return render(request,"client/search.htm")
        params={'item':items}
        return render(request,"client/client.htm",params)
    except:
        return render(request,"client/error.htm")                                            