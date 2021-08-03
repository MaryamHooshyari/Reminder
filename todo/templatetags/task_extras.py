from datetime import datetime
from django import template
import pytz

register = template.Library()


@register.simple_tag
def remain_time(due):
    """counts difference between task's due date and now in datetime format"""
    now = str(due - datetime.now(pytz.timezone('Asia/Tehran')))
    return now[:7].replace(',', '').replace(' ', '')
