from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .modifier import Modifier
from .suggestion import generate


@require_GET
def index(request):
    length = 16
    maximum = 128
    minimum = 8

    context = {
        "digits": True,
        "length": length,
        "lowercase": True,
        "maximum": maximum,
        "minimum": minimum,
        "suggestion": generate(length),
        "punctuation": False,
        "uppercase": True,
    }

    return render(request, "index.html", context)


@require_POST
def new(request):
    try:
        data = request.POST

        digits = Modifier.DIGITS if "digits" in data else Modifier(0)
        length = int(data["length"])
        lowercase = Modifier.LOWERCASE if "lowercase" in data else Modifier(0)
        punctuation = Modifier.PUNCTUATION if "punctuation" in data else Modifier(0)
        uppercase = Modifier.UPPERCASE if "uppercase" in data else Modifier(0)

        suggestion = generate(length, digits | lowercase | punctuation | uppercase)

        return JsonResponse({"suggestion": suggestion})
    except (KeyError, ValueError) as error:
        return HttpResponseBadRequest(error)
