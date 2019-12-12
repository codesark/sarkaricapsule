from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from events.models import Event, Result, AdmitCard

from .models import News
from .utils import create_job_news, create_result_news, create_admitcard_news


@receiver(post_save, sender=Event)
def create_news_from_event(sender, instance, created, **kwargs):
    print("=====> Creating News For Job")

    # Create Job News if instance is a job
    if instance.is_active and instance.create_news and instance.event_type.name == "Job":
        news = create_job_news(instance, created)

@receiver(post_save, sender=Result)
def create_news_from_result(sender, instance, created, **kwargs):
    print("=====> Creating News For Result")

    # Create Result News if Result is Updated in Event
    if instance.event.is_active and instance.event.create_news:
        create_result_news(instance.event, created)

@receiver(post_save, sender=AdmitCard)
def create_news_from_admitcard(sender, instance, created, **kwargs):
    print("=====> Creating News For AdmitCard")

    # Create Result News if Result is Updated in Event
    if instance.event.is_active and instance.event.create_news:
        create_admitcard_news(instance.event, created)


# an event receiver to create slug of News instance
@receiver(pre_save, sender=News)
def add_slug_to_news(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string
