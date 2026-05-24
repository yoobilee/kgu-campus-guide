from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name = 'home'),
    path('club', views.clubView, name = 'club'),
    path('facility', views.facilityView, name = 'facility'),
    path('facility_cafeteria', views.facilityCafeteria, name = 'facility_cafeteria'),
    path('facility_beverage', views.facilityBeverage, name = 'facility_beverage'),
    path('facility_lecture', views.facilityLecture, name = 'facility_lecture'),
    path('facility_etc', views.facilityEtc, name = 'facility_etc'),
    path('facility_facilities', views.facilityFacilities, name = 'facility_facilities'),
    path('graduate', views.Graduate, name = 'graduate'),
    path('graduate_freshman', views.GraduateFreshman, name = 'graduate_freshman'),
    path('graduate_transferman', views.GraduateTransferman, name = 'graduate_transferman'),
    path('outside', views.outsideView, name = 'outside'),
    path('outside_frontgate', views.outsideFront, name = 'outside_frontgate'),
    path('outside_front_restaurant', views.outsideFrontRestaurant, name = 'outside_front_restaurant'),
    path('outside_front_cafe', views.outsideFrontCafe, name = 'outside_front_cafe'),
    path('outside_backgate', views.outsideBack, name = 'outside_backgate'),
    path('outside_back_restaurant', views.outsideBackRestaurant, name = 'outside_back_restaurant'),
    path('outside_back_cafe', views.outsideBackCafe, name = 'outside_back_cafe'),
    path('major', views.MajorSite, name = 'major'),
    path('planBMenu', views.planBMenu, name = 'planBMenu'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

