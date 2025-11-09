# settings file for easy management of config for backend.
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    """
    Manages application settings using environment variables.
    """
    
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../.env'), env_file_encoding='utf-8', extra='ignore')

    DATABASE_URL: str = "mysql+mysqlconnector://root:password@localhost:3306/solar_site_analyzer"
    
    # frontend url hardcoded for CORS 
    CLIENT_ORIGIN_URL: str = "http://localhost:5173" 
settings = Settings()