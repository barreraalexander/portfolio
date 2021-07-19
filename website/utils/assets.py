from flask_assets import Bundle

bundles = {
    'main_scss':Bundle(
        'scss/main.scss',
        filters='libsass',
        depends=['scss/*.scss', 'scss/pages/*.scss', 'scss/components/*.scss'],
        output='gen/css/main.%(version)s.css'
    ),
    'main_js': Bundle(
        'js/main_js/mod_theme.js',
        'js/main_js/mod_menu.js',
        filters='jsmin',
        depends='js/*.js',
        output='gen/js/main.%(version)s.js'
    ),
    'index_js': Bundle(
        'js/index_js/technologies_mod.js',
        'js/index_js/scrolling_mod.js',
        'js/index_js/planets_mod.js',
        'js/index_js/projects_mod.js',
        'js/index_js/digital_mod.js',
        'js/index_js/shifting_h1.js',
        'js/index_js/day_mod.js',
        filters='jsmin',
        depends='js/*.js',
        output='gen/js/index.%(version)s.js'
    ),
}

