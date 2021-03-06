import json

from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from pollution.models import PollutionSource, Coordinates
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

        reports = self.model.objects.filter(**filters).order_by(
            '-when')[top:bottom]
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
                'pk': report.pk,
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
                'when': report.when.strftime('%b %d, %Y'),
                'approve_url': report.approve_url,
                'has_approved': True,
            }
            if request.user.is_authenticated():
                result['has_approved'] = report.user_approved.filter(
                    pk=request.user.pk).exists()
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(status=404)


class CreatePollutionSource(TemplateView):
    template_name = 'pollution/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreatePollutionSource, self).get_context_data(**kwargs)
        context['form'] = PollutionSourceForm()

        return context

    def post(self, request):
        center = Coordinates.objects.create(
            longitude=request.POST['long'],
            latitude=request.POST['lat'])
        pol = PollutionSource.objects.create(
            owner=request.user, center=center, address=request.POST['address'],
            description=request.POST['description'])
        image_pks = self.request.POST['image_pks']
        image_pks = image_pks.split(',')
        if len(image_pks) > 0:
            pol.images.add(*image_pks)
            return HttpResponse()
        return HttpResponse('form error', status=403)


class AddApproval(View):
    model = PollutionSource

    def post(self, request):
        if request.is_ajax():
            print 'here'
            pk = self.request.POST.get('pk', None)
            response = {}
            response['update'] = False
            if pk:
                user = self.request.user
                source = self.model.objects.get(pk=pk)
                if not source.user_approved.filter(pk=user.pk).exists():
                    source.user_approved.add(user)
                    response['count'] = source.user_approved.count()
                    response['update'] = True
            return HttpResponse(json.dumps(response))
        return HttpResponse(status=403)
