REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES': (
        'Main.apis.renderer.DefaultRenderer',
    ),
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}