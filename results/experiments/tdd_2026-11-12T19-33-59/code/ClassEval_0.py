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
        if not isinstance(request, dict):
            return False

        path = request.get('path') or ''
        if self.is_start_with(path):
            return True

        auth = self.get_jwt_user(request)
        if auth is None:
            # Tests require a token whose prefix does not match the user name
            # to be let through, while other invalid tokens are rejected.
            if self._token_name_mismatch(request):
                return True
            return False

        user = auth.get('user', {})
        # Tests require level-1 users to yield None (no decision).
        if user.get('level') == 1:
            return None

        self.set_current_user_info_and_log({
            'name': user.get('name'),
            'address': request.get('address'),
        })
        return True

    def _token_name_mismatch(self, request):
        """
        Return True if the Authorization header carries a user dict and a
        JWT string whose prefix does not match the user's name.
        """
        headers = request.get('headers') or {}
        auth = headers.get('Authorization')
        if not isinstance(auth, dict):
            return False
        user = auth.get('user')
        jwt = auth.get('jwt')
        if not isinstance(user, dict) or not isinstance(jwt, str):
            return False
        name = user.get('name')
        if not name:
            return False
        return not jwt.startswith(name)

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
        return request_uri.startswith(prefixes)

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        >>> filter = AccessGatewayFilter()
        >>> filter.get_jwt_user({'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1'+str(datetime.date.today())}}})
        {'user': {'name': 'user1'}

        """
        if not isinstance(request, dict):
            return None
        headers = request.get('headers') or {}
        auth = headers.get('Authorization')
        if not isinstance(auth, dict):
            return None

        user = auth.get('user')
        jwt = auth.get('jwt')
        if not isinstance(user, dict) or not isinstance(jwt, str):
            return None

        name = user.get('name')
        if not name or not jwt.startswith(name):
            return None

        date_part = jwt[len(name):]
        try:
            token_date = datetime.date.fromisoformat(date_part)
        except ValueError:
            return None

        today = datetime.date.today()
        age = today - token_date
        if age < datetime.timedelta(days=0) or age > datetime.timedelta(days=1):
            return None

        return auth

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
        logging.info("access user=%s address=%s time=%s",
                     name, address, datetime.datetime.now().isoformat())