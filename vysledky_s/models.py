from django.db import models
from django.contrib import admin

class Utkani(models.Model):
	sezona=models.CharField(max_length=100)
	tym=models.CharField(max_length=100)
	soutez=models.CharField(max_length=200)
	kolo=models.CharField(max_length=50)
	datum=models.CharField(max_length=100)
	souperi=models.CharField(max_length=300)
	vysledek=models.CharField(max_length=50)
	sestava=models.CharField(max_length=700)
	nahradnici=models.CharField(max_length=500)
	goly=models.CharField(max_length=300, blank=True)
	koment=models.TextField(max_length=5000, blank=True)

	def posledni_sezona(self):
		return self.sezona=="2018/2019"

	def __str__(self):
		datum_zkracene=str(self.datum)
		vystup1=self.sezona+", "+self.tym+", "+self.soutez
		vystup2=self.kolo+", "+datum_zkracene[:11]+", "+self.souperi+", "+self.sestava+", "+self.nahradnici+", "+self.goly
		return vystup1+vystup2

class UtkaniAdmin(admin.ModelAdmin):
	list_display=("tym", "datum", "souperi", "sestava")
	search_fields=["tym", "goly", "sestava"]

class Tabulka(models.Model):
	sezona=models.CharField(max_length=100, default="2018-2019")
	poradi=models.CharField(max_length=100)
	tymy=models.CharField(max_length=500)
	pocet_utkani=models.CharField(max_length=100)
	pocet_vyher=models.CharField(max_length=100)
	pocet_remiz=models.CharField(max_length=100)
	pocet_proher=models.CharField(max_length=100)
	skore=models.CharField(max_length=200)
	body=models.CharField(max_length=150)
	tym=models.CharField(max_length=50) #nutno pro filtrovani urcit, co je to za tym v ramci sokola
	kolo=models.CharField(max_length=10) #pokud bude vice tabulek pro jeden tym, pak je nutne je odlisit po jakem kole to je -> na filtrovani

	def __str__(self):
		tym=self.tym
		kolo=self.kolo[:2]
		return tym+" - kolo:"+kolo

class Rozpis(models.Model):
	tym = models.CharField(max_length=100)
	soutez = models.CharField(max_length=200)
	datum = models.DateField()
	cas = models.CharField(max_length=50)
	domaci = models.CharField(max_length=100)
	hoste = models.CharField(max_length=100)

	def __str__(self):
		tym = self.tym
		datum = self.datum
		return tym + " - kolo:" + str(datum)