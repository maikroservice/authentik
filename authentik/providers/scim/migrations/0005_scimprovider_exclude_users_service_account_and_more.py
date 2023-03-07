# Generated by Django 4.1.7 on 2023-03-07 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_core", "0025_alter_provider_authorization_flow"),
        ("authentik_providers_scim", "0004_scimprovider_property_mappings_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="scimprovider",
            name="exclude_users_service_account",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="scimprovider",
            name="parent_group",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="authentik_core.group",
            ),
        ),
    ]
