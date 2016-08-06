import json

from django.views.generic import View
from django.http import HttpResponse

from pollution.models import PollutionSource


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
                'after_image_urls': report.image_url,
                'image_urls': report.image_urls,
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
                }

            }
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(status=404)
