class URLHandler:
    """
    The class supports to handle URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        self.url = url

    def get_scheme(self):
        """
        get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """
        scheme, sep, _ = self.url.partition("://")
        if not sep:
            return ""
        return scheme


    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
        _, sep, rest = self.url.partition("://")
        if not sep:
            return ""
        host = rest.split("/", 1)[0]
        host = host.split("?", 1)[0]
        host = host.split("#", 1)[0]
        return host


    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
        _, sep, rest = self.url.partition("://")
        if not sep:
            return ""
        indices = [rest.find(c) for c in ("/", "?", "#") if c in rest]
        if not indices:
            return ""
        return rest[min(indices):]


    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
        without_fragment = self.url.partition("#")[0]
        _, sep, query = without_fragment.partition("?")
        if not sep:
            return None
        params = {}
        for pair in query.split("&"):
            if not pair:
                continue
            key, _, value = pair.partition("=")
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
        _, sep, fragment = self.url.partition("#")
        if not sep:
            return None
        return fragment