# Python imports
import logging

# Django imports

# Application imports
# Base imports
from base.views import BaseListAPIView
from base.permissions import IsAdmin
from base.paginations import IndexPagination
from base.serializers import BaseUserSerializer

# Model imports
from users.models import User

# Serializers imports


logger = logging.getLogger(__name__)


class ListAllUserAPIView(BaseListAPIView):
    model = User
    serializer_class = BaseUserSerializer
    # permission_classes = (IsAdmin,)
    permission_classes = ()
    pagination_class = IndexPagination
    search_fields = (
        'first_name',
        'last_name',
        'phone',
        'email'
    )
    filter_fields = (
        'is_active',
        'role_id'
    )

