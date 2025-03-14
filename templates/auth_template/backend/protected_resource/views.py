from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from authapi.permissions import IsInstitutionOrEndUser

class ProtectedView(generics.ListAPIView):
    permission_classes = [IsInstitutionOrEndUser]
    def get(self, request, format=None):
        return Response('Successfully accessed.', status=status.HTTP_200_OK)
