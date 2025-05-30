from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Comment, Reply, Rate
from .serializers import CommentSerializer, ReplySerializer, RateSerializer
# Create your views here.
