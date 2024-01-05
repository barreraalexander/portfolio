from flask_assets import Bundle

bundles = {
    'main_scss':Bundle(
        'scss/main.scss',
        filters='libsass',
        depends=[
            'scss/*.scss',
            'scss/base/*.scss',
            'scss/pages/*.scss',
            'scss/components/navbars/*.scss',
            'scss/components/pieces/*.scss',
            'scss/components/sections/*.scss',
        ],
        output='gen/css/main.%(version)s.css'
    ),
    'animations_js':Bundle(
        'js/animations/contact_modal.js',
        'js/animations/dramatic_h1.js',
        'js/animations/experience.js',
        'js/animations/glassmin.js',
        'js/animations/hero.js',
        'js/animations/hidden.js',
        'js/animations/minimalism.js',
        'js/animations/neubrutalism.js',
        'js/animations/resume_like.js',
        'js/animations/shifting_dots.js',
        'js/animations/skill_card.js',
        'js/animations/story.js',
        filters='jsmin',
        depends=[
            'js/animations/*.js',
        ],
        output='gen/js/animations.%(version)s.js'
    ),
    'three_d_js':Bundle(
        # 'js/three_d/interactive_donut.js',
        'js/three_d/planets_mod.js',
        # 'js/three_d/rain_scape.js',
        filters='jsmin',
        depends=[
            'js/three_d/*.js',
        ],
        output='gen/js/three_d.%(version)s.js'
    ),
}

