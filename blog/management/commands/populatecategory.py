from blog.models import Category;
from django.core.management.base import BaseCommand
import logging

class Command(BaseCommand):
    help = "this command insert the values"
    def handle(self, *args, **options):
        Category.objects.all().delete()        
        catagory = ["Tech", "Sports", "Motivation", "Entertainment", "Education"]

        for catalog in catagory:
            Category.objects.create(title=catalog)
            logger = logging.getLogger("TESTING")
            logger.debug(catalog)
        self.stdout.write(self.style.SUCCESS("Value Inserted"))