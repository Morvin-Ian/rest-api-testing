from django.core.management.base import BaseCommand
import requests
import json

class Command(BaseCommand):
    help = "Consume the Update Single Blog API"

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='The pk of the blog')
        parser.add_argument('title', type=str, help='The title of the blog')
        parser.add_argument('content', type=str, help='The content of the blog')
        parser.add_argument('token', type=str, help='Auth Token')



    def handle(self, *args, **kwargs):
        id = kwargs['id']
        token = kwargs['token']
        api_url = f"http://127.0.0.1:8000/api/blogs/{id}/update/"

        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type':'application/json'
        }

        blog ={
            "title":kwargs['title'],
            "content":kwargs['content']
        }
  
        response = requests.put(
            api_url,
            json.dumps(blog),
            headers=headers
        )

        if response.status_code == 200:
            api_data = response.json()
            self.stdout.write(self.style.SUCCESS(f'Successfully Updated the Blog: {api_data}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to consume API: {response.json()}'))
            