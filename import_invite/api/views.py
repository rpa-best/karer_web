from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import OrgImportInvite, ClientImportInvite


class InvitePlateCheck(GenericAPIView):
    def post(self, request, *args, **kwargs):
        plate = self.kwargs.get('plate')
        check = OrgImportInvite.check_plate(plate, request.data.get('karer'))
        if not check:
            check = ClientImportInvite.check_plate(plate, request.data.get('karer'))
        return Response({'check': check}, status.HTTP_400_BAD_REQUEST)
