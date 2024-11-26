from django.views.generic import View
from django.shortcuts import render
from django.conf import settings



class IndexView(View):

    template_name = 'index.html'

    def get(self, request):
        context = {
            'user': request.user
        }
        return render(request, self.template_name, context=context)
