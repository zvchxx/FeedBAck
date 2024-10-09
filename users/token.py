from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class MyPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_token_hash(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
    


email_verification_token = MyPasswordResetTokenGenerator()