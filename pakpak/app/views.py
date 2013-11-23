# coding: utf-8
#from django.shortcuts import render
from django.views.generic import TemplateView
from models import Sound


class SoundView(TemplateView):
    template_name = "app/player.html"

    def get_context_data(self, **kwargs):
        context = super(SoundView, self).get_context_data(**kwargs)
        context['sound_src'] = self.get_current_sound()  # 'media/Music/timemachine.mp3'
        context['sound_list'] = self.get_sounds_list()
        print context['sound_list']
        return context

    def get_current_sound(self):
        return Sound.objects.filter().first().url

    def get_sounds_list(self):
        return Sound.objects.all()
