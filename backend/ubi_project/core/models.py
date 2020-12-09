from django.db import models
from django_countries.fields import CountryField
import uuid


class Client(models.Model):
    class Meta:
        verbose_name = 'client'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=30)
    vat_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = CountryField(blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    contact_person_phone = models.CharField(max_length=20, blank=True)
    contact_person_email = models.CharField(max_length=254, blank=True)
    registration_date = models.DateField(blank=False, auto_now=True)
    contract = models.CharField(max_length=100, null=True, blank=True)
    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)

    @property
    def client_logo(self):
        return 'media/{}/logo.png'.format(self.uuid)

    def __str__(self):
        return self.name


class Content(models.Model):
    class Meta:
        verbose_name = 'content'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = CountryField(blank=True)
    # geolocation = PointField(blank=True)
    is_parent = models.BooleanField(default=False)
    is_institutional = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ContentHighlight(models.Model):
    class Meta:
        verbose_name = 'content'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    is_always = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.content} Content Highlight'
