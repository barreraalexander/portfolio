from flask import Markup

def component(description, max_count):
    return Markup(f""" 
    <div class="experience" data-max_count="{max_count}">
        <h3>
            0
        </h3>
        <p>
            {description}
        </p>
    </div>
    """)