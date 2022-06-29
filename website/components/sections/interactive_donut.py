from flask import Markup, url_for

def component():
    three_d_script = url_for('static', filename='js/three_d/interactive_donut.js')

    return Markup(f"""
    <section id="interactive_donut_section">
        <div class="interactive_panel">
            <div id="donut_ctnr">
            </div>
            <div id="controls_ctnr">
            
            </div>

        </div>
    </section>

    <script
        src="{three_d_script}">
    </script>

    """)