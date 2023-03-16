from collections import defaultdict
from django.db.models.functions import Trunc
from django.db.models import Count
from karer_web.charts.line_chart import LineChartDashboard
from .forms import InviteDashboardForm
from invite.models import OrgInvite, ClientInvite


class InviteLineChart(LineChartDashboard):
    settings_form = InviteDashboardForm
    title = 'Линейный график заявки'

    def init_with_context(self, context):
        if self.params:
            dataset = defaultdict(list)
            data = OrgInvite.objects.values_list('create_at__date', 'id')

            for d in data:
                dataset[d[0]].append(d[1])
            
            data = ClientInvite.objects.values_list('create_at__date', 'id')

            for d in data:
                dataset[d[0]].append(d[1])

            for date, v in dataset.items():
                self.children.append((date, len(v), 1))
