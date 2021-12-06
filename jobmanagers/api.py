from rest_framework import generics
from jobmanagers.serializers import JobSerializers
from .models import Job





class JobCreateApi(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers

class JobListApi(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers

class JobUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers

class JobDeleteApi(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers