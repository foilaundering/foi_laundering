import csv
import io
import codecs

import requests

from django.core.management.base import BaseCommand

from foi_requests.models import Authority


class Command(BaseCommand):
    def handle(self, **options):
        CSV_URL = "http://localhost:8000/all-authorities.csv"
        csv_data = requests.get(CSV_URL, stream=True).raw
        csv_reader = csv.reader(codecs.iterdecode(csv_data, 'utf-8'))
        for line in csv_reader:
            obj, created = Authority.objects.update_or_create(
                name=line[0], slug=line[2])

