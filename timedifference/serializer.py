from rest_framework import serializers

from timedifference.models import TimeModel


class TimeSerializer(serializers.ModelSerializer):
    requires_context = True

    owner_id = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)

    class Meta:
        model = TimeModel
        fields = [
            'owner_id',
            'created_at',
        ]
        read_only_fields = fields
