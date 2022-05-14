from flask import Markup

def component(inner_text):
    return Markup(f"""
    <div class="dramatic_h1_ctnr">
        <h1>
            {inner_text}
        </h1>
        <hr>
    </div>
    
    """)