from rest_framework import serializers
from subscription.models import Email


class EmailSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = "__all__"