from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.models import Karer
from core.api.serializers import CarSerializer, DriverSerializer
from marketplace.api.serializers import ProductSerializer
from import_invite.models import OrgImportInvite


class InviteShowSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    product = ProductSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)
    weight = serializers.FloatField(read_only=True)
    status = serializers.CharField(read_only=True)


class InviteCheckSerializer(serializers.Serializer):
    status = serializers.BooleanField(read_only=True)
    invite = InviteShowSerializer(read_only=True, required=False)
    plate = serializers.CharField(write_only=True)
    karer = serializers.SlugRelatedField("slug", queryset=Karer.objects.all(), write_only=True)

    def validate(self, attrs):
        plate: str = attrs.get("plate")
        karer: Karer = attrs.get('karer')
        invite = OrgImportInvite.check_plate(plate, karer.slug)
        accept_statuses = ["payed"]
        if invite.status not in accept_statuses:
            raise ValidationError({"invite": f"Invite status is {invite.status}. Mest be {', '.join(accept_statuses)}"})
        return {
            "status": bool(invite),
            "invite": invite
        }
