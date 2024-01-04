from django_rq import job
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from weasyprint import HTML
from order.models import Check


@job
def generate_pdf(check_id):
    check = Check.objects.get(id=check_id)
    template_path = f"order/{check.type}_check.html"
    template = get_template(template_path)
    html_content = template.render({"order": check.order})
    pdf_path = f"media/pdf/{check.id}_{check.type}.pdf"
    HTML(string=html_content).write_pdf(
        pdf_path, stylesheets=[f"{settings.STATIC_ROOT}/css/receipt_style.css"]
    )
    check.pdf_file.name = pdf_path
    check.status = "rendered"
    check.save()
