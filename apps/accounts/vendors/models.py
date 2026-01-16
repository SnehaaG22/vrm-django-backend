from django.db import models

class Vendor(models.Model):
    organization = models.ForeignKey("orgs.Organization", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    risk_tier = models.CharField(max_length=20, default="medium")
    status = models.CharField(max_length=30, default="active")

    def __str__(self):
        return self.name

class VendorUser(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} -> {self.vendor}"
