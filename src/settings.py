import os


def get_or_raise(env):
    """
    Check if needed environment variables are given.

    :param env: key
    :type env: str
    :return: value
    :rtype: str
    """
    env_value = os.getenv(env)
    if not env_value:
        raise RuntimeError('The environment variable {0:s} should be set.'.format(env))
    return env_value

DB_HOST = get_or_raise('DB_HOST')
DB_NAME = get_or_raise('DB_NAME')
DB_USER = get_or_raise('DB_USER')
DB_PASS = get_or_raise('DB_PASS')
DB_PORT = 5432

APP_PORT = 8080
