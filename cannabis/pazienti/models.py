from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


SESSO = (
    ('M', _("Maschio")),
    ('F', _("Femmina")),
)

TITOLO_DI_STUDIO = (
    ('0', _("Elementari")),
    ('1', _("Licenza Media Inferiore")),
    ('2', _("Licenza Media Superiore")),
    ('3', _("Laurea")),
)

PATOLOGIA = (
    ('0', _("Dolore neuropatico cronico")),
    ('1', _("Patologia oncologica")),
    ('2', _("Spasticità dolorosa")),
    ('3', _("Sindrome fibromialgica")),
    ('4', _("Cefalea")),
)

SOMMINISTRAZIONE = (
    ('0', _("Orale - Cartine")),
    ('1', _("Orale - Capsule apribili")),
    ('2', _("Orale - Olio")),
    ('3', _("Inalazione")),
)


class Paziente(models.Model):
    num_paziente = models.CharField(
    	verbose_name=_(u"N° Paziente"), 
    	max_length=10, blank=True, null=True
    )
    num_cartella = models.CharField(
    	verbose_name=_(u"N° Cartella"), 
    	max_length=100, blank=True, null=True
    )
    nome = models.CharField(
    	verbose_name=_(u"Nome"), 
    	max_length=10, blank=True, null=True
    )
    cognome = models.CharField(
    	verbose_name=_(u"Cognome"), 
    	max_length=100, blank=True, null=True
    )
    sesso = models.CharField(
    	verbose_name=_(u"Sesso"), 
    	max_length=1, blank=True, null=True, choices=SESSO
    )
    data_nascita = models.DateField(
    	verbose_name=_(u'Data di nascita'), 
    	blank=True, null=True
    )
    eta = models.CharField(
    	verbose_name=_(u"Età"), 
    	max_length=2, blank=True, null=True
    )
    luogo_nascita = models.CharField(
    	verbose_name=_(u"Luogo di nascita"), 
    	max_length=100, blank=True, null=True
    )
    lavoro = models.CharField(
    	verbose_name=_(u"Lavoro"), 
    	max_length=100, blank=True, null=True
    )
    titolo_studio = models.CharField(
    	verbose_name=_(u"Titolo di studio"), 
    	max_length=1, blank=True, null=True, choices=TITOLO_DI_STUDIO
    )
    patologia = models.CharField(
    	verbose_name=_(u"Patologia"), 
    	max_length=1, blank=True, null=True, choices=PATOLOGIA
    )
    descrizione_patologica = models.TextField(
    	verbose_name=_(u"Descrizione patologia"), null=True, blank=True
    )
    eta_insorgenza = models.CharField(
    	verbose_name=_(u"Età anagrafica all'insorgenza della patologia dolorosa"), 
    	max_length=2, blank=True, null=True
    )
    altre_patologie = models.TextField(
    	verbose_name=_(u"Altre patologie"), 
    	null=True, blank=True
    )
    trattamenti = models.TextField(
    	verbose_name=_(u"Trattamenti farmacologici in corso"), 
    	null=True, blank=True
    )
    posologia = models.CharField(
    	verbose_name=_(u"Posologia (mg/die)"), 
    	max_length=10, blank=True, null=True
    )
    num_somministrazioni = models.CharField(
    	verbose_name=_(u"Numero di somministrazioni/die"), 
    	max_length=300, blank=True, null=True
    )	
    data_trattamento = models.DateField(
    	verbose_name=_(u'Data di inizio trattamento'), 
    	blank=True, null=True
    )
    modalita_somministrazione = models.CharField(
    	verbose_name=_(u"Modalità di somministrazione"), 
    	max_length=1, blank=True, null=True, choices=SOMMINISTRAZIONE
    )
    utilizzo_cannabis = models.NullBooleanField(
    	verbose_name=_(u"Utilizzo cannabis prescritta per terapia orale anche \
    		con altre modalità di somministrazione (es. per smoking)"), 
    	null=True, blank=True
    )
    tempo_prelievo = models.CharField(
		verbose_name=_(u"Tempo trascorso tra l'assunzione della cannabis e il \
			prelievo ematico (minuti)"), 
		max_length=100, blank=True, null=True
	)
    modalita_ultima_assunzione = models.CharField(
		verbose_name=_(u"Modalità ultima assunzione"), 
		max_length=100, blank=True, null=True
	)
    conc_thc_sangue = models.CharField(
		verbose_name=_(u"Concentrazione THC - Sangue intero"), 
		max_length=100, blank=True, null=True
	)
    conc_thc_dbs = models.CharField(
		verbose_name=_(u"Concentrazione THC - DBS"), 
		max_length=100, blank=True, null=True
	)
    conc_11_oh_thc_sangue = models.CharField(
		verbose_name=_(u"Concentrazione 11-OH-THC - Sangue intero"), 
		max_length=100, blank=True, null=True
	)
    conc_11_oh_thc_dbs = models.CharField(
		verbose_name=_(u"Concentrazione 11-OH-THC - DBS"), 
		max_length=100, blank=True, null=True
	)
    conc_cbd_sangue = models.CharField(
		verbose_name=_(u"Concentrazione CBD - Sangue intero"), 
		max_length=100, blank=True, null=True
	)
    conc_cbd_dbs = models.CharField(
		verbose_name=_(u"Concentrazione CBD - DBS"), 
		max_length=100, blank=True, null=True
	)
    cannabis_ricreazionale = models.NullBooleanField(
		verbose_name=_(u"Attuale utilizzo di cannabis ricreazionale"), 
		null=True, blank=True
	)
    pregresso_utilizzo_ricreazionale = models.NullBooleanField(
		verbose_name=_(u"Pregresso utilizzo di cannabis ricreazonale"), 
		null=True, blank=True
	)
    uso_stupefacenti = models.NullBooleanField(
		verbose_name=_(u"Uso di sostanze stupefacenti"), 
		null=True, blank=True
	)
    note = models.TextField(
		verbose_name=_(u"Note"), 
    	null=True, blank=True
	)


    class Meta:
        verbose_name = _('Paziente')
        verbose_name_plural = _('Pazienti')
        ordering = ('num_paziente',)


    def __str__(self):
        if self.nome and self.cognome:
        	return '%s %s' % (self.nome, self.cognome)
        return 'Paziente anonimo'

    @property
    def nome_completo(self):
    	if self.nome and self.cognome:
    		return '%s %s' % (self.nome, self.cognome)
    	return 'Paziente anonimo'


class BPIForm(models.Model):
	paziente = models.ForeignKey(
    	Paziente, verbose_name=_('Paziente'), related_name='bpi_paziente'
    )
	nrs_1_t0 = models.CharField(
    	verbose_name=_(u"Dolore peggiore a T0"), 
    	max_length=2, blank=True, null=True
    )
	nrs_1_t1 = models.CharField(
    	verbose_name=_(u"Dolore peggiore a T1"), 
    	max_length=2, blank=True, null=True
    )
	nrs_2_t0 = models.CharField(
    	verbose_name=_(u"Dolore più lieve a T0"), 
    	max_length=2, blank=True, null=True
    )
	nrs_2_t1 = models.CharField(
    	verbose_name=_(u"Dolore più lieve a T1"), 
    	max_length=2, blank=True, null=True
    )
	nrs_3_t0 = models.CharField(
    	verbose_name=_(u"Dolore medio a T0"),
    	 max_length=2, blank=True, null=True
    )
	nrs_3_t1 = models.CharField(
    	verbose_name=_(u"Dolore medio a T1"),
    	max_length=2, blank=True, null=True
    )
	nrs_4_t0 = models.CharField(
    	verbose_name=_(u"Dolore al momento a T0"),
    	max_length=2, blank=True, null=True
    )
	nrs_4_t1 = models.CharField(
    	verbose_name=_(u"Dolore al momento a T1"), 
    	max_length=2, blank=True, null=True
    )
	sollievo_indotto_t0 = models.CharField(
    	verbose_name=_(u"% Sollievo indotto a T0"), 
    	max_length=4, blank=True, null=True
    )
	sollievo_indotto_t1 = models.CharField(
    	verbose_name=_(u"% Sollievo indotto a T1"), 
    	max_length=4, blank=True, null=True
    )
	attivita_generale_t0 = models.CharField(
    	verbose_name=_(u"Attività in generale a T0"), 
    	max_length=2, blank=True, null=True
    )
	attivita_generale_t1 = models.CharField(
    	verbose_name=_(u"Attività in generale a T1"), 
    	max_length=2, blank=True, null=True
    )
	umore_t0 = models.CharField(
    	verbose_name=_(u"Umore a T0"), max_length=2, blank=True, null=True
    )
	umore_t1 = models.CharField(
    	verbose_name=_(u"Umore a T1"), max_length=2, blank=True, null=True
    )
	camminare_t0 = models.CharField(
    	verbose_name=_(u"Capacità di camminare a T0"), 
    	max_length=2, blank=True, null=True
    )
	camminare_t1 = models.CharField(
    	verbose_name=_(u"Capacità di camminare a T1"), 
    	max_length=2, blank=True, null=True
    )
	lavoro_t0 = models.CharField(
    	verbose_name=_(u"Lavoro a T0"), max_length=2, blank=True, null=True
    )
	lavoro_t1 = models.CharField(
    	verbose_name=_(u"Lavoro a T1"), max_length=2, blank=True, null=True
    )
	relazioni_t0 = models.CharField(
    	verbose_name=_(u"Relazioni a T0"), max_length=2, blank=True, null=True
    )
	relazioni_t1 = models.CharField(
    	verbose_name=_(u"Relazioni a T1"), max_length=2, blank=True, null=True
    )
	sonno_t0 = models.CharField(
    	verbose_name=_(u"Sonno a T0"), max_length=2, blank=True, null=True
    )
	sonno_t1 = models.CharField(
    	verbose_name=_(u"Sonno a T1"), max_length=2, blank=True, null=True
    )
	gusto_vivere_t0 = models.CharField(
    	verbose_name=_(u"Gusto di vivere a T0"), 
    	max_length=2, blank=True, null=True
    )
	gusto_vivere_t1 = models.CharField(
    	verbose_name=_(u"Gusto di vivere a T1"), 
    	max_length=2, blank=True, null=True
    )
	altro = models.TextField(verbose_name=_(u"Altro"), null=True, blank=True)


	class Meta:
		verbose_name = _('BPI')
		verbose_name_plural = _('BPI')

	def __str__(self):
		return 'BPI'


class EventiAvversi(models.Model):
	paziente = models.ForeignKey(
    	Paziente, verbose_name=_('Paziente'), related_name='eventi_paziente'
    )
	tachicardia = models.BooleanField(
		verbose_name=_(u"Tachicardia"), default=False
	)
	ipotensione_post = models.BooleanField(
		verbose_name=_(u"Ipotensione posturale"), default=False
	)
	cefalea = models.BooleanField(
		verbose_name=_(u"Cefalea"), default=False
	)
	sonnolenza = models.BooleanField(
		verbose_name=_(u"Sonnolenza"), default=False
	)
	iper_congiuntivale = models.BooleanField(
		verbose_name=_(u"Iperemia congiuntivale"), default=False
	)
	tosse = models.BooleanField(
		verbose_name=_(u"Irritazione bronchiale, tosse"), default=False
	)
	astenia = models.BooleanField(
		verbose_name=_(u"Astenia"), default=False
	)
	disforia = models.BooleanField(
		verbose_name=_(u"Disforia"), default=False
	)
	crisi_ansia = models.BooleanField(
		verbose_name=_(u"Crisi di ansia e panico"), default=False
	)
	concentrazione = models.BooleanField(
		verbose_name=_(u"Difficoltà di concentrazione"), default=False
	)
	fauci = models.BooleanField(
		verbose_name=_(u"Secchezza delle fauci"), default=False
	)
	sonnolenza_sedazione = models.BooleanField(
		verbose_name=_(u"Sonnolenza, sedazione"), default=False
	)
	confusione = models.BooleanField(
		verbose_name=_(u"Stato confusionale"), default=False
	)
	amotivazione = models.BooleanField(
		verbose_name=_(u"Sindrome amotivazionale"), default=False
	)
	delirio = models.BooleanField(
		verbose_name=_(u"Crisi psicotica acuta / delirio"), default=False
	)
	altro = models.TextField(
	    verbose_name=_(u"Altro"), 
        null=True, blank=True
	)

    
	class Meta:
		verbose_name = _('Eventi Avversi')
		verbose_name_plural = _('Eventi Avversi')

	def __str__(self):
		return 'Eventi avversi'

	def attrs(self):
		for field in self._meta.fields:
			yield field.verbose_name, getattr(self, field.name)


class ModalitaDecotto(models.Model):
	paziente = models.ForeignKey(
    	Paziente, verbose_name=_('Paziente'), related_name='decotto_paziente',
    	blank=True, null=True
    )
	quantita_acqua = models.CharField(
		verbose_name=_(u'Quantità acqua (ml)'), 
		max_length=10, null=True, blank=True
	)
	sostanza_grassa = models.CharField(
		verbose_name=_(u'Sostanza grassa utilizzata (butto,latte, panna) e quantità (ml)'), 
		max_length=100, null=True, blank=True
	)
	tempo_impiegato = models.CharField(
		verbose_name=_(u'Tempo intercorso tra la preparazione del decotto (min)'), 
		max_length=5, null=True, blank=True
	)
	tempo_assunzione = models.CharField(
		verbose_name=_(u'Tempo intercorso tra la preparazione e l\'assunzione (min)'), 
		max_length=10, null=True, blank=True
	)


	class Meta:
	    verbose_name = _('Modalità decotto')
	    verbose_name_plural = _('Modalità decotto')

	def __str__(self):
		return 'Modalità decotto'
