from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ..models import ClientInvite, OrgInvite


class InvitePlateCheck(GenericAPIView):
    def post(self, request, *args, **kwargs):
        plate = self.kwargs.get('plate')
        check = OrgInvite.check_plate(plate, request.data.get('karer'))
        if not check:
            check = ClientInvite.check_plate(plate, request.data.get('karer'))
        return Response({'check': check}, status.HTTP_400_BAD_REQUEST)
