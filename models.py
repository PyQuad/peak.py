from tortoise.models import Model
from tortoise import fields

class WebLogs(Model):
    class Meta:
        table = "web_logs"

    site_addr = fields.CharField(max_length=1024)
    last_checked = fields.DatetimeField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)