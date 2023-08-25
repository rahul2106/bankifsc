# bankdetails/management/commands/add_bank_details.py
from django.core.management.base import BaseCommand
from api.models import Bank

class Command(BaseCommand):
    help = 'Adds bank details to the database'

    def handle(self, *args, **options):
        # Example data, you can replace this with actual data
        bank_data = [
            {
                'ifsc': 'ABCD1234567',
                'bank_name': 'Example Bank',
                'branch': 'Main Branch',
                'address': '123 Example Street',
                'city': 'Example City',
                'state': 'Example State',
                'district': 'Example District',
                'bank_id': 'BANK123'
            },
            # Add more bank data dictionaries here
        ]

        for data in bank_data:
            Bank.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully added bank details to the database'))
