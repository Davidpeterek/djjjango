from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Klub(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název klubu', help_text='Napis název týmu',
                             error_messages={'blank': 'Toto pole musí být vyplněno'})
    misto = models.CharField(max_length=30, verbose_name='Město', help_text='Napis jméno města',
                             error_messages={'blank': 'Toto pole musí být vyplněno'})
    zalozeni = models.IntegerField(blank=True, validators=[MinValueValidator(1900), MaxValueValidator(2023)], verbose_name='Rok založení',
                                   help_text='Napis rok založení')
    logo = models.ImageField(blank=True, upload_to='loga', verbose_name='Logo klubu', help_text='Zadejte logo klubu')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Klub'
        verbose_name_plural = 'Kluby'

    def __str__(self):
        return f'{self.nazev}, {self.misto}'


class Hrac(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name='Jméno', help_text='Zadejte jméno hráče',
                             error_messages={'blank': 'Jméno cyklisty musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení', help_text='Zadejte příjmení hráče',
                                error_messages={'blank': 'Příjmení cyklisty musí být vyplněno'})
    narozeni = models.DateField(blank=True, verbose_name='Datum narození', help_text='Zadejte datum narození')
    fotka = models.ImageField(blank=True, upload_to='fotky', verbose_name='Nahrejte fotku hráče')
    klub = models.ForeignKey('Klub', on_delete=models.CASCADE, verbose_name='Klub')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Hrac'
        verbose_name_plural = 'Hraci'

    def __str__(self):
        return f'{self.prijmeni}, {self.jmeno}'


class Zapas(models.Model):
    domaci_tym = models.ForeignKey(Klub, related_name='domaci_tymy', on_delete=models.CASCADE, verbose_name='domaci tým',
                                   help_text='Vyber domácí tým')
    hostujici_tym = models.ForeignKey(Klub, related_name='hostujici_tymy', on_delete=models.CASCADE,
                                      verbose_name='hostující tým', help_text='Vyber tým hostů')
    datum = models.DateTimeField(verbose_name='Datum zápasu')
    domaci_skore = models.PositiveIntegerField(verbose_name='Skóre domácího týmu',
                                               help_text='Vyber skóre domácího týmu')
    hostujici_skore = models.PositiveIntegerField(verbose_name='Skóre hostujícího týmu',
                                                  help_text='Vyber skóre hostujícího týmu')

    def __str__(self):
        return f'{self.domaci_tym} vs {self.hostujici_tym} - {self.datum}'

    class Meta:
        ordering = ['-datum']
        verbose_name = 'Zápas'
        verbose_name_plural = 'Zápasy'

    def __str__(self):
        return f'{self.datum.day}. {self.datum.month}. {self.datum.year}:)'