from django.urls import path, include

urlpatterns =[
        path('area_plaza/', include('apps.catalogos.area_plaza.urls')),
        path('cargo/', include('apps.catalogos.cargo.urls')),
        path('departamentos/', include('apps.catalogos.departamentos.urls')),
        path('empresa/', include('apps.catalogos.empresa.urls')),
        path('municipio/', include('apps.catalogos.municipio.urls')),
        path('profesion/', include('apps.catalogos.profesion.urls')),
        path('tipo_empresa/', include('apps.catalogos.tipo_empresa.urls')),
        path('postulantes/', include('apps.catalogos.postulante.urls')),
        path('habilidades/', include('apps.catalogos.habilidades.urls')),
        path('plaza/', include('apps.catalogos.plaza.urls')),
]