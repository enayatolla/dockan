from django.core.cache.backends.redis import RedisCache


CACHES = {
   "default": {
      "BACKEND": "django.core.cache.backends.redis.RedisCache",
      "LOCATION": "redis://redis:6379/0",
   }
}




