from utils.exceptions import HumanReadableError
from utils.views import RestAPIView


class ContactMeEmailView(RestAPIView):
    """Contact me email view."""

    def post(self, request, *args, **kwargs):
        """Send email to me."""
        try:
            data = request.data
            self.pprint_data(data)
            response = {
                "title": "Sucess!",
                "message": "Your message has been sent.",
            }
            return self.success_response(response)
        except HumanReadableError as exc:
            return self.error_response(exc)
        except Exception as exc:
            return self.server_error_response(exc)
