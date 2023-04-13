import logging

from django.utils import timezone

from utils.exceptions import HumanReadableError
from utils.views import RestAPIView

logger = logging.getLogger("contact_me_email")


class ContactMeEmailView(RestAPIView):
    """Contact me email view."""

    def post(self, request, *args, **kwargs):
        """Send email to me."""
        try:
            data = request.data
            self.send_email(data)
            response = {
                "title": "Sucess!",
                "message": "Your message has been sent.",
            }
            return self.success_response(response)
        except HumanReadableError as exc:
            return self.error_response(exc)
        except Exception as exc:
            return self.server_error_response(exc)

    def send_email(self, data: dict) -> None:
        """Send email data."""
        self.log_email(data)

    def log_email(self, data: dict) -> None:
        """Log email data.


        Contact Me Form Submission Data Sample:
        ===============================
        Name: Xander De Vouer
        Email: xander@devouer.com
        Subject: Full Time Senior Developer Role
        Message: Hi we're looking for a Django Full Time Senior Developer Role. Are you interested?
        """
        name = data["contact-me-name"]
        email = data["contact-me-email"]
        subject = data["contact-me-subject"]
        message = data["contact-me-message"]

        email_message = """
        ========== Contact Me Submittion Received ==========
        From: {}
        Email: {}
        Subject: {}
        Message:{}
        Date: {}
        """.format(
            name,
            email,
            subject,
            message,
            timezone.now(),
        )

        logger.info(email_message)
