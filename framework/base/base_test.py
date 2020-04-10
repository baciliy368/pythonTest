import unittest


from framework.utils.client_manager import configure_client, clean_client


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        configure_client()

    def tearDown(self) -> None:
        clean_client()
