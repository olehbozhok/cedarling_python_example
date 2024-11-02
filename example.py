from cedarling_python import MemoryLogConfig, DisabledLoggingConfig, StdOutLogConfig
from cedarling_python import PolicyStoreSource, PolicyStoreConfig, BootstrapConfig, JwtConfig
from cedarling_python import Cedarling
from cedarling_python import ResourceData, Request

# use log config to store logs in memory with a time-to-live of 120 seconds
# by default it is 60 seconds
log_config = MemoryLogConfig(log_ttl=100)
# we can also set value to as property
# log_config.log_ttl = 120

# use disabled log config to ignore all logging
# log_config = DisabledLoggingConfig()

# use log config to print logs to stdout
log_config = StdOutLogConfig()

# Create policy source configuration
with open("policy_store.json",
          mode="r", encoding="utf8") as f:
    policy_raw_json = f.read()
# for now we support only json source
policy_source = PolicyStoreSource(json=policy_raw_json)

policy_store_config = PolicyStoreConfig(source=policy_source)

# Create jwt configuration
# do not validate JWT tokens
jwt_config = JwtConfig(enabled=False)

# collect all in the BootstrapConfig
bootstrap_config = BootstrapConfig(
    application_name="TestApp",
    log_config=log_config,
    policy_store_config=policy_store_config,
    jwt_config=jwt_config
)

# initialize cedarling instance
# all values in the bootstrap_config is parsed and validated at this step.
instance = Cedarling(bootstrap_config)

# returns a list of all active log ids
# active_log_ids = instance.get_log_ids()

# get log entry by id
# log_entry = instance.get_log_by_id(active_log_ids[0])


# show logs
print("Logs stored in memory:")
print(*instance.pop_logs(), sep="\n\n")


# //// Execute authentication request ////

# field resource_type and id is mandatory
# other fields are attributes of the resource.
resource = ResourceData(resource_type="Jans::Issue",
                        id="random_id", org_id="some_long_id", country="US")
# or we can init resource using dict
resource = ResourceData.from_dict({
    "type": "Jans::Issue",
    "id": "random_id",
    "org_id": "some_long_id",
    "country": "US"
})

action_token = "eyJraWQiOiJjb25uZWN0X2JmZmVhYzA4LTEyZTgtNGJiYy04YjA3LTAxOTk0NGI3MjJlNF9zaWdfcnMyNTYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJKM0JtdG5QUEI4QmpNYlNjV21SOGNqVDlnV0NDVEhLZlNmMGRrYk92aEdnIiwiY29kZSI6IjY5N2RhODBkLTE2YWQtNDFmOC1hZDhlLWM3MWY4ODFjNTQ3MyIsImlzcyI6Imh0dHBzOi8vdGVzdC1jYXNhLmdsdXUuaW5mbyIsInRva2VuX3R5cGUiOiJCZWFyZXIiLCJjbGllbnRfaWQiOiI5NWJkNjNkMi04NWVkLTQwYWQtYmQwMy0zYzE4YWY3OTdjYTQiLCJhdWQiOiI5NWJkNjNkMi04NWVkLTQwYWQtYmQwMy0zYzE4YWY3OTdjYTQiLCJhY3IiOiJzaW1wbGVfcGFzc3dvcmRfYXV0aCIsIng1dCNTMjU2IjoiIiwibmJmIjoxNzMwNDk0NTQzLCJzY29wZSI6WyJyb2xlIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTczMDQ5NDU0MiwiZXhwIjoxNzMwNTc0MjQ1LCJpYXQiOjE3MzA0OTQ1NDMsImp0aSI6InFwQ3U1MlowUzh5bmZaN3VmQ1hRb3ciLCJ1c2VybmFtZSI6Ik9sZWggQm96aG9rIiwic3RhdHVzIjp7InN0YXR1c19saXN0Ijp7ImlkeCI6MTAwMywidXJpIjoiaHR0cHM6Ly90ZXN0LWNhc2EuZ2x1dS5pbmZvL2phbnMtYXV0aC9yZXN0djEvc3RhdHVzX2xpc3QifX19.A-k8fP9yqF-LwyNniohlLzwy2y0smbkavubNHKiNn8zAWAz0PFcQXnDKJEpcigXS7iwBRieHcEAgCrBCbsPKZDHOohwx2CFNPK1AvECRmd0U69siaEJqljECiUHqLkHOT9LD89Ag752QNauuQvXnHKuVIKJ7ykg7Jcc5-gi_mH_OfGAz-yYPYJLy0tBiT9LDFu1sQT04P5MqzrSxwBk3PW7Af3W0Dl-hl77SSAAKy7TkYuTEPWLat0nMwuLNzgBkmsGwPdPGmZl5YqMv1VOpr19Xjopr8lMAHN1CdEEFCXoBZewwXGPQFzoF_J9CW95tx_T16Z6iM2EXoIJyplgSwg"
"""
JSON payload of access token
{
  "sub": "J3BmtnPPB8BjMbScWmR8cjT9gWCCTHKfSf0dkbOvhGg",
  "code": "697da80d-16ad-41f8-ad8e-c71f881c5473",
  "iss": "https://test-casa.gluu.info",
  "token_type": "Bearer",
  "client_id": "95bd63d2-85ed-40ad-bd03-3c18af797ca4",
  "aud": "95bd63d2-85ed-40ad-bd03-3c18af797ca4",
  "acr": "simple_password_auth",
  "x5t#S256": "",
  "nbf": 1730494543,
  "scope": [
    "role",
    "openid"
  ],
  "auth_time": 1730494542,
  "exp": 1730574245,
  "iat": 1730494543,
  "jti": "qpCu52Z0S8ynfZ7ufCXQow",
  "username": "Oleh Bozhok",
  "status": {
    "status_list": {
      "idx": 1003,
      "uri": "https://test-casa.gluu.info/jans-auth/restv1/status_list"
    }
  }
}
"""

id_token = "eyJraWQiOiJjb25uZWN0X2JmZmVhYzA4LTEyZTgtNGJiYy04YjA3LTAxOTk0NGI3MjJlNF9zaWdfcnMyNTYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdF9oYXNoIjoiemFqTC1JRVBiSjdYcHJiQWdpNUxBZyIsInN1YiI6IkozQm10blBQQjhCak1iU2NXbVI4Y2pUOWdXQ0NUSEtmU2YwZGtiT3ZoR2ciLCJhbXIiOltdLCJpc3MiOiJodHRwczovL3Rlc3QtY2FzYS5nbHV1LmluZm8iLCJub25jZSI6ImI5YjZkZjUxLWEwNGEtNDc1YS05MTQxLTNmZTU4OWMyYWFiOCIsInNpZCI6IjcxZWVkYjNhLTdjMTgtNDIwYy05ZmVhLTM3ZDY1MzI5OTBlNiIsImphbnNPcGVuSURDb25uZWN0VmVyc2lvbiI6Im9wZW5pZGNvbm5lY3QtMS4wIiwiYXVkIjoiOTViZDYzZDItODVlZC00MGFkLWJkMDMtM2MxOGFmNzk3Y2E0IiwiYWNyIjoic2ltcGxlX3Bhc3N3b3JkX2F1dGgiLCJjX2hhc2giOiJwUWk5cllxbVNDVmMzdEstLTJBZ2lBIiwibmJmIjoxNzMwNDk0NTQzLCJhdXRoX3RpbWUiOjE3MzA0OTQ1NDIsImV4cCI6MTczMDQ5ODE0MywiZ3JhbnQiOiJhdXRob3JpemF0aW9uX2NvZGUiLCJpYXQiOjE3MzA0OTQ1NDMsImp0aSI6InYyU1dHZkFFUUdXWjFtUERTSlB2YmciLCJzdGF0dXMiOnsic3RhdHVzX2xpc3QiOnsiaWR4IjoxMDA0LCJ1cmkiOiJodHRwczovL3Rlc3QtY2FzYS5nbHV1LmluZm8vamFucy1hdXRoL3Jlc3R2MS9zdGF0dXNfbGlzdCJ9fX0.Ot6WNQlg4hVPA4b6dRPO-tr6V20EzEm_3SMN-qRkfpkWQ-GSccFLed5G4sBLh_YIN-qh-P7gsFGg7Y6QS7tsR6CgNB0uVu3lqpqqrkvwxUw0DS4DYQFZ2pZygfVqQc9o7V9JThdVG7VG_SZXnKa8H8ORmp9JbTOTrLqAOgoQ1YdFfcceWob5BcFLCOXXOao90ESC5ntIHXm4lVwjN19odJHgoJ9qRFE69pm4vgqZ211cbfkoA_D12TDEaVmJ5n_982i7OvwK2zdNHlqlVTKN9Ncy6gvvRHb1RsgaVjp5Nd--oMdlb76wy94VIqdbFqDAXpogzS-K2m5n0yGfOhchAw"
"""
JSON payload of id token
{
  "at_hash": "zajL-IEPbJ7XprbAgi5LAg",
  "sub": "J3BmtnPPB8BjMbScWmR8cjT9gWCCTHKfSf0dkbOvhGg",
  "amr": [],
  "iss": "https://test-casa.gluu.info",
  "nonce": "b9b6df51-a04a-475a-9141-3fe589c2aab8",
  "sid": "71eedb3a-7c18-420c-9fea-37d6532990e6",
  "jansOpenIDConnectVersion": "openidconnect-1.0",
  "aud": "95bd63d2-85ed-40ad-bd03-3c18af797ca4",
  "acr": "simple_password_auth",
  "c_hash": "pQi9rYqmSCVc3tK--2AgiA",
  "nbf": 1730494543,
  "auth_time": 1730494542,
  "exp": 1730498143,
  "grant": "authorization_code",
  "iat": 1730494543,
  "jti": "v2SWGfAEQGWZ1mPDSJPvbg",
  "status": {
    "status_list": {
      "idx": 1004,
      "uri": "https://test-casa.gluu.info/jans-auth/restv1/status_list"
    }
  }
}
"""

userinfo_token = "eyJraWQiOiJjb25uZWN0X2JmZmVhYzA4LTEyZTgtNGJiYy04YjA3LTAxOTk0NGI3MjJlNF9zaWdfcnMyNTYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJKM0JtdG5QUEI4QmpNYlNjV21SOGNqVDlnV0NDVEhLZlNmMGRrYk92aEdnIiwiYXVkIjoiOTViZDYzZDItODVlZC00MGFkLWJkMDMtM2MxOGFmNzk3Y2E0Iiwicm9sZSI6WyJNYW5hZ2VyIiwiU3VwcG9ydCJdLCJpc3MiOiJodHRwczovL3Rlc3QtY2FzYS5nbHV1LmluZm8iLCJqdGkiOiJxT3hrbE1ZZlNmcWRZZ1hsMDFqOXdBIiwiY2xpZW50X2lkIjoiOTViZDYzZDItODVlZC00MGFkLWJkMDMtM2MxOGFmNzk3Y2E0In0.DyXs_NEN6-KMebTHJu1_54CXOlrEWube85pV4ZIoNz_EqePZnirSydfNQJZMf1RLXauZIhug0EOpGxbIqRMfGTOlHqTc9nwXN82lRSkF0ctUkl-t3jeJNOXmQQLjDGEhI2IXjmDcIwvms1qy-QUtct9ccniEt6SdfROnSYhY8rAVYLaf34UJmUCav01Q9iGBn5E_ASr4G8zZibq4b9z_AX6DNZilmVeJIy4HLPRNdAtsJs6YHuQDN1QzQNJiFxrJlytMXwdMh1mXRIADBFVsIVte0fHOJBqhPS60t81qsa4r9tE9tJ-li5yRLGNFgab0zdUjPp0M6DrKUigq-nPBQg"
"""
JSON payload of userinfo token
{
  "sub": "J3BmtnPPB8BjMbScWmR8cjT9gWCCTHKfSf0dkbOvhGg",
  "aud": "95bd63d2-85ed-40ad-bd03-3c18af797ca4",
  "role": [
    "Manager",
    "Support"
  ],
  "iss": "https://test-casa.gluu.info",
  "jti": "qOxklMYfSfqdYgXl01j9wA",
  "client_id": "95bd63d2-85ed-40ad-bd03-3c18af797ca4"
}
"""

# Creating cedarling request
request = Request(
    action_token,
    id_token,
    userinfo_token,
    action='Jans::Action::"Update"',
    context={}, resource=resource)

# Authorize call
authorize_result = instance.authorize(request)
print(*instance.pop_logs(), sep="\n\n")

# if you change org_id result will be false
print("result of request: ", authorize_result.is_allowed())

# watch on the decision for workload
workload_result = authorize_result.workload()
print("workload decision", workload_result.decision)

# show diagnostic information
# workload_diagnostic = workload_result.diagnostics
# for i, reason in enumerate(workload_diagnostic.reason):
#     if i == 0:
#         print("reason policies:")
#     print(reason)

# for i, error in enumerate(workload_diagnostic.errors):
#     if i == 0:
#         print("errors:")
#     print("id:", error.id, "error:", error.error)


# watch on the decision for person
print("person decision", authorize_result.person().decision)


# watch on the decision for role if present
role_result = authorize_result.role()
if role_result is not None:
    print("role decision", authorize_result.role().decision)
