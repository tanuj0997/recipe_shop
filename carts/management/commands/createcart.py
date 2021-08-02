from django.core.management.base import BaseCommand, CommandError
from ...models import Cart


class Command(BaseCommand):
    """
    Management command to create the shopping cart for the first time
    """
    help = "Generates the cart for the first time"

    def handle(self, *args, **options):
        # Checking if cart exists
        if not Cart.objects.all().exists():
            Cart.objects.create()
            self.stdout.write(self.style.SUCCESS('Successfully created cart'))
        else:
            self.stdout.write(self.style.WARNING(
                'Cart already exists, skipping this step'))
