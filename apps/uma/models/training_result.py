from django.db import models
from .horse import Horse


class TrainingResult(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, related_name='training_results')
    date = models.DateField(verbose_name='培育日期')
    speed = models.IntegerField()
    stamina = models.IntegerField()
    power = models.IntegerField()
    guts = models.IntegerField()
    wisdom = models.IntegerField()
    evaluation_score = models.IntegerField(verbose_name='總分')
    note = models.TextField(blank=True, verbose_name='備註')

    class Meta:
        verbose_name = '培育結果'
        verbose_name_plural = '培育結果'
    def __str__(self):
        return f"{self.horse.name} ({self.date})"
