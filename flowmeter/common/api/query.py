# coding=utf-8
from django.db.models import Q


class QueryType:
    """
    查询类型枚举类，只有or和and两种类型
    """
    OR = 'or'
    AND = 'and'


class QueryTerms:

    def __init__(self, query_type, **kwargs):
        self.query_type = query_type
        self.terms = kwargs

    @staticmethod
    def make_or_query_terms(**kwargs):
        query_terms = QueryTerms(query_type=QueryType.OR, **kwargs)
        return query_terms

    @staticmethod
    def make_and_query_terms(**kwargs):
        query_terms = QueryTerms(query_type=QueryType.AND, **kwargs)
        return query_terms

    def get_filters(self):
        """
        获得查询条件相对应的过滤条件
        :return:
        """
        filters = None
        for field_name, field_val in self.terms.items():

            if not field_val:
                continue

            now_filter = None
            # 如果值为列表类型，则迭代拼接
            if isinstance(field_val, list):
                for item in field_val:
                    field_dict = {field_name: item}
                    if now_filter:
                        if self.query_type == QueryType.OR:
                            now_filter = now_filter | Q(**field_dict)
                        else:
                            now_filter = now_filter & Q(**field_dict)
                    else:
                        now_filter = Q(**field_dict)
            else:
                field_dict = {field_name: field_val}
                now_filter = Q(**field_dict)

            if filters:
                if self.query_type == QueryType.OR:
                    filters = filters | now_filter
                else:
                    filters = filters & now_filter
            else:
                filters = now_filter

        # filter为 None 说明目前没有过滤条件，就返回一个永远为真的过滤条件
        if filters is None:
            return Q()
        else:
            return filters






