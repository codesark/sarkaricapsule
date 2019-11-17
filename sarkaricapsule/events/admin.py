from django.contrib import admin
from django import forms
from .models import *
from django_summernote.admin import SummernoteModelAdminMixin, SummernoteModelAdmin
from django.db import models as AdminModels
from django_summernote.widgets import SummernoteWidget

# --- Hide Django Summernote Model ----- 
from django.contrib import admin
from django_summernote.utils import get_attachment_model 
admin.site.unregister(get_attachment_model())
#  ----------------- END ----------------------

#  ---- Small Text Area Field for Inline Models
class DifferentlySizedTextarea(forms.Textarea):
  def __init__(self, *args, **kwargs):
    attrs = kwargs.setdefault('attrs', {})
    attrs.setdefault('cols', 15)
    attrs.setdefault('rows', 3)
    super(DifferentlySizedTextarea, self).__init__(*args, **kwargs)


# ---- Inline Models ------------------------
class AdmitCardInlineAdmin(admin.TabularInline):
  model = AdmitCard
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')


class AnswerKeyInlineAdmin(admin.TabularInline):
  model = AnswerKey
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')


class EligibilityInlineAdmin(admin.TabularInline):
  model = Eligibility
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')


class FeeInlineAdmin(admin.TabularInline):
  model = Fee
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')


class ImportantDateInlineAdmin(admin.TabularInline):
  model = ImportantDate
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')


class ImportantLinkInlineAdmin(admin.TabularInline):
  model = ImportantLink
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')


class ImportantUpdateInlineAdmin(admin.TabularInline):
  model = ImportantUpdate
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')


class ResultInlineAdmin(admin.TabularInline):
  model = Result
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')


class SyllabusInlineAdmin(admin.TabularInline):
  model = Syllabus
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')

class HowToInlineAdmin(admin.StackedInline):
  model = HowTo
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': SummernoteWidget}}
  # inlines = (HowToStepInlineAdmin, )



class FaqInlineAdmin(admin.StackedInline):
  model = Faq
  extra = 0
  formfield_overrides = { AdminModels.TextField: {'widget': DifferentlySizedTextarea}}
  exclude = ('created_at', 'modified_at')

  

class EventAdmin(SummernoteModelAdmin):
  summernote_fields = ['description', 'vacancy_details', 'payment_method']
  exclude = ('slug', 'created_at', 'modified_at', )
  inlines = [
    AdmitCardInlineAdmin,
    AnswerKeyInlineAdmin,
    EligibilityInlineAdmin,
    FeeInlineAdmin,
    ImportantDateInlineAdmin,
    ImportantLinkInlineAdmin,
    ImportantUpdateInlineAdmin,
    ResultInlineAdmin,
    SyllabusInlineAdmin,
    HowToInlineAdmin,
    FaqInlineAdmin
  ]
  list_display = ('title', 'modified_at', 'is_active', 'is_recently_added', 'is_recently_updated')
  list_filter = ['modified_at', 'created_at', 'event_type']
  search_fields = ['title', 'slug', 'id']


admin.site.register(Event, EventAdmin)

class EventTypeAdmin(admin.ModelAdmin):

  pass

  # hide from Index
  def get_model_perms(self, request):
    return {}

  # Prevent by mistake addition or removal of Event Types
  def has_add_permission(self, request):
    return False

  def has_delete_permission(self, request, obj=None):
    return False
  
  def has_change_permission(self, request, obj=None):
    return False

  

admin.site.register(EventType, EventTypeAdmin)

# function to hide passed model from admin index
def register_hidden_model(*m):
  ma = type(
    str(m)+'Admin',
    (admin.ModelAdmin,),
    {
      'get_model_perms': lambda self, request: {}
    })
  admin.site.register(m, ma)

register_hidden_model(AdmitCard)
register_hidden_model(AnswerKey)
register_hidden_model(Eligibility)
register_hidden_model(Fee)
register_hidden_model(ImportantDate)
register_hidden_model(ImportantLink)
register_hidden_model(ImportantUpdate)
register_hidden_model(Result)
register_hidden_model(Syllabus)
register_hidden_model(Faq)
register_hidden_model(HowTo)
# register_hidden_model(HowToStep)

