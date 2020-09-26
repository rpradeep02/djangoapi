from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import string
import random
import json

from app1.models import User, Activity

def app1(request):
    return render(request, 'index.html')

def get_details(request, code):
    if request.method == 'GET':
        try:
            user = User.objects.get(no=code)
            activity_detail = Activity.objects.get(no=code)
            response = json.dumps([{'id':user.no, 'real_name':user.real_name, 'tz':user.tz, 'start_time':activity_detail.start_time, 'end_time':activity_detail.end_time}])
        except:
            response = json.dumps([{ 'Error': 'No such user found'}])
    return HttpResponse(response, content_type='text/json')

def get_all_details(request):
    if request.method == 'GET':
        try:
            user = User.objects.all()
            activity_detail = Activity.objects.all()
            result = []
            for _user, _activity in zip(user, activity_detail):
                result.append({'id':_user.no, 'real_name':_user.real_name, 'tz':_user.tz, 'start_time':_activity.start_time, 'end_time':_activity.end_time})
            response = json.dumps(result)
        except:
            response = json.dumps([{ 'Error': 'No such user found'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_user(request):
    if request.method == 'GET':
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        names = ["David","John","Paul","Mark","Andrew","Scott","Steven","Robert","Stephen","William","Craig","Michael","Stuart","Christopher","Alan","Colin","Brian","Kevin","Gary","Richard","Derek","Martin","Thomas","Neil","Barry","Ian","Jason","Iain"]
        real_name = random.choice(names)
        timezones = ["(GMT -12:00) Eniwetok, Kwajalein", "(GMT -11:00) Midway Island, Samoa", "(GMT -10:00) Hawaii", "(GMT -8:00) Pacific Time (US & Canada)", "(GMT -6:00) Central Time (US & Canada), Mexico City", "(GMT -5:00) Eastern Time (US & Canada), Bogota, Lima", "(GMT -3:30) Newfoundland"]
        tz = random.choice(timezones)

        min_year=1900
        max_year=datetime.now().year

        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year+1
        end = start + timedelta(days=365 * years)

        start_time = start + (end - start) * random.random()
        end_time = start + (end - start) * random.random()

        user = User(no=code, real_name=real_name, tz=tz)
        activity_period = Activity(no=code, start_time=start_time, end_time=end_time)
        try:
            user.save()
            activity_period.save()
            response = json.dumps([{ 'User added successfully! -' : code}])
        except:
            response = json.dumps([{ 'Error': 'User could not be added!'}])
    return HttpResponse(response, content_type='text/json')