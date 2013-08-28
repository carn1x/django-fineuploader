# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.views.generic import CreateView


class FineUploaderView(CreateView):
    def form_valid(self, form):
        super(FineUploaderView, self).form_valid(form)
        content = json.dumps({'success': True})
        return HttpResponse(content, content_type='application/json')
