import logging
import datetime


class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        pass

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True

        """
        request_uri = request.get('path', '')
        if self.is_start_with(request_uri):
            return True

        user = self.get_jwt_user(request)
        if user is None:
            return False

        self.set_current_user_info_and_log(user)
        return True

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        Currently, the prefixes being checked are "/api" and "/login".
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.is_start_with('/api/data')
        True

        """
        if not isinstance(request_uri, str):
            return False
        return request_uri.startswith(('/api', '/login'))

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
        {'user': {'name': 'user1'}

        """
        try:
            auth = request['headers']['Authorization']
        except (KeyError, TypeError):
            return None

        if not isinstance(auth, dict):
            return None

        user_info = auth.get('user')
        token = auth.get('jwt')
        if not isinstance(user_info, dict) or not token:
            return None

        name = user_info.get('name')
        if name is None:
            return None

        expected = str(name) + str(datetime.date.today())
        if token != expected:
            return None

        return {'user': user_info}

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        >>> filter = AccessGatewayFilter()
        >>> user = {'name': 'user1', 'address': '127.0.0.1'}
        >>> filter.set_current_user_info_and_log(user)

        """
        info = user.get('user', user) if isinstance(user, dict) else {}
        name = info.get('name') if isinstance(info, dict) else None
        address = info.get('address') if isinstance(info, dict) else None

        self.current_user = info
        logging.getLogger(__name__).info(
            "access log: user=%s address=%s time=%s",
            name,
            address,
            datetime.datetime.now().isoformat(),
        )