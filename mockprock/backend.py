"""
To enable this backend, configure your LMS and CMS settings like this:
PROCTORING_BACKENDS = {
    'DEFAULT': 'mockprock',
    'mockprock': {
        'client_id': 'abcd',
        'client_secret': 'secret'
    }
}
"""

from edx_proctoring.backends.rest import BaseRestProctoringProvider


class MockProckBackend(BaseRestProctoringProvider):
    base_url = 'https://mockprock-master-proctoring.raccoongang.com'
    verbose_name = 'Mock Proctoring Service'
    tech_support_email = 'support@youjustgotmockprockd.com'
    tech_support_phone = '+1 605 475 6968'
    needs_oauth = True
    token_expiration_time = 86400
    npm_module = '@edx/mockprock'

