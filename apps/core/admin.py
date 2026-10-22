from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin
from django.db.models import OuterRef, Subquery

from django.contrib import admin
from django.db.models import OuterRef, Subquery,Count


# =========================================================
# ENQUIRY CALLING HISTORY INLINE
# =========================================================


from .models.website import (
    Setting,
    Slider,
    Why_Choose,
    About,
    Contact_Page,
    Enquiry,
    Our_Team,
    Testimonial,
    FAQ,
    ImpactMetric,
    Gallery,
    USP,
    PriceBreakupInquiry,
    Inquiry,
    EnquiryCalling
)

class EnquiryCallingInline(admin.TabularInline):
    model = EnquiryCalling
    extra = 0
    can_delete = True

    fields = (
        "called_at",
        "response",
        "note",
    )

    readonly_fields = (
        "called_at",
    )

    ordering = (
        "-called_at",
    )




class BaseSettingInline(admin.StackedInline):
    """
    Common inline configuration for all website sections.
    """

    extra = 1
    min_num = 0
    show_change_link = False
    can_delete = True
    classes = ()


class SliderInline(BaseSettingInline):
    model = Slider

    fields = (
        "title1",
        "title2",
        "badge_title",
        "descriptions",
        "image",
        "image_preview",
        "order",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"

class AboutInline(BaseSettingInline):
    model = About

    fields = (
        # Home Content
        "title",
        "subtitle",
        "content",
        "read_legacy",
        "image",
        "image_preview",

        # About Content
        "about_title",
        "about_subtitle",
        "about_content",

        # Mission / Vision
        "mission_title",
        "mission_content",
        "vision_title",
        "vision_content",

        # Hero
        "hero_title",
        "hero_highlight",
        "hero_subtitle",
        "hero_description",
        "hero_background",
        "hero_background_preview",

        "button_one_text",
        "button_one_link",

        "button_two_text",
        "button_two_link",

        # SEO
        "seo_title",
        "seo_description",

        # Images
        "right_image1",
        "right_image1_preview",
        "right_image2",
        "right_image2_preview",

        # Stats
        "years_of_experience",
        "happy_families",

        "is_active",
    )

    readonly_fields = (
        "image_preview",
        "hero_background_preview",
        "right_image1_preview",
        "right_image2_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Main Image Preview"

    def hero_background_preview(self, obj):
        if obj and obj.hero_background:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:cover; border:1px solid #ddd; padding:5px;" />',
                obj.hero_background.url,
            )
        return "No Image"

    hero_background_preview.short_description = "Hero Background Preview"

    def right_image1_preview(self, obj):
        if obj and obj.right_image1:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.right_image1.url,
            )
        return "No Image"

    right_image1_preview.short_description = "Right Image 1 Preview"

    def right_image2_preview(self, obj):
        if obj and obj.right_image2:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.right_image2.url,
            )
        return "No Image"

    right_image2_preview.short_description = "Right Image 2 Preview"

class ContactPageInline(BaseSettingInline):
    model = Contact_Page

    fields = (
        "heading",
        "sub_heading",
        "address",
        "phone",
        "email",
        "map_iframe",
        "is_active",
    )

    extra = 0


class OurTeamInline(BaseSettingInline):
    model = Our_Team

    fields = (
        "name",
        "designation",
        "image",
        "image_preview",
        "bio",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="height:100px; width:100px; '
                'object-fit:cover; border-radius:8px; border:1px solid #ddd;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


class TestimonialInline(BaseSettingInline):
    model = Testimonial

    fields = (
        "name",
        "designation",
        "message",
        "image",
        "image_preview",
        "rating",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="height:100px; width:100px; '
                'object-fit:cover; border-radius:50%; border:1px solid #ddd;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"

class WhyChooseInline(BaseSettingInline):
    model = Why_Choose

    fields = (
        "icons",
        "title",
        "subtitle",
        "order",
        "is_active",
    )

    extra = 0

class USPInline(BaseSettingInline):
    model = USP

    fields = (
        "icons",
        "title",
        "subtitle",
        "order",
        "is_active",
    )

    extra = 0


class FAQInline(BaseSettingInline):
    model = FAQ

    fields = (
        "question",
        "answer",
        "is_active",
    )

    extra = 0


class ImpactMetricInline(BaseSettingInline):
    model = ImpactMetric

    fields = (
        "title",
        "value",
        "icon",
        "order",
        "is_active",
    )

    extra = 0


class GalleryInline(BaseSettingInline):
    model = Gallery

    fields = (
        "gallery_category",
        "title",
        "image",
        "image_preview",
        "description",
        "featured",
        "order",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:150px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


class EnquiryInline(BaseSettingInline):
    model = Enquiry

    fields = (
        "name",
        "email",
        "phone",
        "message",
        "is_active",
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )

    extra = 0


class EnquiryCallingInline(admin.TabularInline):
    model = EnquiryCalling

    extra = 0
    can_delete = True

    fields = (
        "called_at",
        "note",
    )

    readonly_fields = (
        "called_at",
    )

    ordering = (
        "-called_at",
    )


# =========================================================
# INQUIRY ADMIN
# =========================================================

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    change_list_template = "admin/core/inquiry/change_list.html"

    # -----------------------------------------------------
    # LIST DISPLAY
    # -----------------------------------------------------

    list_display = (
        "name",
        "phone",
        "email",
        "project",
        "Enquiry_status",
        "response_count",
        "last_response",
        "contacted_on",
    )

    list_display_links = (
        "name",
    )

    # -----------------------------------------------------
    # SEARCH
    # -----------------------------------------------------

    search_fields = (
        "name",
        "phone",
        "email",
        "project__project_name",
    )

    # -----------------------------------------------------
    # FILTER
    # -----------------------------------------------------

    list_filter = (
        "Enquiry_status",
        "project",
        "contacted_on",
    )

    # -----------------------------------------------------
    # READONLY
    # -----------------------------------------------------

    readonly_fields = (
        "created_at",
        "contacted_on",
    )

    # -----------------------------------------------------
    # ORDERING
    # -----------------------------------------------------

    ordering = (
        "-contacted_on",
    )

    list_per_page = 20

    # -----------------------------------------------------
    # INLINE
    # -----------------------------------------------------

    inlines = [
        EnquiryCallingInline,
    ]

    # =====================================================
    # SAME PHONE NUMBER
    # ONLY LATEST INQUIRY SHOW
    # =====================================================

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        # -----------------------------------------
        # SAME PHONE KI TOTAL INQUIRY COUNT
        # -----------------------------------------

        response_count_subquery = (
            Inquiry.objects
            .filter(
                phone=OuterRef("phone")
            )
            .values("phone")
            .annotate(
                total=Count("id")
            )
            .values("total")[:1]
        )

        # -----------------------------------------
        # SAME PHONE KI LATEST INQUIRY
        # -----------------------------------------

        latest_inquiry = (
            Inquiry.objects
            .filter(
                phone=OuterRef("phone")
            )
            .order_by(
                "-contacted_on",
                "-id"
            )
            .values("id")[:1]
        )

        # -----------------------------------------
        # SAME PHONE KI LATEST RESPONSE DATE
        # -----------------------------------------

        last_response_subquery = (
            Inquiry.objects
            .filter(
                phone=OuterRef("phone")
            )
            .order_by(
                "-contacted_on",
                "-id"
            )
            .values("contacted_on")[:1]
        )

        return (
            qs
            .annotate(
                response_total=Subquery(
                    response_count_subquery
                ),
                latest_response_at=Subquery(
                    last_response_subquery
                ),
            )
            .filter(
                id=Subquery(latest_inquiry)
            )
        )
    # =====================================================
    # RESPONSE COUNT
    #
    # IMPORTANT:
    # ONLY Inquiry MODEL COUNT
    #
    # EnquiryCalling ka koi count nahi
    # =====================================================

    @admin.display(
        description="Responses",
        ordering="phone",
    )
    def response_count(self, obj):

        return Inquiry.objects.filter(
            phone=obj.phone
        ).count()

    # =====================================================
    # LAST RESPONSE
    #
    # SAME PHONE KI LATEST INQUIRY
    # =====================================================

    @admin.display(
        description="Last Response",
    )
    def last_response(self, obj):

        last = (
            Inquiry.objects
            .filter(
                phone=obj.phone
            )
            .order_by(
                "-contacted_on",
                "-id"
            )
            .first()
        )

        if last and last.contacted_on:
            return last.contacted_on.strftime(
                "%d %b %Y, %I:%M %p"
            )

        return "-"


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):

    list_display = (
        "site_name",
        "status",
        "phone",
        "email",
        "logo_preview",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "status",
        "is_active",
    )

    search_fields = (
        "site_name",
        "phone",
        "email",
        "rera_number",
        "address",
    )

    readonly_fields = (
        "logo_preview",
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Website Information",
            {
                "fields": (
                    "site_name",
                    "logo",
                    "logo_preview",
                    "favicon",
                    "offer_img",
                    "offer_img2",
                    "search_bg",
                    "Virtual_bg",
                )
            },
        ),

        (
            "Theme Colors",
            {
                "fields": (
                    "header_footer_color",
                    "text_color",
                    "button_color",
                    "rera_color",
                )
            },
        ),

        (
            "RERA Information",
            {
                "fields": (
                    "rera_number",
                    "current_project_rera",
                )
            },
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "address",
                    "phone",
                    "whatsapp",
                    "email",
                    "google_map",
                    "virtual_360_url",
                    "virtual_360_title",
                    "footer_link_text",


                )
            },
        ),

        (
            "Working Hours",
            {
                "fields": (
                    "working_days",
                    "working_hours",
                )
            },
        ),

        (
            "Google & SMTP",
            {
                "fields": (
                    "googletagmanager",
                    "recaptcha_secret_key",
                    "recaptcha_site_key",
                    "google_label",
                    "smtpserver",
                    "smtpemail",
                    "smtppassword",
                    "smtpport",
                )
            },
        ),

        (
            "Social Media",
            {
                "fields": (
                    "facebook",
                    "instagram",
                    "twitter",
                    "youtube",
                    "linkexplore",
                )
            },
        ),

        (
            "SEO",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "meta_keywords",
                )
            },
        ),

        (
            "Footer",
            {
                "fields": (
                    "footer_text",
                    "copy_right",
                )
            },
        ),


        (
            "Legal Pages",
            {
                "fields": (
                    "privacy_policy_title",
                    "privacy_policy_content",
                    "disclaimer_title",
                    "disclaimer_content",
                    
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "status",
                    "is_active",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    inlines = [
        SliderInline,
        AboutInline,
        ContactPageInline,
        OurTeamInline,
        TestimonialInline,
        WhyChooseInline,
        FAQInline,
        ImpactMetricInline,
        GalleryInline,
        EnquiryInline,
        USPInline,

    ]

    def logo_preview(self, obj):
        if obj and obj.logo:
            return format_html(
                '<img src="{}" style="height:60px; max-width:180px; '
                'object-fit:contain; border:1px solid #ddd; padding:4px;" />',
                obj.logo.url,
            )

        return "No Logo"

    logo_preview.short_description = "Logo"


@admin.register(PriceBreakupInquiry)
class PriceBreakupInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'project', 'created_at')
    list_filter = ('created_at', 'project')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False

