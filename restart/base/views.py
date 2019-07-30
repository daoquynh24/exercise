# Python imports
import os
import uuid

# Django imports
from django.conf import settings
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

# Rest framework import
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter
)

# Application imports
from base.constants.common import (
    AppConstants,
    ViewConstants
)


# Create your views here.
class BaseListCreateAPIView(generics.ListCreateAPIView):
    model = None
    action = None
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    )
    ordering_fields = "__all__"

    # Set action
    def get(self, request, *args, **kwargs):
        self.action = ViewConstants.Action.LIST
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.action = ViewConstants.Action.CREATE
        return self.create(request, *args, **kwargs)

    # set default query, create
    def get_queryset(self):
        return self.model.objects.filter(deleted_at=None)

    def perform_create(self, serializer):
        serializer.save()


class BaseListAPIView(generics.ListAPIView):
    model = None
    action = None

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    )
    ordering_fields = "__all__"

    # set action
    def get(self, request, *args, **kwargs):
        self.action = ViewConstants.Action.LIST
        return self.list(request, *args, **kwargs)

    # set default query
    def get_queryset(self):
        return self.model.objects.filter(deleted_at=None)

