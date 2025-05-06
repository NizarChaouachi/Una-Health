import django_filters.rest_framework as filters

from .models import GlucoseTableLvels,User



class GlucoseLevelsFilter(filters.FilterSet):
    start = filters.IsoDateTimeFilter(field_name="device_time_stamp",lookup_expr="gte")
    stop = filters.IsoDateTimeFilter(field_name="device_time_stamp",lookup_expr="lte")
    limit  = filters.NumberFilter(field_name="limit",method="limit_filter")
    sort = filters.OrderingFilter(fields=("__all__"))
    def limit_filter(self,queryset,name,value):
        return queryset[:value]
   