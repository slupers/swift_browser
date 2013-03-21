# Create your views here.Q
from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.shortcuts import render_to_response, redirect
from swift import Swift


def display_meta(request):
    conts_and_objs = {}
    cont_meta = {}
    obj_meta = {}

    sw = Swift()
    acct_data = sw.get_acct()
	
	# traverse containers
    for cont in acct_data[1]:
        cont_data = sw.get_cont(cont['name'])

        # store container's meta as html
        cont_meta[cont['name']] = '<ul><ul>'
        for k,v in cont_data[0].iteritems():
            cont_meta[cont['name']] += '<li>'+str(k)+' : '+str(v)+'</li>'
        cont_meta[cont['name']] += '</ul></ul>'

        obj_names = []

		# traverse objects
        for obj in cont_data[1]:
            obj_names.append(obj['name'])

            obj_data = sw.get_obj(cont['name'], obj['name'])
            # store object's meta as html
            obj_meta[obj['name']] = '<ul>'
            for k,v in obj_data[0].iteritems():
                obj_meta[obj['name']] += '<li>'+str(k)+' &nbsp;:&nbsp;'+str(v)+'</li>'
            obj_meta[obj['name']] += '</ul>'

        conts_and_objs[cont['name']] = obj_names

    return render_to_response('show_data.html', {'conts_and_objs' : conts_and_objs, 'cont_meta' : cont_meta, 'obj_meta' : obj_meta})