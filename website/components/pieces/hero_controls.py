from flask import Markup

def component():
    return Markup(f"""
    <div class="controls_ctnr">
        <p id="controls_ctnr_message">
            press <button> ENTER </button> to the control camera 
        </p>
        <div class="controls">

            <div class="control_set">

                <div class="control_button">
                    <p id='q' class="control">
                        Q
                    </p>
                    <small>
                        up
                    </small>
                </div>

                <div class="control_button">
                    <p id='e' class="control">
                        E
                    </p>
                    <small>
                        down
                    </small>
                </div>
            </div>

            <div class="control_set">
                <div class="control_button">
                    <p id='w' class="control">
                        W
                    </p>
                    <small>
                        forward
                    </small>
                </div>
            </div>

            <div class="control_set">
                
                <div class="control_button">
                    <p id='a' class="control">
                        A
                    </p>
                    <small>
                        left 
                    </small> 
                </div>
                

                <div class="control_button">
                    <p id='s' class="control">
                        S
                    </p>
                    <small>
                        backward
                    </small>
                </div>

                <div class="control_button">
                    <p id='d' class="control">
                        D
                    </p>
                    <small>
                        right
                    </small>
                </div>
            </div>

        </div>
    </div>
    
    
    """)