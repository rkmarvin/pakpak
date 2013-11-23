#from django.shortcuts import render
from django.views.generic import TemplateView


class SoundView(TemplateView):
    template_name = "app/player.html"

    def get_context_data(self, **kwargs):
        context = super(SoundView, self).get_context_data(**kwargs)
        context['sound_src'] = 'media/Music/timemachine.mp3'
        context['sound_list'] = [
            'media/Music/love_my_country.mp3',
            'media/Music/lada.mp3'
        ]
        return context
