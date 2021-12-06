# Create your views here.
from django.http import Http404
from rest_framework import status
from jobmanagers.models import Company,Job,Category,Tech,Location
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
        job = Job.objects.all()
        serializer = JobSerializers(job, many=True)
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
            job = self.get_object(pk)
            serializer = JobSerializers(job)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            job = self.get_object(pk)
            serializer = JobSerializers(job, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            job = self.get_object(pk)
            job.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    """
    List all category, or create a new snippet.
    """
    
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
        """
        List a category, or update and delete.
        """
        def get_object(self, pk):
            try:
                return Category.objects.get(pk=pk)
            except Category.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            category = self.get_object(pk)
            serializer = CategorySerializers(category)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            category = self.get_object(pk)
            serializer = CategorySerializers(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            category = self.get_object(pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class TechList(APIView):
    """
    List all Tech, or create a new snippet.
    """
    
    def get(self, request, format=None):
        tech = Tech.objects.all()
        serializer = TechSerializers(tech, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TechSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechDetail(APIView):
        """
        List a Tech, or update and delete.
        """
        def get_object(self, pk):
            try:
                return Tech.objects.get(pk=pk)
            except Tech.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            tech = self.get_object(pk)
            serializer = TechSerializers(tech)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            tech = self.get_object(pk)
            serializer = TechSerializers(tech, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            tech = self.get_object(pk)
            tech.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class LocationList(APIView):
    """
    List all Location, or create a new snippet.
    """
    
    def get(self, request, format=None):
        location = Location.objects.all()
        serializer = LocationSerializers(location, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
        """
        List a location, or update and delete.
        """
        def get_object(self, pk):
            try:
                return Location.objects.get(pk=pk)
            except Location.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            location = self.get_object(pk)
            serializer = LocationSerializers(location)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            location = self.get_object(pk)
            serializer = LocationSerializers(location, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            location = self.get_object(pk)
            location.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
