from rest_framework import serializers
from .models import Category, Project, ProjectTag, ProjectPic
from users.models import CustomUser
from django.utils import timezone

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProjectPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPic
        fields = ['id', 'pic']
        read_only_fields = ['id']

class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = ['id', 'tagname']
        read_only_fields = ['id']

class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    pictures = ProjectPicSerializer(many=True, required=False)
    tags = ProjectTagSerializer(many=True, required=False)
    current_funding = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        read_only=True
    )
    funding_percentage = serializers.FloatField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'user', 'category', 'title', 'details', 'total_target',
            'start_date', 'end_date', 'status', 'is_cancelled', 'created_at',
            'current_funding', 'funding_percentage', 'average_rating',
            'pictures', 'tags'
        ]
        read_only_fields = ['id', 'created_at', 'is_cancelled']
    
    def validate(self, data):
        if 'start_date' in data and 'end_date' in data:
            if data['start_date'] >= data['end_date']:
                raise serializers.ValidationError("End date must be after start date")
            if data['end_date'] <= timezone.now():
                raise serializers.ValidationError("End date must be in the future")
        return data
    
    def create(self, validated_data):
        pictures_data = validated_data.pop('pictures', [])
        tags_data = validated_data.pop('tags', [])
        
        project = Project.objects.create(**validated_data)
        
        # Create project pictures
        for pic_data in pictures_data:
            ProjectPic.objects.create(project=project, **pic_data)
        
        # Create project tags
        for tag_data in tags_data:
            ProjectTag.objects.create(project=project, **tag_data)
            
        return project
    
    def update(self, instance, validated_data):
        pictures_data = validated_data.pop('pictures', None)
        tags_data = validated_data.pop('tags', None)
        
        # Update main fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update pictures
        if pictures_data is not None:
            # Clear existing pictures
            instance.pictures.all().delete()
            # Add new pictures
            for pic_data in pictures_data:
                ProjectPic.objects.create(project=instance, **pic_data)
        
        # Update tags
        if tags_data is not None:
            # Clear existing tags
            instance.tags.all().delete()
            # Add new tags
            for tag_data in tags_data:
                ProjectTag.objects.create(project=instance, **tag_data)
                
        return instance

class ProjectDetailSerializer(ProjectSerializer):
    category = CategorySerializer(read_only=True)