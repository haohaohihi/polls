from django.http import HttpResponse
import logging

logger = logging.getLogger("polls")


def index(request):
    logger.info("hello")
    return HttpResponse("Hello, world. You're at the polls index.")