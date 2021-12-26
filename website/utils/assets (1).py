from flask_assets import Bundle

bundles = {
    'dark_scss':Bundle(
        'scss/theme_dark/main.scss',
        filters='libsass',
        depends=['scss/theme_dark/*.scss'],
        output='gen/css/main.%(version)s.css'
    ),
    'light_scss':Bundle(
        'scss/theme_light/main.scss',
        filters='libsass',
        depends=['scss/theme_light/*.scss'],
        output='gen/css/main.%(version)s.css'
    ),
    'main_js': Bundle(
        'js/main_js/technologies_mod.js',
        'js/main_js/scrolling_mod.js',
        'js/main_js/planets_mod.js',
        'js/main_js/projects_mod.js',
        'js/main_js/digital_mod.js',
        'js/theme2_js/mod_theme.js',
        filters='jsmin',
        depends='js/*.js',
        output='gen/js/main.%(version)s.js'
    ),
    'theme2': Bundle(
        'js/theme2_js/mod_theme.js',
        'js/theme2_js/shifting_h1.js',
        filters='jsmin',
        depends='js/theme2/*.js',
        output='gen/js/theme2.%(version)s.js'
    )
}

