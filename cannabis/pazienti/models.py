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


class Paziente(models.Model):
    num_paziente = models.CharField(verbose_name=_(u"N° Paziente"), max_length=10, blank=True, null=True)
    num_cartella = models.CharField(verbose_name=_(u"N° Cartella"), max_length=100, blank=True, null=True)
    nome = models.CharField(verbose_name=_(u"Sesso"), max_length=10, blank=True, null=True)
    cognome = models.CharField(verbose_name=_(u"Sesso"), max_length=100, blank=True, null=True)
    sesso = models.CharField(max_length=1, verbose_name=_(u"Sesso"), choices=SESSO, blank=True, null=True)
    data_nascita = models.DateField(verbose_name=_(u'Data di nascita'), blank=True, null=True)
    eta = models.CharField(verbose_name=_(u"Età"), max_length=2, blank=True, null=True)
    lavoro = models.CharField(verbose_name=_(u"Lavoro"), max_length=100, blank=True, null=True)
    titolo_studio = models.CharField(verbose_name=_(u"Titolo di studio"), max_length=1, blank=True, null=True, choices=TITOLO_DI_STUDIO)
    patologia = models.CharField(verbose_name=_(u"Patologia"), max_length=1, blank=True, null=True, choices=PATOLOGIA)
    descrizione_patologica = models.TextField(verbose_name=_(u"Descrizione patologica"), null=True, blank=True)
    eta_insorgenza = models.CharField(verbose_name=_(u"Età anagrafica all'insorgenza della patologia dolorosa"), max_length=2, blank=True, null=True)
    altre_patologie = models.TextField(verbose_name=_(u"Altre patologie"), null=True, blank=True)
    trattamenti = models.TextField(verbose_name=_(u"Trattamenti farmacologici in corso"), null=True, blank=True)

    class Meta:
        verbose_name = _('Paziente')
        verbose_name_plural = _('Pazienti')

    def __str__(self):
        return '%s %s'.format(self.nome, self.cognome)
