import json

DEFAULT_COOKIES = {'key1': 'value1', 'key2': 'value2'}


class CookiesUtil:
    """
    This is a class as utility for managing and manipulating Cookies, including methods for retrieving, saving, and setting Cookies data.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = None

    def get_cookies(self, reponse):
        """
        Gets the cookies from the specified response,and save it to cookies_file.
        :param reponse: The response to get cookies from, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """
        cookies = {}
        if isinstance(reponse, dict):
            value = reponse.get('cookies', {})
            if isinstance(value, dict):
                cookies = value
        self.cookies = cookies
        self._save_cookies()

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.load_cookies()
        {'key1': 'value1', 'key2': 'value2'}

        """
        if self.cookies is not None:
            data = self.cookies
        else:
            try:
                with open(self.cookies_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (OSError, ValueError, TypeError):
                if self.cookies_file:
                    # No usable cookies file yet: seed it with the default cookies.
                    data = dict(DEFAULT_COOKIES)
                    self.cookies = data
                    self._save_cookies()
                else:
                    data = {}

        if isinstance(data, dict) and 'cookies' in data and isinstance(data['cookies'], dict):
            cookies = data['cookies']
        elif isinstance(data, dict):
            cookies = data
        else:
            cookies = {}

        self.cookies = cookies
        return cookies

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util._save_cookies()
        True

        """
        if not self.cookies_file:
            return False
        try:
            with open(self.cookies_file, 'w', encoding='utf-8') as f:
                json.dump({'cookies': self.cookies or {}}, f)
            return True
        except (OSError, TypeError, ValueError):
            return False