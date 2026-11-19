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
        if "://" not in self.url:
            return None
        return self.url.split("://", 1)[0]


    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
        if "://" not in self.url:
            return None
        rest = self.url.split("://", 1)[1]
        end = len(rest)
        for delimiter in ("/", "?", "#"):
            index = rest.find(delimiter)
            if index != -1 and index < end:
                end = index
        return rest[:end]


    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
        if "://" not in self.url:
            return None
        rest = self.url.split("://", 1)[1]
        index = rest.find("/")
        if index == -1:
            return ""
        return rest[index:]


    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
        if "://" not in self.url:
            return None
        rest = self.url.split("://", 1)[1]
        # Drop the fragment first so a '?' inside it is not mistaken for the query start
        without_fragment = rest.split("#", 1)[0]
        if "?" not in without_fragment:
            return None
        query = without_fragment.split("?", 1)[1]
        params = {}
        for pair in query.split("&"):
            if not pair:
                continue
            if "=" in pair:
                key, value = pair.split("=", 1)
            else:
                key, value = pair, ""
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
        if "://" not in self.url:
            return None
        rest = self.url.split("://", 1)[1]
        if "#" not in rest:
            return None
        return rest.split("#", 1)[1]