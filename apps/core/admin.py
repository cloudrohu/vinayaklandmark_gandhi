from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.urls import reverse

from django.contrib import admin
from django.db.models import (
    Q,
    Count,
    OuterRef,
    Subquery,
)
from urllib.parse import quote

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


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    # change_list_template = "admin/core/inquiry/change_list.html"

    # =====================================================
    # LIST
    # =====================================================

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

    # =====================================================
    # SEARCH
    # =====================================================

    search_fields = (
        "name",
        "phone",
        "email",
        "project__project_name",
    )

    # =====================================================
    # IMPORTANT
    # Custom filter use ho raha hai
    # =====================================================

    list_filter = (
    "Enquiry_status",
    "project",
    "contacted_on",
)

    # =====================================================
    # READONLY
    # =====================================================

    readonly_fields = (
        "created_at",
        "contacted_on",
    )

    # =====================================================
    # ORDERING
    # =====================================================

    ordering = (
        "-contacted_on",
        "-id",
    )

    list_per_page = 24

    # =====================================================
    # CHANGE LIST CONTEXT
    # =====================================================

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        status = request.GET.get("Enquiry_status", "").strip()
        project = request.GET.get("project", "").strip()
        contacted_on = request.GET.get("contacted_on", "").strip()
        search = request.GET.get("q", "").strip()

        if search:
            qs = qs.filter(
                Q(name__icontains=search)
                | Q(phone__icontains=search)
                | Q(email__icontains=search)
                | Q(project__project_name__icontains=search)
            )

        if status:
            qs = qs.filter(
                Enquiry_status=status
            )

        if project:
            qs = qs.filter(
                project_id=project
            )

        if contacted_on:
            qs = qs.filter(
                contacted_on__date=contacted_on
            )

        return qs

    def changelist_view(self, request, extra_context=None):

        extra_context = extra_context or {}

        extra_context["inquiry_status_choices"] = (
            Inquiry.ENQUIRY_STATUS_CHOICES
        )

        project_model = (
            Inquiry._meta
            .get_field("project")
            .remote_field
            .model
        )

        extra_context["inquiry_projects"] = (
            project_model.objects
            .all()
            .order_by("project_name")
        )

        return super().changelist_view(
            request,
            extra_context=extra_context
        )

    # =====================================================
    # QUERYSET
    # =====================================================

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        # -------------------------------------------------
        # GET FILTER VALUES
        # -------------------------------------------------

        status = request.GET.get(
            "Enquiry_status"
        )

        project = request.GET.get(
            "project"
        )

        contacted_on = request.GET.get(
            "contacted_on"
        )

        search = request.GET.get(
            "q"
        )

        # -------------------------------------------------
        # CLEAN VALUES
        # -------------------------------------------------

        status = status.strip() if status else ""
        project = project.strip() if project else ""
        contacted_on = (
            contacted_on.strip()
            if contacted_on
            else ""
        )
        search = search.strip() if search else ""

        # =================================================
        # SEARCH
        # =================================================

        if search:

            qs = qs.filter(
                Q(name__icontains=search)
                | Q(phone__icontains=search)
                | Q(email__icontains=search)
                | Q(
                    project__project_name__icontains=search
                )
            )

        # =================================================
        # STATUS FILTER
        # =================================================

        if status:

            qs = qs.filter(
                Enquiry_status=status
            )

        # =================================================
        # PROJECT FILTER
        # =================================================

        if project:

            qs = qs.filter(
                project_id=project
            )

        # =================================================
        # DATE FILTER
        # =================================================

        if contacted_on:

            qs = qs.filter(
                contacted_on__date=contacted_on
            )

        # =================================================
        # RESPONSE COUNT
        # =================================================

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

        # =================================================
        # LAST RESPONSE
        # =================================================

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

        # =================================================
        # ANNOTATE
        # =================================================

        qs = qs.annotate(

            response_total=Subquery(
                response_count_subquery
            ),

            latest_response_at=Subquery(
                last_response_subquery
            ),

        )

        # =================================================
        # IMPORTANT
        # Latest inquiry per phone
        #
        # Status filter ke baad latest record
        # already filtered queryset se liya jayega.
        # =================================================

        latest_ids = (
            qs
            .order_by(
                "phone",
                "-contacted_on",
                "-id"
            )
            .values("id")
        )

        # =================================================
        # FINAL
        # =================================================

        return qs.filter(
            id__in=Subquery(
                latest_ids
            )
        )

    # =====================================================
    # RESPONSE COUNT
    # =====================================================

    @admin.display(
        description="Responses",
        ordering="response_total",
    )
    def response_count(self, obj):

        return obj.response_total or 0

    # =====================================================
    # LAST RESPONSE
    # =====================================================

    @admin.display(
        description="Last Response",
    )
    def last_response(self, obj):

        if obj.latest_response_at:

            return obj.latest_response_at.strftime(
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

    # ==========================================================
    # CUSTOM ADMIN TEMPLATE
    # ==========================================================

    change_list_template = (
        "admin/core/inquiry/price_inquiry_list.html"
    )

    # ==========================================================
    # LIST DISPLAY
    # ==========================================================

    list_display = (
        "customer_info",
        "project_info",
        "property_info",
        "inquiry_count",
        "last_enquiry",
        "history_button",
    )

    # ==========================================================
    # FILTERS
    # ==========================================================

    list_filter = (
        "status",
        "project",
        "property_type",
        "created_at",
    )

    # ==========================================================
    # SEARCH
    # ==========================================================

    search_fields = (
        "name",
        "phone",
        "email",
        "message",
        "property_area",
        "project__project_name",
    )

    # ==========================================================
    # READONLY
    # ==========================================================

    readonly_fields = (
        "created_at",
    )

    # ==========================================================
    # ORDERING
    # ==========================================================

    ordering = (
        "-created_at",
    )

    # ==========================================================
    # DISABLE ADD
    # ==========================================================

    def has_add_permission(self, request):
        return True

    # ==========================================================
    # GROUPING / QUERYSET
    #
    # Same:
    # Phone + Project + Property Area
    #
    # = One Card
    # ==========================================================

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        # ------------------------------------------------------
        # GROUP QUERY
        # ------------------------------------------------------

        group_qs = PriceBreakupInquiry.objects.filter(
            phone=OuterRef("phone"),
            project=OuterRef("project"),
            property_area=OuterRef("property_area"),
        )

        # ------------------------------------------------------
        # TOTAL ENQUIRY COUNT
        # ------------------------------------------------------

        count_subquery = (
            group_qs
            .values(
                "phone",
                "project",
                "property_area",
            )
            .annotate(
                total=Count("id"),
            )
            .values("total")[:1]
        )

        # ------------------------------------------------------
        # LAST ENQUIRY DATE
        # ------------------------------------------------------

        last_enquiry_subquery = (
            group_qs
            .order_by(
                "-created_at",
                "-id",
            )
            .values("created_at")[:1]
        )

        # ------------------------------------------------------
        # LATEST RECORD ID
        # ------------------------------------------------------

        latest_id_subquery = (
            group_qs
            .order_by(
                "-created_at",
                "-id",
            )
            .values("id")[:1]
        )

        # ------------------------------------------------------
        # RETURN ONLY LATEST RECORD OF EACH GROUP
        # ------------------------------------------------------

        return (
            qs
            .filter(
                id=Subquery(
                    latest_id_subquery
                )
            )
            .annotate(
                _inquiry_count=Subquery(
                    count_subquery
                ),
                _last_enquiry=Subquery(
                    last_enquiry_subquery
                ),
            )
            .order_by(
                "-_last_enquiry"
            )
        )

    # ==========================================================
    # CHANGE LIST
    #
    # Dashboard + Grid Cards
    # ==========================================================

    def changelist_view(
        self,
        request,
        extra_context=None,
    ):

        today = timezone.localdate()

        # ------------------------------------------------------
        # TOTAL ENQUIRIES
        # ------------------------------------------------------

        total_enquiries = (
            PriceBreakupInquiry.objects.count()
        )

        # ------------------------------------------------------
        # UNIQUE CUSTOMERS / GROUPS
        # ------------------------------------------------------

        unique_customers = (
            PriceBreakupInquiry.objects
            .values(
                "phone",
                "project",
                "property_area",
            )
            .distinct()
            .count()
        )

        # ------------------------------------------------------
        # REPEAT ENQUIRY GROUPS
        # ------------------------------------------------------

        repeat_enquiries = (
            PriceBreakupInquiry.objects
            .values(
                "phone",
                "project",
                "property_area",
            )
            .annotate(
                total=Count("id")
            )
            .filter(
                total__gt=1
            )
            .count()
        )

        # ------------------------------------------------------
        # TODAY'S ENQUIRIES
        # ------------------------------------------------------

        today_enquiries = (
            PriceBreakupInquiry.objects
            .filter(
                created_at__date=today
            )
            .count()
        )

        # ------------------------------------------------------
        # DASHBOARD DATA
        # ------------------------------------------------------

        extra_context = extra_context or {}

        extra_context.update({
            "total_enquiries": total_enquiries,
            "unique_customers": unique_customers,
            "repeat_enquiries": repeat_enquiries,
            "today_enquiries": today_enquiries,
        })

        # ------------------------------------------------------
        # DEFAULT ADMIN CHANGE LIST
        # ------------------------------------------------------

        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        # ------------------------------------------------------
        # GET CURRENT FILTERED / PAGINATED RESULTS
        # ------------------------------------------------------

        if (
            hasattr(response, "context_data")
            and "cl" in response.context_data
        ):

            cl = response.context_data["cl"]

            response.context_data["grid_cards"] = [
                self.render_grid_card(obj)
                for obj in cl.result_list
            ]

        return response

    # ==========================================================
    # GRID CARD
    # ==========================================================

    def render_grid_card(self, obj):

        # ------------------------------------------------------
        # PROJECT
        # ------------------------------------------------------

        project_name = (
            obj.project.project_name
            if obj.project
            else "Property Enquiry"
        )

        # ------------------------------------------------------
        # COUNT
        # ------------------------------------------------------

        inquiry_count = (
            getattr(obj, "_inquiry_count", 1) or 1
        )

        # ------------------------------------------------------
        # LAST ENQUIRY
        # ------------------------------------------------------

        last_enquiry = getattr(
            obj,
            "_last_enquiry",
            None,
        )

        if last_enquiry:
            last_enquiry_text = (
                last_enquiry.strftime(
                    "%d %b %Y, %I:%M %p"
                )
            )
        else:
            last_enquiry_text = "-"

        # ------------------------------------------------------
        # PROPERTY DATA
        # ------------------------------------------------------

        property_type = (
            obj.property_type or "-"
        )

        property_area = (
            obj.property_area or "-"
        )

        property_price = (
            obj.property_price or "-"
        )

        # ------------------------------------------------------
        # STATUS
        # ------------------------------------------------------

        status = obj.get_status_display()

        status_class_map = {

            "New": "status-new",

            "Contacted": "status-contacted",

            "Follow Up": "status-followup",

            "Interested": "status-interested",

            "Qualified": "status-qualified",

            "Site Visit": "status-sitevisit",

            "Negotiation": "status-negotiation",

            "Booked": "status-booked",

            "Not Interested": "status-not-interested",

            "Not Received": "status-not-received",

            "Callback": "status-callback",

            "Wrong Number": "status-wrong-number",

            "No Response": "status-no-response",

            "Lost": "status-lost",

            "Closed": "status-closed",
        }

        status_class = status_class_map.get(
            status,
            "status-default",
        )

        status_html = format_html(
            """
            <span class="inquiry-status {}">
                <i class="fa-solid fa-circle"></i>
                {}
            </span>
            """,
            status_class,
            status,
        )

        # ======================================================
        # EMAIL
        # ======================================================

        if obj.email:

            subject = (
                f"Property Enquiry - {project_name}"
            )

            body = f"""Hello {obj.name},

Thank you for your enquiry regarding {property_type} {property_area} at {project_name}.

We would be happy to assist you with the property details, pricing, availability and site visit.

Please feel free to reply to this email or contact us.

Regards,
Sales Team
{project_name}
"""

            email_url = (
                f"mailto:{obj.email}"
                f"?subject={quote(subject)}"
                f"&body={quote(body)}"
            )

            email_html = format_html(
                """
                <a
                    href="{}"
                    class="grid-contact grid-email"
                >
                    <i class="fa-solid fa-envelope"></i>
                    {}
                </a>
                """,
                email_url,
                obj.email,
            )

        else:

            email_html = format_html(
                """
                <span class="grid-contact grid-no-email">
                    <i class="fa-regular fa-envelope"></i>
                    {}
                </span>
                """,
                "No email",
            )

        # ======================================================
        # COUNT BADGE
        # ======================================================

        if inquiry_count > 1:

            count_html = format_html(
                """
                <span class="grid-count-badge repeat">
                    <i class="fa-solid fa-repeat"></i>
                    {} Times
                </span>
                """,
                inquiry_count,
            )

        else:

            count_html = format_html(
                """
                <span class="grid-count-badge single">
                    <i class="fa-solid fa-circle-check"></i>
                    {}
                </span>
                """,
                "1 Time",
            )

        # ======================================================
        # EDIT URL
        # ======================================================

        edit_url = reverse(
            "admin:core_pricebreakupinquiry_change",
            args=[obj.id],
        )

        # ======================================================
        # CALL URL
        # ======================================================

        phone_number = (
            str(obj.phone).strip()
            if obj.phone
            else ""
        )

        call_url = f"tel:{phone_number}"

        # ======================================================
        # WHATSAPP URL
        # ======================================================

        whatsapp_message = (
            f"Hello {obj.name}, "
            f"we received your enquiry regarding "
            f"{property_type} {property_area} "
            f"at {project_name}. "
            f"How can we assist you?"
        )

        whatsapp_url = (
            "https://wa.me/"
            f"{phone_number}"
            f"?text={quote(whatsapp_message)}"
        )

        # ======================================================
        # FINAL CARD
        # ======================================================

        return format_html(
            """
            <div class="enquiry-grid-card">

                <!-- ==========================================
                     CUSTOMER HEADER
                =========================================== -->

                <div class="grid-card-top">

                    <div class="grid-customer">

                        <div class="grid-avatar">
                            <i class="fa-solid fa-user"></i>
                        </div>

                        <div class="grid-customer-info">

                            <div class="grid-customer-name">
                                {}
                            </div>

                            <a
                                href="tel:{}"
                                class="grid-contact grid-phone"
                            >
                                <i class="fa-solid fa-phone"></i>
                                {}
                            </a>

                            {}

                        </div>

                    </div>

                    <div class="grid-card-actions">

                        <div class="grid-status">
                            {}
                        </div>

                        <div class="grid-count">
                            {}
                        </div>

                    </div>

                </div>


                <!-- ==========================================
                     PROJECT
                =========================================== -->

                <div class="grid-project">

                    <div class="grid-project-title">

                        <i class="fa-solid fa-building"></i>

                        <span>
                            {}
                        </span>

                    </div>

                    <div class="grid-project-subtitle">

                        <i class="fa-solid fa-location-dot"></i>

                        Property Enquiry

                    </div>

                </div>


                <!-- ==========================================
                     PROPERTY INFORMATION
                =========================================== -->

                <div class="grid-property">

                    <div class="grid-property-item">

                        <span class="grid-label">

                            <i class="fa-solid fa-house"></i>

                            Property

                        </span>

                        <strong>
                            {}
                        </strong>

                    </div>


                    <div class="grid-property-item">

                        <span class="grid-label">

                            <i class="fa-solid fa-ruler-combined"></i>

                            Area

                        </span>

                        <strong>
                            {}
                        </strong>

                    </div>


                    <div class="grid-property-item">

                        <span class="grid-label">

                            <i class="fa-solid fa-indian-rupee-sign"></i>

                            Price

                        </span>

                        <strong>
                            {}
                        </strong>

                    </div>

                </div>


                <!-- ==========================================
                     LAST ENQUIRY
                =========================================== -->

                <div class="grid-last-enquiry">

                    <div class="grid-clock">

                        <i class="fa-regular fa-clock"></i>

                    </div>

                    <div>

                        <span>
                            Last Enquiry
                        </span>

                        <strong>
                            {}
                        </strong>

                    </div>

                </div>


                <!-- ==========================================
                     CTA BUTTONS
                =========================================== -->

                <div class="grid-card-cta">

                    <!-- CALL -->

                    <a
                        href="{}"
                        class="grid-cta-btn grid-cta-call"
                        title="Call Customer"
                    >
                        <i class="fa-solid fa-phone"></i>
                        <span>Call</span>
                    </a>


                    <!-- WHATSAPP -->

                    <a
                        href="{}"
                        target="_blank"
                        rel="noopener"
                        class="grid-cta-btn grid-cta-whatsapp"
                        title="WhatsApp Customer"
                    >
                        <i class="fa-brands fa-whatsapp"></i>
                        <span>WhatsApp</span>
                    </a>


                    <!-- EDIT -->

                    <a
                        href="{}"
                        class="grid-cta-btn grid-cta-edit"
                        title="Edit Enquiry"
                    >
                        <i class="fa-solid fa-pen"></i>
                        <span>Edit</span>
                    </a>

                </div>

            </div>
            """,

            # 1. Customer name
            obj.name,

            # 2. Phone href
            obj.phone,

            # 3. Phone text
            obj.phone,

            # 4. Email
            email_html,

            # 5. Status
            status_html,

            # 6. Count
            count_html,

            # 7. Project
            project_name,

            # 8. Property type
            property_type,

            # 9. Area
            property_area,

            # 10. Price
            property_price,

            # 11. Last enquiry
            last_enquiry_text,

            # 12. Call URL
            call_url,

            # 13. WhatsApp URL
            whatsapp_url,

            # 14. Edit URL
            edit_url,
        )

    # ==========================================================
    # OLD TABLE METHODS
    # ==========================================================

    @admin.display(
        description="Customer",
        ordering="name",
    )
    def customer_info(self, obj):

        project_name = (
            obj.project.project_name
            if obj.project
            else "Property Enquiry"
        )

        property_text = " ".join(
            filter(
                None,
                [
                    obj.property_type,
                    obj.property_area,
                ],
            )
        )

        subject = (
            f"Property Enquiry - {project_name}"
        )

        body = f"""Hello {obj.name},

Thank you for your enquiry regarding {property_text or "the property"} at {project_name}.

We would be happy to assist you with the property details, pricing, availability and site visit.

Please feel free to reply to this email or contact us.

Regards,
Sales Team
{project_name}
"""

        if obj.email:

            email_url = (
                f"mailto:{obj.email}"
                f"?subject={quote(subject)}"
                f"&body={quote(body)}"
            )

            email_html = format_html(
                """
                <a
                    href="{}"
                    class="customer-contact email-link"
                >
                    <i class="fa-solid fa-envelope"></i>
                    {}
                </a>
                """,
                email_url,
                obj.email,
            )

        else:

            email_html = format_html(
                """
                <span class="customer-contact no-email">
                    <i class="fa-regular fa-envelope"></i>
                    {}
                </span>
                """,
                "No email",
            )

        return format_html(
            """
            <div class="customer-card">

                <div class="customer-avatar">
                    <i class="fa-solid fa-user"></i>
                </div>

                <div class="customer-details">

                    <div class="customer-name">
                        {}
                    </div>

                    <a
                        href="tel:{}"
                        class="customer-contact phone-link"
                    >
                        <i class="fa-solid fa-phone"></i>
                        {}
                    </a>

                    {}

                </div>

            </div>
            """,
            obj.name,
            obj.phone,
            obj.phone,
            email_html,
        )

    # ==========================================================

    @admin.display(
        description="Project",
    )
    def project_info(self, obj):

        project_name = (
            obj.project.project_name
            if obj.project
            else "No Project"
        )

        return format_html(
            """
            <div class="project-card">

                <div class="project-title">

                    <i class="fa-solid fa-building"></i>

                    <span>
                        {}
                    </span>

                </div>

                <div class="project-subtitle">

                    <i class="fa-solid fa-location-dot"></i>

                    Property Enquiry

                </div>

            </div>
            """,
            project_name,
        )

    # ==========================================================

    @admin.display(
        description="Property",
    )
    def property_info(self, obj):

        return format_html(
            """
            <div class="property-card">

                <div class="property-main">

                    <i class="fa-solid fa-house"></i>

                    <strong>
                        {}
                    </strong>

                </div>

                <div class="property-meta">

                    <span>

                        <i class="fa-solid fa-ruler-combined"></i>

                        {}

                    </span>

                    <span>

                        <i class="fa-solid fa-indian-rupee-sign"></i>

                        {}

                    </span>

                </div>

            </div>
            """,
            obj.property_type or "-",
            obj.property_area or "-",
            obj.property_price or "-",
        )

    # ==========================================================

    @admin.display(
        description="Enquiries",
        ordering="_inquiry_count",
    )
    def inquiry_count(self, obj):

        count = (
            obj._inquiry_count
            or 1
        )

        if count > 1:

            return format_html(
                """
                <span class="inquiry-badge repeat">

                    <i class="fa-solid fa-repeat"></i>

                    {} Times

                </span>
                """,
                count,
            )

        return format_html(
            """
            <span class="inquiry-badge single">

                <i class="fa-solid fa-circle-check"></i>

                {}

            </span>
            """,
            "1 Time",
        )

    # ==========================================================

    @admin.display(
        description="Last Enquiry",
        ordering="_last_enquiry",
    )
    def last_enquiry(self, obj):

        date = (
            obj._last_enquiry.strftime(
                "%d %b %Y, %I:%M %p"
            )
            if obj._last_enquiry
            else "-"
        )

        return format_html(
            """
            <div class="last-enquiry">

                <i class="fa-regular fa-clock"></i>

                <span>
                    {}
                </span>

            </div>
            """,
            date,
        )

    # ==========================================================

    @admin.display(
        description="Action",
    )
    def history_button(self, obj):

        url = reverse(
            "admin:core_pricebreakupinquiry_change",
            args=[obj.id],
        )

        return format_html(
            """
            <a
                href="{}"
                class="history-btn"
            >

                <i class="fa-solid fa-arrow-up-right-from-square"></i>

                View

            </a>
            """,
            url,
        )

    # ==========================================================
    # FONT AWESOME
    # ==========================================================

    class Media:

        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css",
            )
        }
