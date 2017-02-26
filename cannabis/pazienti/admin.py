from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import BPIForm, EventiAvversi, ModalitaDecotto, Paziente


class BPIFormInline(admin.StackedInline):
    model = BPIForm
    fields = (
    	('nrs_1_t0', 'nrs_1_t1'), ('nrs_2_t0', 'nrs_2_t1'),
    	('nrs_3_t0', 'nrs_3_t1'), ('nrs_4_t0', 'nrs_4_t1'),
    	('sollievo_indotto_t0', 'sollievo_indotto_t1'), 
    	('attivita_generale_t0', 'attivita_generale_t1'),
    	('umore_t0', 'umore_t1'), ('camminare_t0', 'camminare_t1'),
    	('lavoro_t0', 'lavoro_t1'), ('relazioni_t0', 'relazioni_t1'),
    	('sonno_t0', 'sonno_t1'), ('gusto_vivere_t0', 'gusto_vivere_t1'),
    	('altro'),
    )
    extra = 0


class EventiAvversiInline(admin.StackedInline):
    model = EventiAvversi
    fields = (
    	('tachicardia', 'ipotensione_post', 'cefalea', 
    		'sonnolenza', 'iper_congiuntivale'),
    	('tosse', 'astenia', 'disforia', 'crisi_ansia', 'concentrazione'), 
    	('fauci', 'sonnolenza_sedazione', 'confusione', 'amotivazione', 'delirio'),
    	('altro')
    )
    extra = 0


class ModalitaDecottoInline(admin.StackedInline):
    model = ModalitaDecotto
    fields = (
    	('quantita_acqua', 'sostanza_grassa'),
    	('tempo_impiegato', 'tempo_assunzione')
    )
    extra = 0


class PazienteResources(resources.ModelResource):

	class Meta:
		model = Paziente


class PazienteAdmin(ImportExportModelAdmin):
	resource_class = PazienteResources
	list_display = (
		'nome_completo', 'num_paziente', 'num_cartella', 'data_nascita', 'lavoro', 
		'titolo_studio', 'patologia'
	)
	radio_fields = {
		'titolo_studio': admin.HORIZONTAL,
		'patologia': admin.HORIZONTAL,
		'modalita_somministrazione': admin.HORIZONTAL
	}
	inlines = [BPIFormInline, EventiAvversiInline, ModalitaDecottoInline,]
	fieldsets = (
		('Dati paziente', {
            'fields': (('num_paziente', 'num_cartella'), ('nome','cognome'), 
            	('sesso', 'data_nascita', 'eta'),
            	('lavoro', 'titolo_studio'),
            	('patologia'),
            	('descrizione_patologica', 'eta_insorgenza'),
            	('altre_patologie', 'trattamenti')
            )
        }),
        ('Terapia con cannabis', {
            'fields': (('posologia', 'num_somministrazioni', 'data_trattamento'), 
            	('modalita_somministrazione'),
            	('utilizzo_cannabis', 'tempo_prelievo'),
            	('cannabis_ricreazionale', 'pregresso_utilizzo_ricreazionale', 
            		'uso_stupefacenti'),
            	('note')
            )
        }),
    )

admin.site.register(Paziente, PazienteAdmin)
