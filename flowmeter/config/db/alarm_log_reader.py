# coding=utf-8
from django.db import models

from flowmeter.config.const import STATE_CHAR_LEN, UNIQUE_FLAG_CHAR_LEN
from flowmeter.config.db.log_table import AlarmLog
from flowmeter.config.db.user_table import User


class AlarmLogReader(models.Model):
    """
    记录警报通知给了哪些用户
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 该警报已经被阅读
    STATE_READ = 'read'
    # 该警报未被阅读
    STATE_UNREAD = 'unread'
    # 警报状态
    state = models.CharField(max_length=STATE_CHAR_LEN, default=STATE_UNREAD)
    alarm_log = models.ForeignKey(AlarmLog, on_delete=models.CASCADE)
    # 判断警报是否重复推送的标志
    unique_flag = models.CharField(max_length=UNIQUE_FLAG_CHAR_LEN)

    class Meta:
        # 创建状态索引
        indexes = [
            models.Index(fields=['user', 'state'], name='user_state_index'),
        ]
