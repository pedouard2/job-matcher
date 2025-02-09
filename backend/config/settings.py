from dynaconf import Dynaconf
import os

load_dotenv = os.getenv("DYNACONF_ENV") != "prod"

settings = Dynaconf(
    settings_files=["settings.yaml"],
    envvar_prefix=False,
    environments=True,
    load_dotenv=load_dotenv,
    env_switcher="DYNACONF_ENV",
)
