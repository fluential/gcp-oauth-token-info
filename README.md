# gcp-oauth-token-info
Retrieve auth token information from Google OAuth2 endpoint

When working with remote GCP resources often it's good practice to relay on the CLOUDSDK_AUTH_ACCESS_TOKEN, this token can be easily obtained by doing running `gcloud auth print-access-token` and reused in a way like:

```shell
> export CLOUDSDK_AUTH_ACCESS_TOKEN=<token>
> gcloud compute instances list
```

But it's not easy to identify user identity of such tokens which is important when you work with different Service Account, environments etc.
This small snippet will retrieve token info from Google API endpoint:

```shell
export CLOUDSDK_AUTH_ACCESS_TOKEN=<token>
./gcp-oauth-token-info.py
2024-12-04 05:44:50 - INFO - Token Information:
2024-12-04 05:44:50 - INFO - {
  "azp": "721552944539.apps.googleusercontent.com",
  "aud": "721552944539.apps.googleusercontent.com",
  "sub": "777455885472527483726",
  "scope": "https://www.googleapis.com/auth/accounts.reauth https://www.googleapis.com/auth/appengine.admin https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/compute https://www.googleapis.com/auth/sqlservice.login https://www.googleapis.com/auth/userinfo.email openid",
  "exp": "1733315061",
  "expires_in": "2370",
  "email": "foo@bar",
  "email_verified": "true",
  "access_type": "offline"
}
```
