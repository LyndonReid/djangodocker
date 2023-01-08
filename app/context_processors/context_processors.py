import datetime

from offers.models import Offer

# For _footer_bottom.html template file
def current_year_context_processor(request):
    current_datetime = datetime.datetime.now()
    return {
        'current_year': current_datetime.year
    }


def allmakes_context_processor(request):
    allmakes = Offer.objects.order_by('carmake').distinct("carmake")
    return {
        'allmakes': allmakes
    }
    