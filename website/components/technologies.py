from flask import Markup, url_for

def component():

    def tech_img_ctnr(technology):
        selected = "selected_img"
        img_src = url_for('static', filename=f'images/assets/{technology}.svg')
        return Markup(f"""
            <div
                id="{technology}"
                class="tech_img_ctnr"
            >
                <img
                    src="{img_src}"
                    alt="{technology}"
                >
            </div>        
        """)

    TECHNOLOGIES = [
        'python', 'html5', 'css',
        'javascript', 'mysql', 'photoshop',
        'xd','github', 'windows'
    ]

    def unpack():
        divs = [tech_img_ctnr(elem) \
                for elem in TECHNOLOGIES]
        return " ".join(divs)

    return Markup(f"""
        <div class="technologies_ctnr">
            {unpack()}
        </div>
    """)