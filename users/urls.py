from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentsViewSet

router = SimpleRouter()
router.register("", PaymentsViewSet)

app_name = UsersConfig.name

urlpatterns = []

urlpatterns += router.urls