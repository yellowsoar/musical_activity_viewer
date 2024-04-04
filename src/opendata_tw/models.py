from django.db import models

# Create your models here.

# Ref:
# https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJOpenApi&category=1


class MusicalActivity(models.Model):
    id = models.CharField(
        help_text="唯一辨識碼(Activity/UID)",
        max_length=50,
        primary_key=True,
        verbose_name="唯一辨識碼",
    )

    # Activity metadata
    additional_remark = models.TextField(
        blank=True,
        help_text="備註(Activity/comment)",
        null=True,
        verbose_name="備註",
    )
    category_code = models.ForeignKey(
        "ActivityCategory",
        help_text="活動類別(Activity/category)",
        null=True,
        on_delete=models.CASCADE,
        verbose_name="活動類別",
    )
    # Click-through rate (CTR)
    click_through_rate = models.IntegerField(
        blank=True,
        help_text="點閱數(Activity/hitRate)",
        null=True,
        verbose_name="點閱數",
    )
    description_content = models.TextField(
        blank=True,
        help_text="簡介說明(Activity/descriptionFilterHtml)",
        null=True,
        verbose_name="簡介說明",
    )
    discount_info = models.TextField(
        blank=True,
        help_text="折扣資訊(Activity/discountInfo)",
        null=True,
        verbose_name="折扣資訊",
    )
    flyer_source = models.CharField(
        blank=True,
        help_text="來源網站名稱(Activity/sourceWebName)",
        max_length=150,
        null=True,
        verbose_name="來源網站名稱",
    )
    publish_version = models.CharField(
        blank=True,
        help_text="發行版本(Activity/version)",
        max_length=50,
        null=True,
        verbose_name="發行版本",
    )
    title = models.CharField(
        blank=True,
        help_text="活動名稱(Activity/title)",
        max_length=250,
        null=True,
        verbose_name="活動名稱",
    )

    # Organizations, corps, teams
    unit_perform = models.ManyToManyField(
        "PerformUnit",
        help_text="演出單位(Activity/showUnit)",
        blank=True,
        through="ActivityPerformUnitMapping",
        through_fields=(
            "musical_activity",
            "unit_name",
        ),
        verbose_name="演出單位",
    )
    unit_host = models.ManyToManyField(
        "HostUnit",
        help_text="主辦單位(Activity/masterUnit)",
        blank=True,
        through="ActivityHostUnitMapping",
        through_fields=(
            "musical_activity",
            "unit_name",
        ),
        verbose_name="主辦單位",
    )
    unit_assist = models.ManyToManyField(
        "AssistUnit",
        help_text="協辦單位(Activity/subUnit)",
        blank=True,
        through="ActivityAssistUnitMapping",
        through_fields=(
            "musical_activity",
            "unit_name",
        ),
        verbose_name="協辦單位",
    )
    unit_sponsor = models.ManyToManyField(
        "SponsorUnit",
        help_text="贊助單位(Activity/supportUnit)",
        blank=True,
        through="ActivitySponsorUnitMapping",
        through_fields=(
            "musical_activity",
            "unit_name",
        ),
        verbose_name="贊助單位",
    )
    unit_other = models.ManyToManyField(
        "OtherUnit",
        help_text="其他單位(Activity/otherUnit)",
        blank=True,
        through="ActivityOtherUnitMapping",
        through_fields=(
            "musical_activity",
            "unit_name",
        ),
        verbose_name="其他單位",
    )

    # URLs
    url_image = models.URLField(
        blank=True,
        help_text="圖片連結(Activity/imageUrl)",
        null=True,
        verbose_name="圖片連結",
    )
    url_ticket = models.URLField(
        blank=True,
        help_text="售票網址(Activity/webSales)",
        null=True,
        verbose_name="售票網址",
    )
    url_flyer = models.URLField(
        blank=True,
        help_text="推廣網址(Activity/sourceWebPromote)",
        null=True,
        verbose_name="推廣網址",
    )

    # Date & Time
    time_created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text="Created time",
        null=True,
        verbose_name="記錄建立時間",
    )
    time_modified = models.DateTimeField(
        auto_now=True,
        editable=False,
        help_text="編輯時間(Activity/editModifyDate)",
        null=True,
        verbose_name="編輯時間",
    )
    time_start = models.DateField(
        blank=True,
        help_text="活動起始日期(Activity/startDate)",
        null=True,
        verbose_name="活動起始日期",
    )
    time_end = models.DateField(
        blank=True,
        help_text="活動結束日期(Activity/endDate)",
        null=True,
        verbose_name="活動結束日期",
    )


class ActivityCategory(models.Model):
    id = models.CharField(
        help_text="活動類別 Primary key",
        max_length=50,
        unique=True,
        primary_key=True,
    )
    category_name = models.CharField(
        help_text="活動類別名稱(Activity/category)",
        max_length=50,
        verbose_name="活動類別名稱",
    )


class PerformUnit(models.Model):
    unit_name = models.CharField(
        help_text="演出單位名稱(Activity/showUnit)",
        max_length=250,
        unique=True,
        primary_key=True,
        verbose_name="單位名稱",
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )


class ActivityPerformUnitMapping(models.Model):
    id = models.UUIDField(
        help_text="Primary key to a activity and show unit mapping",
        primary_key=True,
    )
    musical_activity = models.ForeignKey(
        'MusicalActivity',
        models.CASCADE,
    )
    unit_name = models.ForeignKey(
        'PerformUnit',
        models.CASCADE,
    )


class HostUnit(models.Model):
    unit_name = models.CharField(
        help_text="主辦單位(Activity/masterUnit)",
        max_length=250,
        unique=True,
        primary_key=True,
        verbose_name="單位名稱",
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )


class ActivityHostUnitMapping(models.Model):
    id = models.UUIDField(
        help_text="Primary key to a activity and show unit mapping",
        primary_key=True,
    )
    musical_activity = models.ForeignKey(
        'MusicalActivity',
        models.CASCADE,
    )
    unit_name = models.ForeignKey(
        'HostUnit',
        models.CASCADE,
    )


class AssistUnit(models.Model):
    unit_name = models.CharField(
        help_text="協辦單位(Activity/subUnit)",
        max_length=250,
        unique=True,
        primary_key=True,
        verbose_name="單位名稱",
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )


class ActivityAssistUnitMapping(models.Model):
    id = models.UUIDField(
        help_text="Primary key to a activity and show unit mapping",
        primary_key=True,
    )
    musical_activity = models.ForeignKey(
        'MusicalActivity',
        models.CASCADE,
    )
    unit_name = models.ForeignKey(
        'AssistUnit',
        models.CASCADE,
    )


class SponsorUnit(models.Model):
    unit_name = models.CharField(
        help_text="贊助單位(Activity/supportUnit)",
        max_length=250,
        unique=True,
        primary_key=True,
        verbose_name="單位名稱",
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )


class ActivitySponsorUnitMapping(models.Model):
    id = models.UUIDField(
        help_text="Primary key to a activity and show unit mapping",
        primary_key=True,
    )
    musical_activity = models.ForeignKey(
        'MusicalActivity',
        models.CASCADE,
    )
    unit_name = models.ForeignKey(
        'SponsorUnit',
        models.CASCADE,
    )


class OtherUnit(models.Model):
    unit_name = models.CharField(
        help_text="其他單位(Activity/otherUnit)",
        max_length=250,
        unique=True,
        primary_key=True,
        verbose_name="單位名稱",
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )


class ActivityOtherUnitMapping(models.Model):
    id = models.UUIDField(
        help_text="Primary key to a activity and show unit mapping",
        primary_key=True,
    )
    musical_activity = models.ForeignKey(
        'MusicalActivity',
        models.CASCADE,
    )
    unit_name = models.ForeignKey(
        'OtherUnit',
        models.CASCADE,
    )


class ActivityShow(models.Model):
    id = models.UUIDField(
        help_text="Primary key to a single show.",
        primary_key=True,
    )

    # Show Metadata
    activity_id = models.ForeignKey(
        'MusicalActivity',
        help_text="活動",
        on_delete=models.CASCADE,
    )
    # NOTE: Django choices has performance issue
    on_sale = models.CharField(
        blank=True,
        default="",
        help_text="是否售票(onSales)",
        max_length=50,
    )
    price_detail = models.TextField(
        blank=True,
        help_text="售票說明",
    )

    # Location
    location_address = models.TextField(
        blank=True,
        help_text="地址(location)",
        max_length=250,
    )
    location_name = models.CharField(
        blank=True,
        help_text="場地名稱(localtionName)",
        max_length=150,
    )
    location_longitude = models.CharField(
        blank=True,
        help_text="經度(longitude)",
        max_length=50,
    )
    location_latitude = models.CharField(
        blank=True,
        help_text="緯度(latitude)",
        max_length=50,
    )

    # Date time
    time_start = models.DateTimeField(
        blank=True,
        help_text="單場次演出時間(time)",
    )
    time_end = models.DateTimeField(
        blank=True,
        help_text="結束時間(endTime)",
    )
