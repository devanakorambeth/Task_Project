"""
URL configuration for Taskproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/',views.BMIView.as_view()),
    path('age/',views.AgeCalculator.as_view()),
    path('simpleinterest/',views.SimpleInterest.as_view()),
    path('percentage/',views.Percentage.as_view()),
    path('electricity/',views.Electricity.as_view()),
    path('discount/',views.Discount.as_view()),
    path('profit/',views.ProfitCalculator.as_view()),
    path('salary/',views.SalaryCalculator.as_view()),
    path('time/',views.TimeConverter.as_view()),
    path('fuel-cost/',views.FuelCostCalculator.as_view()),
    path('product-profit/',views.Product.as_view()),
    path('work-salary/',views.Worksalary.as_view()),
    path('age-details/',views.Agedayscalculator.as_view()),   
]
