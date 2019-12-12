from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import datetime

from organizations.models import Organization

# Event Core Related Models

RECENT_DAYS_OFFSET = 5

class EventType(models.Model):
  name = models.CharField(max_length=5000)
  description = models.CharField(max_length=5000, blank=True, null=True)

  def __str__(self):
    return f"{ self.name }"



# Event Model

class Event(models.Model):  
  event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, related_name='events')
  title = models.CharField(max_length=5000)
  page_title = models.CharField(max_length=5000)
  is_active = models.BooleanField(default=False)
  slug = models.SlugField(max_length=5000, unique=True)
  image = models.ImageField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='events')

  # meta fields
  meta_keywords = models.TextField(max_length=10000, blank=True, null=True)
  
  # event start and end date
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)

  # created and modified fields
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  # related_data
  min_eligible_age = models.PositiveSmallIntegerField(blank=True, null=True)
  max_eligible_age = models.PositiveSmallIntegerField(blank=True, null=True)
  min_education_qualification = models.CharField(max_length=5000, blank=True, null=True)
  vacancy_details = models.TextField(blank=True, null=True)
  payment_method = models.TextField(blank=True, null=True)

  create_news = models.BooleanField("Create News??", default=False, blank=True, null=True)
  
  class Meta:
    ordering = ('-modified_at',)

  def clean(self):
    if self.min_eligible_age is not None and self.max_eligible_age is not None:
      if self.min_eligible_age >= self.max_eligible_age:
        raise ValidationError({'min_eligible_age': "Minimum eligible age must be smaller that Max eligible age."})

  def __str__(self):
    return f"{self.title}, {self.organization.name} ({ self.event_type.name })"

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False


  is_recently_added.admin_order_field = 'created_at'
  is_recently_added.boolean = True
  is_recently_added.short_description = 'Recenty Added?'

  
  is_recently_updated.admin_order_field = 'modified_at'
  is_recently_updated.boolean = True
  is_recently_updated.short_description = 'Recenty Updated?'
  
  def get_absolute_url(self):
    from django.urls import reverse
    return reverse('events:detail', kwargs={'pk': self.id, 'slug': self.slug, 'listtype': self.event_type.name.lower()})
    
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(Event, self).save(*args, **kwargs)

# Event Related Models

class ImportantDate(models.Model):
  
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="importantDates")
  
  title = models.CharField(max_length=5000)
  date = models.DateTimeField('Date', blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()
  
  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = 'Important Date'
    verbose_name_plural = 'Important Dates'

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(ImportantDate, self).save(*args, **kwargs)



class ImportantUpdate(models.Model):
  
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="importantUpdates")

  title = models.CharField(max_length=5000)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = 'Important Updates'
    verbose_name_plural = 'Important Updates'

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(ImportantUpdate, self).save(*args, **kwargs)



class ImportantLink(models.Model):

  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="importantLinks")

  title = models.CharField(max_length=5000)
  link = models.CharField(max_length=5000)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Important Link'
    verbose_name_plural = 'Important Links'

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(ImportantLink, self).save(*args, **kwargs)



class Result(models.Model):

  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="results")

  title = models.CharField(max_length=5000)
  link = models.CharField(max_length=5000, blank=True, null=True)
  file = models.FileField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Result'
    verbose_name_plural = 'Results'
  
  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(Result, self).save(*args, **kwargs)



class AnswerKey(models.Model):

  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="answerKeys")

  title = models.CharField(max_length=5000)
  link = models.CharField(max_length=5000, blank=True, null=True)
  file = models.FileField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Answer Keys'
    verbose_name_plural = 'Answer Keys'

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(AnswerKey, self).save(*args, **kwargs)


class AdmitCard(models.Model):

  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="admitCards")

  title = models.CharField(max_length=5000)
  description = models.TextField(blank=True, null=True)
  link = models.CharField(max_length=5000, blank=True, null=True)
  file = models.FileField(blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Admit Card'
    verbose_name_plural = 'Admit Cards'

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at >= comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at >= comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(AdmitCard, self).save(*args, **kwargs)


class Syllabus(models.Model):
  
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="syllabuses")

  title = models.CharField(max_length=5000)
  description = models.TextField(blank=True, null=True)
  link = models.CharField(max_length=5000, blank=True, null=True)
  file = models.FileField(blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Syllabus'
    verbose_name_plural = 'Syllabuses'

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(Syllabus, self).save(*args, **kwargs)



class Fee(models.Model):
  
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="fees")

  title = models.CharField(max_length=5000)
  description = models.TextField(blank=True, null=True)
  amount = models.FloatField()
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Fee'
    verbose_name_plural = 'Fees'

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(Fee, self).save(*args, **kwargs)


class Eligibility(models.Model):
 
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="eligibilities")

  title = models.CharField(max_length=5000)
  description = models.TextField(blank=True, null=True)
  criteria = models.CharField(max_length=5000, blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()
  def __str__(self):  
    return self.title

  class Meta:
    verbose_name = 'Eligibility Criteria'
    verbose_name_plural = 'Eligibility Criterias'

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(Eligibility, self).save(*args, **kwargs)



class Faq(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="faqs")
  
  question_title = models.CharField(max_length=5000)
  question_description = models.TextField(blank=True, null=True)
  answer_title = models.CharField(max_length=5000)
  answer_detail = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  class Meta:
    verbose_name = "FAQ"
    verbose_name_plural = "FAQs"

  def __str__(self):
    return f"{ self.question_title }"

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(Faq, self).save(*args, **kwargs)



class HowTo(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="howTos")

  title = models.CharField(max_length=5000)
  description = models.TextField()
  created_at = models.DateTimeField()
  modified_at = models.DateTimeField()

  class Meta:
    verbose_name = "How-To"
    verbose_name_plural = "How-To\'s"

  def is_recently_added(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.created_at > comparison_date):
      return True
    return False

  def is_recently_updated(self):
    comparison_date = timezone.now() - timezone.timedelta(days=RECENT_DAYS_OFFSET)
    # comparison_date = timezone.make_aware(datetime(2019, 9, 9), timezone.get_current_timezone())
    if (self.modified_at > comparison_date):
      return True
    return False

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created_at = timezone.now()
    self.modified_at = timezone.now()
    return super(HowTo, self).save(*args, **kwargs)

# class HowToStep(models.Model):

#   howto = models.ForeignKey(HowTo, on_delete=models.CASCADE, related_name="steps")
#   title = models.TextField()

  