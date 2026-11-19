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
        user = self.get_jwt_user(request)
        if user is not None:
            self.set_current_user_info_and_log(user['user'])
            return True
        return False


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
        prefixes = ('/api', '/login')
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
        if not isinstance(headers, dict):
            return None
        auth = headers.get('Authorization')
        if not isinstance(auth, dict):
            return None
        user = auth.get('user')
        token = auth.get('jwt')
        if not isinstance(user, dict) or not token:
            return None
        name = user.get('name')
        if not name:
            return None
        expected = str(name) + str(datetime.date.today())
        if token != expected:
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
        if isinstance(user, dict):
            name = user.get('name')
            address = user.get('address')
        else:
            name = user
            address = None
        logging.getLogger(__name__).info(
            "access by user=%s address=%s at %s",
            name, address, datetime.datetime.now().isoformat()
        )