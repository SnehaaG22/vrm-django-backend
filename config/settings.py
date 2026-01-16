INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps (full path!)
    'apps.accounts.apps.AccountsConfig',
    'apps.orgs.apps.OrgsConfig',
    'apps.vendors.apps.VendorsConfig',
    'apps.templates.apps.TemplatesConfig',
    'apps.assessments.apps.AssessmentsConfig',
    'apps.evidence.apps.EvidenceConfig',
    'apps.reviews.apps.ReviewsConfig',
    'apps.remediations.apps.RemediationsConfig',
    'apps.renewals.apps.RenewalsConfig',
    'apps.audit.apps.AuditConfig',
    'apps.core.apps.CoreConfig',
]
