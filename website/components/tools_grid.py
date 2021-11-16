from flask import Markup, url_for
from website.blueprints.main import unpack_elems

def component():
    def grid_item(tool):
        tool_title = tool.replace("_", " ").capitalize()
        img_src = url_for('static', filename=f'images/assets/{tool}.svg')

        return f"""
        <div id="{tool}_tool" class="tool">
            <img
                src="{img_src}"
                alt="tool logo"
            >
            <p> {tool_title} </p>
        </div>
        """
    
    learning = [
        "react", "mongodb",
        "node", "vue",
        "graphene", "graphql"
    ]

    learning_grid_items = [
                        f"""
                        {grid_item(elem)}
                        """ for elem in learning
                        ]

    mastered = [
        "html5", "css",
        "github", "javascript",
        "mysql", "photoshop",
        "python", "flask",
        "windows", "xd"
    ]

    mastered_grid_items = [
                        f"""
                        {grid_item(elem)}
                        """ for elem in mastered
                        ]
    

    prospect = [
        "ruby_on_rails", "c_sharp",
        "pytorch", "rush"
    ]

    prospect_grid_items = [
                        f"""
                        {grid_item(elem)}
                        """ for elem in prospect]


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
                    Prospect
                </p>
            </li>
        </ul>
    </section>
    <section id="tools_grid">
        <div class="col learning_ctnr">
            {unpack_elems(learning_grid_items)}
        </div>
        <div class="col mastered_ctnr">
            {unpack_elems(mastered_grid_items)}
        </div>
        <div class="col covet_ctnr">
            {unpack_elems(prospect_grid_items)}
        </div>
    </section>
    """)