import json

from django.views.generic import View, TemplateView
from django.http import HttpResponse

from images.models import ImageUploads
from images.forms import ImageForm

from core.views.mixins import LoginRequiredMixin


class UploadImage(LoginRequiredMixin, TemplateView):
    template_name = 'images/upload.html'
    form_class = ImageForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            i = form.save()
            return HttpResponse(json.dumps({'pk': i.pk, 'url': i.url}))
        return HttpResponse('invalid file', status=403)

        

