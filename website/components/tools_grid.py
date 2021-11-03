from flask import Markup

def component():
    tools = [
        "photoshop"
    ]
    def grid_item(tool):
        return f"""
        <div class="tool">
            <img
                src=""
                alt="tool logo"
            >
            <p> Tool Name </p>
        </div>
        """


    return Markup(f"""
    <section id="keytable">
        <ul>
            <li>
                <div class="circle" data-type="learning">
                </div>
                <p>
                    Learning
                </p>
            </li>
            <li>
                <div class="circle" data-type="mastered">
                </div>
                <p>
                    Mastered
                </p>
            </li>
            <li>
                <div class="circle" data-type="covet">
                </div>
                <p>
                    Covet
                </p>
            </li>
        </ul>
    </section>
    <section id="tools_grid">
        <div class="col learning_ctnr">
            {grid_item('photoshop')}
            {grid_item('photoshop')}
        </div>
        <div class="col mastered_ctnr">
            {grid_item('photoshop')}
            {grid_item('photoshop')}
            {grid_item('photoshop')}
            {grid_item('photoshop')}
        </div>
        <div class="col covet_ctnr">
            {grid_item('photoshop')}
            {grid_item('photoshop')}
        </div>
    </section>
    """)