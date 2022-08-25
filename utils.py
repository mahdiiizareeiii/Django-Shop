from urllib import response
from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin
def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI("58724E614C59706176706C633579414952627A6A51774E2B3931463655505176494D3662773838703572733D")
        params = {
            "sender":"",
            "receptor": phone_number,
            "message": f"کد تایید شما{code}"
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin