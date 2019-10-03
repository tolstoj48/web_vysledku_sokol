def test():
	pass

def helper(u):
	list_strelci=[]
	for i in u:
		branky=i.goly.split(",")
		list_strelci.append(branky)
	mezilist=[]
	for i in list_strelci:
		mezilist=mezilist+i
	final={}
	kerel=[]
	for i in mezilist:
		i=i.strip()
		kerel.append(i)
		pocet=kerel.count(i)
		if i not in final.keys():
			final[i]=pocet
		else:
			final.update({i: pocet})
	finalni={}
	finalni=sorted(final.items(), key=lambda x: x[1], reverse=True)
	finalni_k=[u[0].tym]
	for i in finalni:
		if i[0]=="bez vstřeleného gólu" or i[0]=="":
			pass
		else:
			finalni_k.append(i)
	return finalni_k

def helper_get_seznam_hracu_tymu(s):
	list_hracu=[]
	for i in s:
		hraci_zaklad_list=i.sestava.split(",")
		hraci_nahradnici_list=i.nahradnici.split(",")
		for k in hraci_zaklad_list:
			k=k.strip()
			if k in list_hracu:
				pass
			else:
				list_hracu.append(k)
		for k in hraci_nahradnici_list:
			k=k.strip()
			if k in list_hracu:
				pass
			else:
				list_hracu.append(k)
	list_hracu.append(s[0].tym)
	return list_hracu

def helper_tabulka(tabulka):
	list_tymy=[]
	finalni_list=[]
	f=len(tabulka.poradi)
	list_tymy.append(tabulka.poradi.split(","))
	list_tymy.append(tabulka.tymy.split(","))
	list_tymy.append(tabulka.pocet_utkani.split(","))
	list_tymy.append(tabulka.pocet_vyher.split(","))
	list_tymy.append(tabulka.pocet_remiz.split(","))
	list_tymy.append(tabulka.pocet_proher.split(","))
	list_tymy.append(tabulka.skore.split(","))
	list_tymy.append(tabulka.body.split(","))
	finalni_list=list(zip(list_tymy[0],list_tymy[1], list_tymy[2], list_tymy[3], list_tymy[4], list_tymy[5], list_tymy[6], list_tymy[7]))
	return finalni_list