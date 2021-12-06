# Create your views here.
from django.http import Http404
from rest_framework import status
from jobmanagers.models import Company,Job
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from jobmanagers.serializers import UserSerializer, GroupSerializer,CompanySerializers,JobSerializers,CategorySerializers,LocationSerializers,TechSerializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyList(APIView):
    """
    List all company, or create a new snippet.
    """
    
    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = CompanySerializers(company, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetail(APIView):
        """
        List a company, or update and delete.
        """
        def get_object(self, pk):
            try:
                return Company.objects.get(pk=pk)
            except Company.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            company = self.get_object(pk)
            serializer = CompanySerializers(company)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            company = self.get_object(pk)
            serializer = CompanySerializers(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            company = self.get_object(pk)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



class JobList(APIView):
    """
    List all jobs, or create a new snippet.
    """
    
    def get(self, request, format=None):
        company = Job.objects.all()
        serializer = JobSerializers(company, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobDetail(APIView):
        """
        List a job, or update and delete.
        """
        def get_object(self, pk):
            try:
                return Job.objects.get(pk=pk)
            except Job.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            company = self.get_object(pk)
            serializer = JobSerializers(company)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            company = self.get_object(pk)
            serializer = JobSerializers(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            company = self.get_object(pk)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


