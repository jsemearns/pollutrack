import json

from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.shortcuts import render

from pollution.models import PollutionSource
from pollution.forms import PollutionSourceForm


class ListPollutionSources(View):

    model = PollutionSource

    def get(self, request):
        filters = {
            'is_verified': True,
            'is_fixed': request.GET.get('fixed', False),
        }

        top = request.GET.get('top', 0)
        bottom = request.GET.get('bottom', 30)
        result = []

        reports = self.model.objects.filter(**filters)[top:bottom]
        for report in reports:
            center = report.center;
            result.append({
                'image_url': report.image_url,
                'long': center.longitude,
                'lat': center.latitude,
                'address': report.address,
                'approve_count': report.user_approved.count(),
                'pk': report.pk,
                })
        return HttpResponse(json.dumps(result))


class GetPollutionSources(View):

    model = PollutionSource

    def get(self, request):
        filters = {
            'is_verified': True,
            'pk': request.GET.get('pk', 0),
        }

        report = self.model.objects.filter(**filters).first()
        if report:
            center = report.center;
            result = {
                'first_image_url': report.image_url,
                'image_urls': report.image_urls,
                'after_image_urls': report.after_image_urls,
                'long': center.longitude,
                'lat': center.latitude,
                'address': report.address,
                'approve_count': report.user_approved.count(),
                'is_fixed': report.is_fixed,
                'description': report.description,
                'owner': {
                    'full_name': report.owner.get_full_name(),
                    'profile_image_url':
                    report.owner.profile.profile_image_url,
                },
                'when': report.when.strftime('%b %d, %Y')

            }
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(status=404)


class CreatePollutionSource(TemplateView):
    template_name = 'pollution/create.html'
    form_class = PollutionSourceForm

    def get_context_data(self, **kwargs):
        context = super(CreatePollutionSource, self).get_context_data(**kwargs)
        context['form'] = PollutionSourceForm()

        return context

    def post(self, request):
        form = self.form_class(request.POST)
        image_pks = self.request.POST.getlist('image_pks')

        if form.is_valid():
            pol = form.save()
            if image_pks:
                pol.images.add(*image_pks)
            return HttpResponse()
        return HttpResponse('form error', status=403)
