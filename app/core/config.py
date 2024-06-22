from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'secret'

    type: str
    project_id: str
    private_key_id: str
    private_key: str
    client_id: str
    auth_uri: str
    token_uri: str
    auth_provider_x509_cert_url: str
    client_x509_cert_url: str
    universe_domain: str
    email: str

    class Config:
        env_file = '.env'


settings = Settings()
