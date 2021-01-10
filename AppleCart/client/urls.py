from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   path('',views.shop,name="shop"),
   path('about/',views.about,name="about"),
   path('details/',views.details,name="details"),
   path('login/details',views.details,name="details"),
   path('entry/',views.entry,name="entry"),
   path('entry/about/',views.about,name="about"),
   path('shop/details/',views.details,name="details"),
   path('shop/buy/',views.buy,name="buy"),
   path('server/',views.server,name="server"),
   path('server/control/',views.control,name="control"),
   path('server/control/delete',views.delete,name="delete"),
   path('shop/buy/order/',views.order,name="order"),
   path('server/control/save_in_db',views.save,name="save_in_db"),
   path('login/',views.login,name="login"),
   path('login/val',views.val,name="val"),
   path('shop/search',views.search,name="search"),
   path('shop/logout',views.logout,name="logout"),
   path('server/control/admin/',admin.site.urls),
   path('shop/catagory_1/',views.catogories_1,name="catogories_1"),
   path('shop/catagory_2/',views.catogories_2,name="catogories_2"),
   path('shop/catagory_3/',views.catogories_3,name="catogories_3"),
   path('shop/catagory_4/',views.catogories_4,name="catogories_4"),
   path('shop/catagory_5/',views.catogories_5,name="catogories_5"),
   path('shop/catagory_6/',views.catogories_6,name="catogories_6"),    
]