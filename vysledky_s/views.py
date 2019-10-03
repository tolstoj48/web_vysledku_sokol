from django.shortcuts import get_object_or_404,render, get_list_or_404
from .models import Utkani, Tabulka, Rozpis
from collections import Counter
from django.views import generic
from datetime import date, timedelta
from vysledky_s.utils import helper, helper_get_seznam_hracu_tymu, helper_tabulka
from django.http import JsonResponse
import time
import datetime

def takeElem(elem):
		return int(elem.kolo)

def hlavni(request, sezona = "2019-2020"): #menit s novou sezonou
	s = get_list_or_404(Utkani)
	context = {"sezona": sezona}
	return render(request, "vysledky_s/base.html", context)

def rozpisy(request, sezona = "2019-2020"): #menit s novou sezonou
	s = get_list_or_404(Rozpis)
	startdate = date.today()
	enddate = startdate + timedelta(days = 6)
	context = {"sezona": sezona, "rozpis": s, "startdate": startdate, "enddate":enddate}
	return render(request, "vysledky_s/rozpis.html", context)

def uvodni_sezona(request, sezona):
	s = get_list_or_404(Utkani)
	context = {"sezona": sezona}
	return render(request, "vysledky_s/uvodni.html", context)

def tym(request, tyms, sezona):
	u = get_list_or_404(Utkani, tym__exact = tyms, sezona__exact = sezona)
	u.sort(key=takeElem)
	shooters=helper(u)
	tabulka=get_object_or_404(Tabulka, tym__exact = tyms, sezona__exact = sezona)
	tabulka=helper_tabulka(tabulka)
	context = {"u": u, "list_strelci": shooters, "tabulka": tabulka, "sezona": sezona}
	return render(request, "vysledky_s/vysledky_tymu.html", context)

def detail(request, id, tyms, sezona):
    u = get_object_or_404(Utkani, id__exact = id, sezona__exact = sezona)
    s = get_list_or_404(Utkani, sezona__exact = sezona)
    best_shooters = helper(s)
    context = {"u": u, "nejlepsi_strelci": best_shooters[:10], "sezona": sezona}
    return render(request, 'vysledky_s/detail.html', context)

def strelci(request, sezona):
	tymy_list = ["A-tým", "B-tým", "C-tým", "Starší dorost", "Mladší dorost", "Starší žáci", "Mladší žáci A", "Mladší žáci B", "Mladší žáci C"]
	if sezona == "2018-2019":
		tymy_list = tymy_list[:4] + tymy_list[5:] # uprava dle sezony - vyjmout ty tymy, ktere nehraly danou sezonu
	finalni=[]
	finalni_seznam_hraci = []
	k = get_list_or_404(Utkani, sezona__exact = sezona)
	best_shooters = helper(k)
	if sezona == "2019-2020":
		tymy_list = ["A-tým", "B-tým", "C-tým", "Starší dorost", "Mladší dorost", "Starší žáci", "Mladší žáci A", "Mladší žáci B", "Mladší žáci C"] #nutno upravit, az budou nabihat dalsi tymy zacatky
	for i in tymy_list:
		s = get_list_or_404(Utkani, tym__exact = i, sezona__exact = sezona)
		finalni.append(helper(s))
		finalni_seznam_hraci.append(helper_get_seznam_hracu_tymu(s))
	context = {"nejlepsi_strelci": finalni, "club_strelci": best_shooters[:10], "seznam_hracu_tymu": finalni_seznam_hraci, "sezona": sezona}
	return render(request, "vysledky_s/strelci.html", context)

def nehrano_2018_2019(request): # kazdou sezonu pridat na zacatku a propojit s urls.py
	context = {"sezona": "2018-2019"}
	return render(request,'vysledky_s/nehrano.html', context)

def zatim_nehrano_2019_2020(request): # kazdou sezonu pridat na zacatku a propojit s urls.py
	context = {"sezona": "2019-2020"}
	return render(request,'vysledky_s/zatim_nehrano.html', context)

def appis(request, hodnota): #nutno upravovat pro aplikaci android
	switcher = {0: "Pondělí", 1: "Úterý", 2: "Středa", 3: "Čtvrtek", 4: "Pátek", 5: "Sobota", 6: "Neděle", 7: "Nic"}
	if hodnota == "tymy":
		utkani = Utkani.objects.filter(tym__in = ['A-tým', 'B-tým', 'C-tým'], sezona = "2019-2020").values()
		utkani_list = list(utkani)
		return JsonResponse(utkani_list, safe = False)
	elif hodnota =="aktualni_rozpis":
		startdate = date.today()
		enddate = startdate + timedelta(days = 6)
		rozpisy = Rozpis.objects.filter(datum__range = [startdate, enddate]).values()
		rozpisy_list = list(rozpisy)
		vysledek_final = []
		final = []
		for i in rozpisy_list:
			day = datetime.datetime.weekday(i["datum"])
			den = switcher[day]
			x = [str(i["tym"]) + " | " + den + " | " + str(i["datum"]) + 
			" | " + i["cas"] + " | " + i["domaci"] + " - " + i["hoste"] + " \n\n"]
			final += x
		vysledek_final.append(final)
		return JsonResponse(vysledek_final, safe = False)
	else:
		tymy = ["A-tým", "B-tým", "C-tým", "Starší dorost", "Mladší dorost", 
		"Starší žáci", "Mladší žáci A", "Mladší žáci B", "Mladší žáci C"]
		a, b, c, st_d, ml_d, st_z, ml_z_a, ml_z_b, ml_z_c = [],[],[],[],[],[],[],[],[]
		vysledek = [a, b, c, st_d, ml_d, st_z, ml_z_a, ml_z_b, ml_z_c]
		helper_variable = 0
		for i in tymy:
			rozpisy = Rozpis.objects.filter(tym__exact = i).values()
			rozpisy_list = list(rozpisy)
			vysledek[helper_variable] = rozpisy_list
			helper_variable += 1
		vysledek_final = []
		for i in vysledek:
			final = []
			for f in i:
				day = datetime.datetime.weekday(f["datum"])
				den = switcher[day]
				x = [den + " | " + str(f["datum"]) + " | " + f["cas"] + " | " + f["domaci"] + " - " + f["hoste"] + " \n\n"]
				final += x
			vysledek_final.append(final)
		return JsonResponse(vysledek_final, safe = False)