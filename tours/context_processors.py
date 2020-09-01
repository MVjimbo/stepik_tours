from data import title, subtitle, description, departures


def base(request):
    link = {"link": request.path}
    kwargs = {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "departures": departures,
        "link": link
    }
    return kwargs
