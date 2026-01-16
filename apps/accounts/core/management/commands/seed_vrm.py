from django.core.management.base import BaseCommand
from orgs.models import Organization
from accounts.models import User
from vendors.models import Vendor
from templates.models import Template, TemplateVersion, Section, Question

class Command(BaseCommand):
    help = "Seed VRM demo data"

    def handle(self, *args, **kwargs):
        org = Organization.objects.create(name="Demo Org")

        admin = User.objects.create_user(
            username="admin",
            password="admin123",
            role="ADMIN",
            organization=org
        )

        reviewer = User.objects.create_user(
            username="reviewer",
            password="review123",
            role="REVIEWER",
            organization=org
        )

        vendor1 = Vendor.objects.create(
            organization=org,
            name="Cloud CRM Vendor",
            risk_tier="high"
        )

        template = Template.objects.create(name="Security Assessment")
        version = TemplateVersion.objects.create(template=template, version=1)

        section = Section.objects.create(
            template_version=version,
            title="Access Control",
            weight=40
        )

        Question.objects.create(
            section=section,
            text="Is MFA enabled?",
            is_red_flag=True,
            requires_evidence=True
        )

        self.stdout.write(self.style.SUCCESS("✅ VRM seed data loaded"))
