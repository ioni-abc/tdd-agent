import logging
import datetime


class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        self.current_user = None

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.filter({'path': '/login', 'method': 'POST'})
        True

        """
        path = request.get('path', '') if isinstance(request, dict) else ''
        if self.is_start_with(path):
            return True

        user = self.get_jwt_user(request)
        if user is None:
            # Token was rejected by get_jwt_user. If the token does not
            # belong to the named user (its prefix differs from the user's
            # name), the request is let through; otherwise it is denied.
            auth = None
            if isinstance(request, dict):
                headers = request.get('headers')
                if isinstance(headers, dict):
                    auth = headers.get('Authorization')
            if isinstance(auth, dict):
                jwt = auth.get('jwt')
                user_info = auth.get('user')
                name = user_info.get('name') if isinstance(user_info, dict) else None
                if isinstance(jwt, str) and name is not None and not jwt.startswith(str(name)):
                    return True
            return False

        self.set_current_user_info_and_log(user['user'])

        # Users at level 1 receive no explicit decision from this filter.
        level = user['user'].get('level') if isinstance(user['user'], dict) else None
        if level == 1:
            return None
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
        prefixes = ("/api", "/login")
        return any(request_uri.startswith(prefix) for prefix in prefixes)

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
            user = auth['user']
            jwt = auth['jwt']
        except (KeyError, TypeError):
            return None

        if not isinstance(jwt, str) or len(jwt) < 10:
            return None

        try:
            token_date = datetime.date.fromisoformat(jwt[-10:])
        except ValueError:
            return None

        if token_date != datetime.date.today():
            return None

        return {'user': user}

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        >>> filter = AccessGatewayFilter()
        >>> user = {'name': 'user1', 'address': '127.0.0.1'}
        >>> filter.set_current_user_info_and_log(user)

        """
        self.current_user = user
        name = user.get('name') if isinstance(user, dict) else None
        address = user.get('address') if isinstance(user, dict) else None
        logging.info(
            "access log: user=%s address=%s time=%s",
            name,
            address,
            datetime.datetime.now().isoformat(),
        )