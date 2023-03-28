from jet.dashboard.dashboard import AppIndexDashboard, Dashboard
from jet.dashboard import modules
from invite.dashboard import OrgInviteLineChart, ClientInviteLineChart
from import_invite.dashboard import OrgImportInviteLineChart, ClientImportInviteLineChart
from marketplace.dashboard import StateProductDashboard
from karer_web.dashboard import InviteLineChart
from django.utils.translation import gettext_lazy as _


class AppIndexDashboard(AppIndexDashboard):

    def init_with_context(self, context):
        self.available_children.append(modules.ModelList)
        self.available_children.append(modules.RecentActions)
        if self.app_label not in ['marketplace']:
            self.available_children.append(OrgInviteLineChart)
            self.available_children.append(ClientInviteLineChart)
            self.available_children.append(OrgImportInviteLineChart)
            self.available_children.append(ClientImportInviteLineChart)
        if self.app_label == 'marketplace':
            self.available_children.append(StateProductDashboard)


class IndexDashboard(Dashboard):
    columns = 1

    def init_with_context(self, context):
        self.available_children.append(modules.AppList)
        self.available_children.append(modules.RecentActions)
        self.available_children.append(InviteLineChart)
