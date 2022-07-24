from django.shortcuts import render
from django.http import JsonResponse
import json
from pathlib import Path
import os
import sqlite3
from .forms import NewUserForm, Query

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def index(request):
    if request.method == 'GET':
        form = Query()
        args = {}
        # args.update(csrf(request))
        args['form'] = form

        # return render_to_response('profile.html',args)

        return render(request,'scraper_app/index.html',args)
    if request.method == 'POST':
        search_form = Query(request.POST)

        if not search_form.is_valid():
            return render(request,'scraper_app/index.html')
        else:
            search_term = search_form.cleaned_data['search_input']
            # print('search input: ' + search_form.cleaned_data['search_input'])
        # json_data = open('igem_team_new.json')
        # print(json_data)
        #
        # list = json.loads(json_data)

        with open("igem_team_new.json", "r") as file:
            fileData  = file.read()
            jsonData = json.loads(fileData)

        answer = []
        for i in jsonData:
            count = i['title'].count(search_term)
            count = count + i['abstract'].count(search_term)
            if not count:  # if count is '', 0, or null
                continue

            sentence = None
            sentence_list = i['abstract'].split('.')
            for s in sentence_list:
                if search_term in s:
                    sentence = s + '.'
                    break

            answer.append({
                'title': i['title'],
                'count': count,
                'url': i['url'],
                'team': i['team'],
                'sentence': sentence})

        newlist = sorted(answer, key=lambda k: k['count'], reverse=True)
        new_dict = {"res":newlist}
        return render(request,'scraper_app/searched.html',context=new_dict)

def searched(request):
    if request.method == 'GET':
        form = Query()
        args = {}
        # args.update(csrf(request))
        args['form'] = form

        # return render_to_response('profile.html',args)

        return render(request,'scraper_app/index.html',args)
    if request.method == 'POST':
        search_form = Query(request.POST)

        if not search_form.is_valid():
            return render(request,'scraper_app/index.html')
        else:
            search_term = search_form.cleaned_data['search_input']
            print('search input: ' + search_form.cleaned_data['search_input'])

        with open("igem_team_new.json", "r") as file:
            fileData  = file.read()
            jsonData = json.loads(fileData)

        answer = []
        for i in jsonData:
            count = i['title'].count(search_term)
            count = count + i['abstract'].count(search_term)
            if not count:  # if count is '', 0, or null
                continue

            sentence = None
            sentence_list = i['abstract'].split('.')
            for s in sentence_list:
                if search_term in s:
                    sentence = s + '.'
                    break

            answer.append({
                'title': i['title'],
                'count': count,
                'url': i['url'],
                'team': i['team'],
                'sentence': sentence})

        newlist = sorted(answer, key=lambda k: k['count'], reverse=True)
        new_dict = {"res":newlist}
        return render(request,'scraper_app/searched.html',context=new_dict)

def api(request):
    if request.method == 'GET':

        search_term = request.GET.get('search_input')
        if search_term is None:
            return JsonResponse({'data': []})
        # search_form.cleaned_data['search_input']
            # print('search input: ' + search_form.cleaned_data['search_input'])
        # json_data = open('igem_team_new.json')
        # print(json_data)
        #
        # list = json.loads(json_data)

        with open("igem_team_new.json", "r") as file:
            fileData  = file.read()
            jsonData = json.loads(fileData)

        answer = []
        for i in jsonData:
            count = i['title'].count(search_term)
            count = count + i['abstract'].count(search_term)
            if not count:  # if count is '', 0, or null
                continue

            sentence = None
            sentence_list = i['abstract'].split('.')
            for s in sentence_list:
                if search_term in s:
                    sentence = s + '.'
                    break

            answer.append({
                'title': i['title'],
                'count': count,
                'url': i['url'],
                'team': i['team'],
                'abstract': sentence})

        newlist = sorted(answer, key=lambda k: k['count'], reverse=True)
        return JsonResponse({'data': newlist})
