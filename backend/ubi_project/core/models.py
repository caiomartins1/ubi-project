from django.db import models
from django_countries.fields import CountryField
from django_pgviews import view as pg
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


class ContentSibling(models.Model):
    class Meta:
        verbose_name = 'content'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)
    parent = models.ForeignKey(Content, on_delete=models.CASCADE,
                               to_field="uuid", related_name="parent_uuid")
    content = models.ForeignKey(Content, on_delete=models.CASCADE,
                                to_field="uuid", related_name="content_uuid")

    def __str__(self):
        return f'{self.content} Sibling'


class ContentHighlight(models.Model):
    class Meta:
        verbose_name = 'highlight'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    is_always = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.content} Content Highlight'


class ContentUpselling(models.Model):
    class Meta:
        verbose_name = 'upselling'
        verbose_name_plural = 'upselling'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ContentCard(pg.View): #TODO: Integrate Images and Translation tool

    uuid = models.UUIDField(unique=True)
    title = models.CharField(max_length=100)
    client_id = models.UUIDField()
    upselling_uuid = models.UUIDField()
    highlight_uuid = models.UUIDField()
    is_parent = models.BooleanField()
    is_institutional = models.BooleanField()
    active_highlight = models.BooleanField()
    active = models.BooleanField()

    sql = """
        SELECT  c.uuid AS id,
            c.uuid,
            c.title,
            c.client_id,
            u.uuid AS upselling_uuid,
            h.uuid AS highlight_uuid,
            c.is_parent,
                CASE
                    WHEN h.is_always OR CURRENT_DATE >= h.start_date AND CURRENT_DATE <= h.end_date THEN true
                    ELSE false
                END as active_highlight,
            c.active,
            c.is_institutional
        FROM core_content AS c
            LEFT JOIN core_contentupselling u ON u.content_id = c.uuid
            LEFT JOIN core_contenthighlight h ON h.content_id = c.uuid
        WHERE c.active
        ORDER BY c.title;
    """

    class Meta:
        managed = False
        db_table = 'content_card_view'


class UpsellingCard(pg.View):

    uuid = models.UUIDField(unique=True)
    title = models.CharField(max_length=100)
    client_id = models.UUIDField()
    upselling_uuid = models.UUIDField()
    highlight_uuid = models.UUIDField()
    is_parent = models.BooleanField()
    is_institutional = models.BooleanField()
    active_highlight = models.BooleanField()
    active = models.BooleanField()

    sql = """
        SELECT c.uuid as id,
            c.uuid,
            c.title,
            c.client_id,
            u.uuid AS upselling_uuid,
            h.uuid AS highlight_uuid,
            c.is_parent,
                CASE
                    WHEN h.is_always OR CURRENT_DATE >= h.start_date AND CURRENT_DATE <= h.end_date THEN true
                    ELSE false
                END as active_highlight,
            c.active,
            c.is_institutional
        FROM core_contentupselling u, core_content c
            LEFT JOIN core_contenthighlight h ON h.content_id = c.uuid
        WHERE u.content_id = c.uuid AND c.active
        ORDER BY c.title;
    """

    class Meta:
        managed = False
        db_table = 'upselling_card_view'


class HighlightCard(pg.View):

    uuid = models.UUIDField(unique=True)
    title = models.CharField(max_length=100)
    client_id = models.UUIDField()
    upselling_uuid = models.UUIDField()
    highlight_uuid = models.UUIDField()
    is_parent = models.BooleanField()
    is_institutional = models.BooleanField()
    active_highlight = models.BooleanField()
    active = models.BooleanField()

    sql = """
        SELECT c.uuid as id,
            c.uuid,
            c.title,
            c.client_id,
            u.uuid AS upselling_uuid,
            h.uuid AS highlight_uuid,
            c.is_parent,
                CASE
                    WHEN h.is_always OR CURRENT_DATE >= h.start_date AND CURRENT_DATE <= h.end_date THEN true
                    ELSE false
                END AS active_highlight,
            c.active,
            c.is_institutional
        FROM core_contenthighlight h, core_content c
            LEFT JOIN core_contentupselling u ON u.content_id = c.uuid
        WHERE h.content_id = c.uuid AND c.active
        ORDER BY c.title;
    """

    class Meta:
        managed = False
        db_table = 'highlight_card_view'
