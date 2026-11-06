class URLHandler:
    """
    The class supports to handle URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        self.url = url

    def _split_scheme(self):
        if "://" in self.url:
            scheme, rest = self.url.split("://", 1)
        else:
            scheme, rest = "", self.url
        return scheme, rest

    def _split_host(self):
        _, rest = self._split_scheme()
        end = len(rest)
        for ch in "/?#":
            idx = rest.find(ch)
            if idx != -1 and idx < end:
                end = idx
        return rest[:end], rest[end:]

    def get_scheme(self):
        """
        get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """
        scheme, _ = self._split_scheme()
        return scheme

    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
        host, _ = self._split_host()
        return host

    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
        _, path = self._split_host()
        return path

    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
        _, path = self._split_host()
        path = path.split("#", 1)[0]
        if "?" not in path:
            return {}
        query = path.split("?", 1)[1]
        params = {}
        for item in query.split("&"):
            if not item:
                continue
            if "=" in item:
                key, value = item.split("=", 1)
            else:
                key, value = item, ""
            params[key] = value
        return params

    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
        _, path = self._split_host()
        if "#" not in path:
            return ""
        return path.split("#", 1)[1]