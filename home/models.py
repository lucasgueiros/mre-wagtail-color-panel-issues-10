from django.db import models

from wagtail.models import Page
from wagtail_color_panel.blocks import NativeColorBlock
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import StreamFieldPanel

class HomePage(Page):
    secoes = StreamField([
        ("cor",NativeColorBlock()),
    ], null = True)
    content_panels = Page.content_panels + [
        StreamFieldPanel("secoes"),
    ]
