from ..models import Cosplayer
from ..forms import CosplayerForm
from .generic_posting_view import make_posting_view


shoottikala_cosplayer_view = make_posting_view(
    Cosplayer,
    CosplayerForm,
    create_posting_title='Hae photoshoottia cossaajana',
    edit_posting_title='Muokkaa cossaajailmoitustasi',
    read_only_title='Cossaajailmoitus',
    footer_message=(
        'Nämä tiedot näkyvät cossaajia etsiville valokuvaajille. '
        'Voit muokata näitä tietoja myöhemmin.'
    )
)
