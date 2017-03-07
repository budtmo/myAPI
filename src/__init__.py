import os

WORKDIR = os.path.dirname(__file__)

_db_host = os.getenv('DB_HOST')
_db_name = os.getenv('DB_NAME')
_db_user = os.getenv('DB_USER')
_db_password = os.getenv('DB_PASS')

if not _db_host or not _db_name or not _db_user or not _db_password:
    raise ValueError('DB_HOST, DB_NAME, DB_USER, DB_PASSWORD environment variable have to be set!')

database_config = {
    'host': _db_host,
    'dbname': _db_name,
    'username': _db_user,
    'password': _db_password,
    'port': 5432
}


def get_number_of_pages(num_of_items: int, page_size: int) -> int:
    """
    Get number of pages
    :param num_of_items: number of items in database
    :param page_size: size of one page
    :return: number of pages
    """
    return int((num_of_items / float(page_size)) + int(num_of_items % float(page_size) > 0))
