from django.core.management.base import BaseCommand
from main.models import Project, Service, Testimonial

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **options):
        # Create dummy projects
        Project.objects.create(
            titre='Project 1',
            slug='project-1',
            description='Description for Project 1',
            image='projects/project1.jpg',
            date='2025-01-01',
            is_featured=True
        )
        Project.objects.create(
            titre='Project 2',
            slug='project-2',
            description='Description for Project 2',
            image='projects/project2.jpg',
            date='2025-02-01',
            is_featured=False
        )

        # Create dummy services
        Service.objects.create(
            titre='Service 1',
            slug='service-1',
            description='Description for Service 1',
            icone='fa fa-cog'
        )
        Service.objects.create(
            titre='Service 2',
            slug='service-2',
            description='Description for Service 2',
            icone='fa fa-wrench'
        )

        # Create dummy testimonials
        Testimonial.objects.create(
            nom='John Doe',
            contenu='Great service!',
            note=5
        )
        Testimonial.objects.create(
            nom='Jane Smith',
            contenu='Highly recommend!',
            note=4
        )

        self.stdout.write(self.style.SUCCESS('Dummy data added successfully!'))
