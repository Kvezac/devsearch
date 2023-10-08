from users.models import Profile, User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.user.email,
            name=user.first_name
        )


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created is False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
