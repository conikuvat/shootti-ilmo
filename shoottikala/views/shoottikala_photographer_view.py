from ..models import Photographer
from ..forms import PhotographerForm
from .generic_posting_view import make_posting_view


shoottikala_photographer_view = make_posting_view(
    Photographer,
    PhotographerForm,
    create_posting_title='Hae photoshoottia valokuvaajana',
    edit_posting_title='Muokkaa valokuvaajailmoitustasi',
    read_only_title='Valokuvaajailmoitus',
    footer_message=(
        'Nämä tiedot näkyvät valokuvaajia etsiville cossaajille. '
        'Voit muokata näitä tietoja myöhemmin.'
    )
)
