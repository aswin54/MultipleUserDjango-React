from django.urls import path

from RestApiapp.views import CustomerSignup, CustomAuthToken, CustomerOnlyView

urlpatterns = [
    path('CustomerSignup/',CustomerSignup.as_view()),
    path('login_view/',CustomAuthToken.as_view(),name='auth-token'),
    path('Customer_dashboard/',CustomerOnlyView.as_view()),
]