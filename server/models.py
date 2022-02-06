from tortoise.models import Model
from tortoise import fields

class WebLog(Model):
    site_addr = fields.CharField(max_length=256)
    ping_ms = fields.FloatField()
    status = fields.SmallIntField()
    reason = fields.CharField(16)
    checked_at = fields.DatetimeField(auto_now_add=True)