from flask import Markup, url_for

def component():
    three_d_script = url_for('static', filename='js/three_d/interactive_donut.js')
    
    return Markup(f"""
    <section id="interactive_donut_section">
        <h1>
            Interactive 3d Objects
        </h1>
        <div class="interactive_panel">
            <div id="donut_ctnr">
            </div>
            <div id="controls_ctnr">
                <div class="movement_controls">
                    <div id="backward" class="control">
                        <p>
                            ⬆
                        </p>
                    </div>
                    <div id="forward" class="control">
                        <p>
                            ⬇
                        </p>
                    </div>
                    <div id="left" class="control">
                        <p>
                            ⬅
                        </p>
                    </div>
                    <div id="right" class="control">
                        <p>
                            ➡
                        </p>
                    </div>
                </div>

                <div class="transformer_controls">
                    
                    <div id="change_mesh" class="changer" >
                    </div>

                    <div id="change_color"  class="changer">
                    </div>

                </div>

            </div>

        </div>
    </section>

    <script
        src="{three_d_script}">
    </script>

    """)