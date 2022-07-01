from flask import Markup, url_for

def component():
    three_d_script = url_for('static', filename='js/three_d/interactive_donut.js')

    ship_model = url_for('static', filename='images/assets/three_d/ship.glb')
    planet_model = url_for('static', filename='images/assets/three_d/planet.glb')
    stork_model = url_for('static', filename='images/assets/three_d/stork.glb')

    return Markup(f"""
    <section id="interactive_donut_section">
        <h1>
            Interactive 3d Objects
        </h1>
        <div class="interactive_panel">
            <div id="donut_ctnr"
                data-model1="{planet_model}"
                data-model2="{ship_model}"
                data-model3="{stork_model}">
            </div>
            <div id="controls_ctnr">
                <div class='zoom_controls'>
                    <div id="zoom_in" class="control">
                        <p>
                            +
                        </p>
                    </div>
                    <div id="zoom_out" class="control">
                        <p>
                            -
                        </p>
                    </div>
                </div>
                <div class="movement_controls">

                    <div id="forward" class="control">
                        <p>
                            ⬆
                        </p>
                    </div>
                    <div id="backward" class="control">
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