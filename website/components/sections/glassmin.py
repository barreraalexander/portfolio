from flask import Markup, url_for

def component():
    return Markup(f"""
    <section id="glassmin_section">
        <div class="glass_panel">
            <div class="glass_ctnr">
            </div>
            <p>
                this is text
            </p>
        <div>
    </section>
    <script src="{url_for('static', filename='js/animations/glassmin.js')}">
    </script>
    """)