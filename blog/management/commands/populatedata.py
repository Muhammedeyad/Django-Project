
from blog.models import post, Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help="this command is used to insert values to blog"
    def handle(self, *args, **options):
            post.objects.all().delete()
            
            titles = [
                'Full Stack ',
                "Web Development",
                'Software Engineering',
                "Internet Of Things",
                "Information Technology",
                'Programming in Python ',
                'Data scientist',
                'Data Analysist'
            ]
            contents = [
                'About Full Stack Web Development in Tamil',
                'About Web Development In Tamil',
                'Set of Program is called Software',
                'Things Accessed by internet is called as Internet of things',
                'INfomartion Techlogy is related to It Field',
                'Python is a Interpreter Programming Language',
                'Data Scientist is a About data structure',
                'Data Analysist is also called About data structure',
                ]
            value = Category.objects.all()
            for title, content in zip(titles, contents):
                catagory = random.choice(value)
                post.objects.create(title=title, content=content, catagory = catagory)

            self.stdout.write(self.style.SUCCESS("Data Inserted"))