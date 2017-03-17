import os

WORKDIR = os.path.dirname(__file__)
SWAGGER_PATH = os.path.join(WORKDIR, 'swagger')


def get_number_of_pages(num_of_items: int, page_size: int) -> int:
    """
    Get number of pages
    :param num_of_items: number of items in database
    :param page_size: size of one page
    :return: number of pages
    """
    return int((num_of_items / float(page_size)) + int(num_of_items % float(page_size) > 0))
