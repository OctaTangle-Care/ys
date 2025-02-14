# # from django.urls import path
# # from .views import register_patient, register_doctor, upload_report, generate_api_key

# # urlpatterns = [
# #     path('register_patient/', register_patient, name='register_patient'),
# #     path('register_doctor/', register_doctor, name='register_doctor'),
# #     path('upload_report/', upload_report, name='upload_report'),
# #     path('generate_api_key/', generate_api_key, name='generate_api_key'),
# # ]

# from django.urls import path
# from .views import register_patient, register_doctor, upload_report, generate_api_key, list_api_keys
# # from ysweb.hospital import views
# from . import views  # Use relative import


# urlpatterns = [
#     path('',views.home,name="home"),
#     path('register_patient/', register_patient, name='register_patient'),
#     path('register_doctor/', register_doctor, name='register_doctor'),
#     path('upload_report/', upload_report, name='upload_report'),
#     path('generate_api_key/', generate_api_key, name='generate_api_key'),
#     path('list_api_keys/', list_api_keys, name='list_api_keys'),
# ]

from django.urls import path
from . import views
    
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.base, name='home'),
path('', views.home, name='home'),
path('patient', views.patient, name='patient'),
path('doctor', views.doctor, name='doctor'),
path('api', views.api, name='api'),
path('report', views.report, name='report'),

    # Patient Registration
    path('register_patient_view/', views.register_patient_view, name='register_patient_view'),
    # Doctor Registration
    path('register_doctor_view/', views.register_doctor_view, name='register_doctor_view'),
    # Upload Patient Reports
    path('upload_report_view/', views.upload_report_view, name='upload_report_view'),
   path('display_reports/', views.display_reports, name='display_reports'),
path('display_reports/', views.display_reports, name='display_reports'),

path('generate_api_key_view/', views.generate_api_key_view, name='generate_api_key_view'),
path('check_patient/', views.check_patient_record, name='check_patient'),

]
if settings.DEBUG:  # Serve media files only in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)