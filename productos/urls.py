from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("productos",views.list,name="list_product"),
    path("",views.list,name="list_product"),
    path("productos/<int:pk>",views.listDetail,name="product_detail"),
    path("searchProduct",views.searchProduct,name="searchProduct"),
    path("productos/<slug:category>",views.getByCatgorias,name="getByCategory"),
    path("about",views.about,name="about"),
    path("contacto",views.contacto,name="contacto"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)