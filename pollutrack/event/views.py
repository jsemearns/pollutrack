import json

from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

from event.models import Event


class ListEvents(View):
    model = Event

    def get(self, request):
        filters = {
            'pollution_source__pk': request.GET.get('pk', 0),
            'status': request.GET.get('status', 0),
            'approval': 1
        }

        top = request.GET.get('top', 0)
        bottom = request.GET.get('bottom', 30)
        result = []

        events = self.model.objects.filter(**filters).order_by(
            'start_date')[top:bottom]
        for event in events:
            freebie = event.freebies
            result.append({
                'owner_image_url': event.owner.profile.profile_image_url,
                'owner_name': event.owner.get_full_name(),
                'slogan': event.slogan,
                'no_of_volunteers': event.volunteers.count(),
                'start_date': event.start_date.strftime('%b %d, %Y %I:%M %p'),
                'pk': event.pk,
            })
        print result
        return HttpResponse(json.dumps(result))


class GetEvent(View):
    model = Event

    def get(self, request):
        filters = {
            'status': request.GET.get('status', 0),
            'pk': request.GET.get('pk', 0),
        }

        event = self.model.objects.filter(**filters).first()
        if event:
            freebies = []
            for f in event.freebies:
                freebie = {
                    'title': f.title,
                    'description': f.description,
                    'image_urls': f.image_urls
                }
                freebies.append(freebie)
            result = {
                'owner_image_url': event.owner.profile.profile_image_url,
                'owner_name': event.owner.get_full_name(),
                'slogan': event.slogan,
                'no_of_volunteers': event.volunteers.count(),
                'first_volunteer': event.volunteers.first().get_full_name(),
                'when': event.when,
                'freebies': freebies,
                'description': event.description,
                'start_date': event.start_date.strftime('%m/%d/%Y %I:%M %p'),
                'end_date': event.end_date.strftime('%m/%d/%Y %I:%M %p'),
                'donation_goal': event.donation_goal,
                'donation_gathered': event.donation_gathered,
                'approval': event.approval,
                'before_images_urls': event.before_images_urls,
                'after_images_urls': event.after_images_urls,
                'meetup_address': event.meetup_address
            }
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(status=404)
