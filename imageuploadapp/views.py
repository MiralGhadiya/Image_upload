from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema 


class BlogCreateAPIView(APIView):
    @swagger_auto_schema(request_body=Blogserializer)
    def post(self, request, *args, **kwargs):
        serializer = Blogserializer(data=request.data)
        
        if 'image' in request.FILES:
            image = request.FILES['image']
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                return Response({"status": False, 'message': "You can send only Image File"}, status=status.HTTP_400_BAD_REQUEST)
            if len(request.FILES.getlist('image')) > 1:
                return Response({"status": False, 'message': "Only one image is allowed"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, 'message': "Your Blog Created successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogGetAPIView(APIView):
    def get (self,request):
        data=Blog.objects.all()
        serializers=Blogserializer(data,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class SendEmailAPIView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        client_email = 'miral.g.evenmore@gmail.com'  
        send_mail(
            request.data.get('subject'),
            f"Message from {request.data.get('firstname')}  {request.data.get('lastname')}\n\n ({request.data.get('email')}):\n\n{request.data.get('message')}",
            request.data.get('email'),  
            [client_email],
            fail_silently=False,
        )
        
        send_mail(
            'Thank you for contacting us',
            'We appreciate your message and will get back to you soon!',
            client_email,  
            [request.data.get('email')],
            fail_silently=False,
        )
        if serializer.is_valid():
            
            serializer.save()

            return Response("email sent successfully", status=status.HTTP_201_CREATED)

        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
    
