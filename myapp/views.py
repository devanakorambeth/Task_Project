from django.shortcuts import render
import json 
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class BMIView(View):
    def post(self,request):
        data=json.loads(request.body)
        
        h=data.get("height")
        w=data.get("weight")
        
        # Convert height from cm to meter
        height=h/100
        
        #calculate BMI
        bmi=w/(height**2)
        
        result={
            "Height":data.get('height'),
            "Weight":w,
            "BMI":round(bmi ,2)
        }
        
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class AgeCalculator(View):

    def post(self, request):
        data = json.loads(request.body)

        b = data.get("birth_year")
        c = data.get("current")

        age = c - b

        result = {
            "birth_year": b,
            "current": c,
            "Age": age
        }

        return JsonResponse(result)

    

@method_decorator(csrf_exempt, name='dispatch')
class SimpleInterest(View):
    def post(self, request):
        data = json.loads(request.body)

        p = data.get("principal")
        r = data.get("rate")
        t = data.get("time")

        simpleinterest = (p * r * t) / 100

        result = {
            "principal": p,
            "rate": r,
            "time": t,
            "simpleinterest": simpleinterest
        }

        return JsonResponse(result)

        
@method_decorator(csrf_exempt, name='dispatch')
class Percentage(View):
    def post(self, request):
        data = json.loads(request.body)

        O = data.get("obtained_marks")
        T = data.get("total_marks")

        Percentage =(O/T)*100

        result = {
            "obtained_marks": O,
            "total_marks": T,
            "Percentage": Percentage
        }

        return JsonResponse(result)       
    
    
@method_decorator(csrf_exempt, name='dispatch')
class Electricity(View):
    def post(self, request):
        data = json.loads(request.body)

        u = data.get("units")
        r = data.get("rate")

        Bill =u*r

        result = {
            "units": u,
            "rate": r,
            "Bill": Bill
        }

        return JsonResponse(result)      
    
     

@method_decorator(csrf_exempt, name='dispatch')
class Discount(View):
    def post(self, request):
        data = json.loads(request.body)

        p = data.get("price")
        d = data.get("discount_percentage")

        Discount_amount =p*d/100
        Final_price=p-Discount_amount
        
    
        result = {
            "price": p,
            "discount_percentage": d,
            "discount_amount": Discount_amount,
            "final_price": Final_price
        }

        return JsonResponse(result)  
    
    
@method_decorator(csrf_exempt, name='dispatch')
class ProfitCalculator(View):
    def post(self, request):
        data = json.loads(request.body)

        c = data.get("cost_price")
        s = data.get("selling_price")

        Profit=s-c
        
    
        result = {
            "cost_price": c,
            "selling_price": s,
            "profit": Profit
        }

        return JsonResponse(result)  
    
@method_decorator(csrf_exempt, name='dispatch')
class SalaryCalculator(View):
    def post(self, request):
        data = json.loads(request.body)

        basic = data.get("basic_salary")
        bonus = data.get("bonus")
        d = data.get("deduction")

        Net_salary=basic+bonus-d
        
    
        result = {
            "basic_salary": basic,
            "bonus": bonus,
            "deduction": d,
            "Net_salary":Net_salary
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class TimeConverter(View):
    def post(self, request):
        data = json.loads(request.body)

        hours = data.get("hours")
               
        minutes=hours*60
        seconds=hours*3600
        
        result = {
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class FuelCostCalculator(View):
    def post(self, request):
        data = json.loads(request.body)

        d= data.get("distance")
        m= data.get("mileage")
        fp= data.get("fuel_price")
        
               
        fuel_required=d/m
        total_cost=fuel_required*fp
        
        result = {
            "distance": d,
            "mileage": m,
            "fuel_price": fp,
            "fuel_required":fuel_required,
            "total_cost":total_cost
            
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class Product(View):
    def post(self, request):
        data = json.loads(request.body)

        cost= data.get("cost_price")
        selling= data.get("selling_price")
        q= data.get("quantity")
        
        total_cost = cost*q
        total_sales = selling*q
        Profit = total_sales - total_cost 
        
        result = {
            "cost_price": cost,
            "selling_price": selling,
            "quantity": q,
            "total_cost":total_cost,
            "total_sales":total_sales,
            "Profit":Profit 
            
        }

        return JsonResponse(result)
    
    
@method_decorator(csrf_exempt, name='dispatch')
class Worksalary(View):
    def post(self, request):
        data = json.loads(request.body)

        hours_worked= data.get("hours_worked")
        regular_hours= data.get("regular_hours")
        hourly_rate= data.get("hourly_rate")
        overtime_rate= data.get("overtime_rate")
        
        regular_pay = regular_hours * hourly_rate 
        overtime_hours = hours_worked - regular_hours 
        overtime_pay = overtime_hours * overtime_rate 
        total_salary = regular_pay + overtime_pay     
        
        result = {
            "hours_worked": hours_worked,
            "regular_hours": regular_hours,
            "hourly_rate": hourly_rate,
            "overtime_rate":overtime_rate,
            "regular_pay":regular_pay,
            "overtime_hours":overtime_hours,
            "overtime_pay":overtime_pay,
            "total_salary":total_salary
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class Agedayscalculator(View):
    def post(self, request):
        data = json.loads(request.body)

        age= data.get("age")
              
        months=age*12
        week=age*52
        days=age*365
        
        result = {
            "age": age,
            "months": months,
            "week": week,
            "days":days
        }

        return JsonResponse(result)
    