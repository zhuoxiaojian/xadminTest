import datetime

from django.db.models import FieldDoesNotExist, Avg, Max, Min, Count, Sum
from django.utils.translation import ugettext as _
from django.forms import Media

from users.models import AdPriceRate
from utils import ConversionUtils
from xadmin.sites import site
from xadmin.views import BaseAdminPlugin, ListAdminView

from xadmin.views.list import ResultRow, ResultItem
from xadmin.util import display_for_field

AGGREGATE_METHODS = {
    'min': Min, 'max': Max, 'avg': Avg, 'sum': Sum, 'count': Count
}
AGGREGATE_TITLE = {
    'min': _('Min'), 'max': _('Max'), 'avg': _('Avg'), 'sum': _('Sum'), 'count': _('Count')
}


class AggregationPlugin(BaseAdminPlugin):

    aggregate_fields = {}

    def init_request(self, *args, **kwargs):
        return bool(self.aggregate_fields)

    def _get_field_aggregate(self, field_name, obj, row):
        item = ResultItem(field_name, row)
        item.classes = ['aggregate', ]
        if field_name not in self.aggregate_fields:
            item.text = ""
        else:
            try:
                f = self.opts.get_field(field_name)
                agg_method = self.aggregate_fields[field_name]
                key = '%s__%s' % (field_name, agg_method)
                if key not in obj:
                    item.text = ""
                else:
                    item.text = display_for_field(obj[key], f)
                    item.wraps.append('%%s<span class="aggregate_title label label-info">%s</span>' % AGGREGATE_TITLE[agg_method])
                    item.classes.append(agg_method)
            except FieldDoesNotExist:
                item.text = ""

        return item

    def _get_aggregate_row(self):
        queryset = self.admin_view.list_queryset._clone()
        obj = queryset.aggregate(*[AGGREGATE_METHODS[method](field_name) for field_name, method in
                                   self.aggregate_fields.items() if method in AGGREGATE_METHODS])
        if 'cost__sum' in obj:

            if self.user.is_superuser != 1:
                obj['cost__sum'] = 0
                for q in queryset:
                    obj['cost__sum'] += q.cost

            # print('cost__sum::{0}'.format(obj['cost__sum']))
        if 'avgCpc__avg' in obj:

            if self.user.is_superuser != 1:
                if obj['clicks__sum'] != 0:
                    obj['avgCpc__avg'] = round(obj['cost__sum'] / obj['clicks__sum'], 3)
                    if obj['avgCpc__avg'] == 0:
                        obj['avgCpc__avg'] = '0.000'
                else:
                    obj['avgCpc__avg'] = '0.000'
            # print('avgCpc__avg::{0}'.format(obj['avgCpc__avg']))
        if 'avgCpm__avg' in obj:

            if self.user.is_superuser != 1:
                if obj['impressions__sum'] != 0:
                    obj['avgCpm__avg'] = round(obj['cost__sum'] / obj['impressions__sum'] * 1000, 3)
                    if obj['avgCpm__avg'] == 0:
                        obj['avgCpm__avg'] = '0.000'
                else:
                    obj['avgCpm__avg'] = '0.000'
            # print('avgCpm__avg::{0}'.format(obj['avgCpm__avg']))
        if 'ctr__sum' in obj:

            if self.user.is_superuser != 1:
                if obj['impressions__sum'] != 0:
                    obj['ctr__sum'] = str(round((obj['clicks__sum']/obj['impressions__sum'])*100, 2)) + '%'
                else:
                    obj['ctr__sum'] = '0.00'
                    # print('ctr__sum::{0}'.format(obj['ctr__sum']))

        if 'ecpa1__avg' in obj:

            if self.user.is_superuser != 1:
                if obj['G1__sum'] != 0:
                    obj['ecpa1__avg'] = round(obj['cost__sum'] / obj['G1__sum'], 2)
                    if obj['ecpa1__avg'] == 0:
                        obj['ecpa1__avg'] = '0.00'
                else:
                    obj['ecpa1__avg'] = '0.00'
            # print('ecpa1__sum::{0}'.format(obj['ecpa1__sum']))

        if 'ecpa2__avg' in obj:

            if self.user.is_superuser != 1:
                if obj['G2__sum'] != 0:
                    obj['ecpa2__avg'] = round(obj['cost__sum'] / obj['G2__sum'], 2)
                    if obj['ecpa2__avg'] == 0:
                        obj['ecpa2__avg'] = '0.00'
                else:
                    obj['ecpa2__avg'] = '0.00'
            # print('ecpa2__sum::{0}'.format(obj['ecpa2__sum']))

        if 'ecpa3__avg' in obj:

            if self.user.is_superuser != 1:
                if obj['G3__sum'] != 0:
                    obj['ecpa3__avg'] = round(obj['cost__sum'] / obj['G3__sum'], 2)
                    if obj['ecpa3__avg'] == 0:
                        obj['ecpa3__avg'] = '0.00'
                else:
                    obj['ecpa3__avg'] = '0.00'
            # print('ecpa3__sum::{0}'.format(obj['ecpa3__sum']))

        if 'ecpa4__avg' in obj:

            if self.user.is_superuser != 1:
                if obj['G4__sum'] != 0:
                    obj['ecpa4__avg'] = round(obj['cost__sum'] / obj['G4__sum'], 2)
                    if obj['ecpa4__avg'] == 0:
                        obj['ecpa4__avg'] = '0.00'
                else:
                    obj['ecpa4__avg'] = '0.00'
            # print('ecpa4__sum::{0}'.format(obj['ecpa4__sum']))

        row = ResultRow()
        row['is_display_first'] = False
        row.cells = [self._get_field_aggregate(field_name, obj, row) for field_name in self.admin_view.list_display]
        row.css_class = 'info aggregate'
        return row

    def results(self, rows):
        if rows:
            rows.append(self._get_aggregate_row())
        return rows

    # Media
    def get_media(self, media):
        return media + Media(css={'screen': [self.static('xadmin/css/xadmin.plugin.aggregation.css'), ]})


site.register_plugin(AggregationPlugin, ListAdminView)
