from flask_assets import Bundle

bundles = {
    'main_scss':Bundle(
        'scss/main.scss',
        filters='libsass',
        depends='scss/*.scss',
        output='gen/css/main.%(version)s.css'
    )
}

