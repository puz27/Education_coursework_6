from django.core.management import BaseCommand
from users.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@gmail.com",
            first_name="admin",
            last_name="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True
            )

        user.set_password("admin")
        user.save()
        print("Creating user admin.")

        user = User.objects.create(
            email="moderator@gmail.com",
            first_name="moderator",
            last_name="moderator",
            is_superuser=False,
            is_staff=True,
            is_active=True
        )
        user.set_password("moderator")
        user.save()
        print("Creating user moderator.")

        user = User.objects.create(
            email="test@gmail.com",
            first_name="test",
            last_name="test",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )
        user.set_password("test")
        user.save()
        print("Creating user test.")

        GROUPS = ['moderators', ]
        MODELS = ['Client', 'Message', 'Transmission', ]
        PERMISSIONS = ['view', ]

        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
                for permission in PERMISSIONS:
                    name = 'Can {} {}'.format(permission, model)
                    print("Creating {}".format(name))
                    model_add_perm = Permission.objects.get(name=name)
                    new_group.permissions.add(model_add_perm)

