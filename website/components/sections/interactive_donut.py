from flask import Markup, url_for

def component():
    three_d_script = url_for('static', filename='js/three_d/interactive_donut.js')
    # texture1 = url_for('static', filename='images/assets/three_d/texture5.jpg')
    texture1 = url_for('static', filename='images/assets/three_d/sprinkle_texture.png')
    # texture1 = url_for('static', filename='images/assets/three_d/bubble_texture.png')


    moon_model = url_for('static', filename='images/assets/three_d/moon.glb')
    ship_model = url_for('static', filename='images/assets/three_d/ship.glb')
    planet_model = url_for('static', filename='images/assets/three_d/planet.glb')



    return Markup(f"""
    <section id="interactive_donut_section">
        <h1>
            Interactive 3d Objects
        </h1>
        <div class="interactive_panel">
            <div id="donut_ctnr" data-texture1="{texture1}" data-model1="{planet_model}" data-model2="{ship_model}">
            </div>
            <div id="controls_ctnr">
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