from rest_framework.throttling import UserRateThrottle

class MyRateThrottling(UserRateThrottle):
    scope = 'my'