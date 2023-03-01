from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from students.models import University, Student
from students.api.serializers import UniversitySerializer, StudentSerializer


# UNIVERSITY VIEWS
class UniversityListAPIView(ListCreateAPIView):
    queryset = University.objects.all().order_by('name')
    serializer_class = UniversitySerializer


class UniversityDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


# STUDENT VIEWS
class StudentListAPIView(ListCreateAPIView):
    queryset = Student.objects.all().order_by('-created_at')
    serializer_class = StudentSerializer


class StudentDetailAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
