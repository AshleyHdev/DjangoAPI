from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔐 JWT 路由
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 🧠 加入你自己的 API 路由
    path('api/', include('events.urls')),
    path('api/', include('users.urls')),

    # 📄 drf-spectacular schema 路由
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # ✅ 使用官方 Swagger UI CDN
    path(
        'api/docs/',
        TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'schema'}
        ),
        name='swagger-ui'
    ),

    # ✅ 使用 Redoc（不會出錯）
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]
