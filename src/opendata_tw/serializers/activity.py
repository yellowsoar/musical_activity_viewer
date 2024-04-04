import copy
import json
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)

from opendata_tw import models
from rest_framework import serializers


class MusicalActivitySerializer(serializers.ModelSerializer):
    """Musical Activity Serializer"""

    class Meta:
        model = models.MusicalActivity
        fields = '__all__'


class ActivityCategorySerializer(serializers.ModelSerializer):
    """Activity Category Serializer"""

    class Meta:
        model = models.ActivityCategory
        fields = '__all__'
