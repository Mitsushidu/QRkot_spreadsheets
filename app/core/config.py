from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'secret'

    type: str = "service_account",
    project_id: str = "warm-physics-419911",
    private_key_id: str = "ccbb7aa84c7b7ec2b8896caeed74d5abd77199b3",
    private_key: str = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCwazAzGCr6oJxg\nGiNDNFGi6dKaJ3kqwogluswhIbKYVVn492Pwlev5Ak0xq8hWAiKr1QplOMTpHAle\nW1FeNgZozPXN7cQSjNyDFVtu6c2GnIy7lZ3yLKZmVboCk8op0h5WGRn0W1A/RMVf\n3BBh3jV693WX2VzU0Lds/Q6yPaCdPJ/j8rDSv0Vnp861dMhNM9GE/nzmZGogiHT4\nFC32ZcKCmytnCKZYbkoL3pGD38kWRR7cFhtmFRpsheb+G/WqTAX82lv8y1CWneTE\n0n21koncbLgaYNjYh8EZn3Y5jbSzgxzg6FWdl8hZo8bGKguNO14xjmAlw5PjB5Fr\nFed9hAA3AgMBAAECggEABgE1UXKPzpq2N98r4WxfyvfCdKobSa/4CltipKNiUiUK\n5u/PYFpPVIPA34vv9F17k0sGYOOfGtVwIYdiLElny8a40cWMrZpLIdBm8vjU8gaq\nE53IE9Ieknp11liewkWl8AWdXd/YdLmBLlNt4KbmPcU7z2tVPuPLxSiSiNE9gkcw\nzzVvUIh8lZOvdgvZsq+C7Qka7kNLkDNdQPB5XXtM6bFoBkIdnSSQzR7JhleCVb5G\nZuPbHXwqD2yZYr+jB1PeQsaMI+oT/BztRSutzzyzPuFkpb7YO5hgpaa+k0UaxWY3\nI2a8TTn4tf3XuwFJnOlOAwLhxARSKSU4eab0Q+xaQQKBgQDjgaBfDsZjHS0Qd7BJ\nehIj69lN9JPPumnwf3AgK88EedZ5SZD22tyeLhhdpIpHlHWQ+v1NMtK0Yhaokkxb\nVft1g7N8O8MkeP/ALbN5yHlKmexnoYYgCZWloah6CK9wAAYA671BbOs1Py4IYFHd\nLrstDvgi7bRtlfURZOLYT0DqnwKBgQDGg5M3OHEuaQ1eZ+06SZUFrJM1I0pZbIQb\nnmQiOXNtIF+BpY+5Xmi+zNYeeSbpHCLuwmMYadEQZcmVt3ARfyIrovx1lSrEHiAM\nyOVxw803z1uk4lep/do1ZuWD1xVGGNOn7+dTZCItMn8vr/ENXu5V+e807elpAHsh\nvbvxn7sbaQKBgQDS8puf6FQ9DI1/ams0BhMR6ZrJNJFlmESosZFm0xgV317lgTgA\nHDlaFgWTtoBdFKPaNU9vKEPE6/p0fYp9WgFaGi7vb35msCb7q6RxtFf6uzQ/dr6l\nsB1owbc0yB7bq7nlWrBWHMcOzTFCpQTjIHR/uBSOVnfo8JWWdkP8K6hWowKBgHCP\n4OT56yt+w+bZFSns2UQ7Y8lItnrYTlx+xpalbu7c4WrZHxLkFo7CBVOILOkXXDN4\nI8qPDc23ecOcHT6+kPifVXmy2GoWDuRQ8dE9TlssB/IJqd2pJJcNPm0wg06Y+0MJ\nhGjDqaFpNbcrk4qaXph/vQSNNsGkVS1/sVdD1EupAoGBAJo7TAr9asKUvO9SgTdO\nSWgA81DU+8Sh1htjty92QyvWTD4Hxklz8JTeee3a5odpTVXD0kf4ivk3JWCRXL68\n7mZESpOG4XgWCLTtD4dw+upNm4gVwp0iFGRdQFMO/aV7fEopgB35+3huLU6P5woh\n6I2A/Iq11LOOYRia/P4n8wNx\n-----END PRIVATE KEY-----\n",
    client_email: str = "mtsshd-practice@warm-physics-419911.iam.gserviceaccount.com",
    client_id: str = "117526244174295614178",
    auth_uri: str = "https://accounts.google.com/o/oauth2/auth",
    token_uri: str = "https://oauth2.googleapis.com/token",
    auth_provider_x509_cert_url: str = "https://www.googleapis.com/oauth2/v1/certs",
    client_x509_cert_url: str = "https://www.googleapis.com/robot/v1/metadata/x509/mtsshd-practice%40warm-physics-419911.iam.gserviceaccount.com",
    universe_domain: str = "googleapis.com"
    email: str = 'fireminergoodplay@gmail.com'

    class Config:
        env_file = '.env'


settings = Settings()