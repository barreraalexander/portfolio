from flask import Markup, url_for


def component(title):
    text = ""

    def unpack_divs():
        divs = ["<div></div>" for i in range(20)]
        divs = "".join(divs)
        return divs

    if (title=="food"):
        title="The Food"
        text="This is the text about the project. the project that I love so very much and you, are not hungry until the hour."
    
    elif (title=="tod"):
        title="Technician on Demand"
        text="This is the text about the project. the project that I love so very much and you, are not hungry until the hour."
    
    

    
    return Markup(f"""
            <div class="project">
                <p>
                    <strong>
                        {title}
                    </strong>
                    <br>
                    {text}
                </p>
                <div class="img_ctnr">
                    <img src="https://source.unsplash.com/random/600x600" loading-lazy alt="broward reseller">
                    <div class="shifting_grill_ctnr">
                        <div class="horizontal_bars">
                            {unpack_divs()}
                        </div>
                        <div class="vertical_bars">
                            {unpack_divs()}
                        </div>
                    </div>
                </div>
            </div>
    """)