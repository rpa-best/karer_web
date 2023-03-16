from jet.dashboard.dashboard import AppIndexDashboard, Dashboard, DefaultIndexDashboard
from jet.dashboard import modules
from invite.dashboard import OrgInviteLineChart, ClientInviteLineChart
from karer_web.dashboard import InviteLineChart
from django.utils.translation import gettext_lazy as _


class AppIndexDashboard(AppIndexDashboard):

    def init_with_context(self, context):
        self.available_children.append(modules.ModelList)
        self.available_children.append(modules.RecentActions)
        if self.app_label == 'invite':
            self.columns = 2
            self.available_children.append(OrgInviteLineChart)
            self.available_children.append(ClientInviteLineChart)



class IndexDashboard(Dashboard):
    columns = 1

    def init_with_context(self, context):
        self.available_children.append(modules.AppList)
        self.available_children.append(modules.RecentActions)
        self.available_children.append(InviteLineChart)
