from flask import Markup, url_for


def component(title, elem_id=""):
    text = ""
    domain = ""
    img_src1 =f"https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/{title}1.png"
    img_src2 = f"https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/{title}2.png"
    img_src3 = f"https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/{title}3.png"
    img_src4 = f"https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/{title}4.png"


    def unpack_divs():
        divs = ["<div></div>" for i in range(20)]
        divs = "".join(divs)
        return divs

    if (title=="food"):
        title_formatted="The Food}"
        text="This is the text about the project. the project that I love so very much and you, are not hungry until the hour."
        domain = "www.thefood.com"
        img_src1 = url_for('static', filename=f'images/portfolio_screenshots/{title}1.png')
        img_src2 = url_for('static', filename=f'images/portfolio_screenshots/{title}2.png')
        img_src3 = url_for('static', filename=f'images/portfolio_screenshots/{title}3.png')

    elif (title=="tod"):
        title_formatted="Technicians on Demand"
        text="This is the text about the project. the project that I love so very much and you, are not hungry until the hour."
        domain = "www.technicianondemand.com"
        img_src1 = url_for('static', filename=f'images/portfolio_screenshots/{title}1.png')
        img_src2 = url_for('static', filename=f'images/portfolio_screenshots/{title}2.png')
        img_src3 = url_for('static', filename=f'images/portfolio_screenshots/{title}3.png')
        img_src4 = url_for('static', filename=f'images/portfolio_screenshots/{title}4.png')
    
    elif (title=="browardreseller"):
        title_formatted="Broward Reseller"
        text="This is the text about the project. the project that I love so very much and you, are not hungry until the hour."
        domain = "www.browardreseller.com"
        img_src1 = url_for('static', filename=f'images/portfolio_screenshots/{title}1.png')
        img_src2 = url_for('static', filename=f'images/portfolio_screenshots/{title}2.png')
        img_src3 = url_for('static', filename=f'images/portfolio_screenshots/{title}3.png')
    

    elif (title=="ppb"):
        title_formatted="Privacy Playbook"
        text="This is the text about the project. the project that I love so very much and you, are not hungry until the hour."
        domain = "www.privacyplaybook.com"
        img_src1 = url_for('static', filename=f'images/portfolio_screenshots/{title}1.png')
        img_src2 = url_for('static', filename=f'images/portfolio_screenshots/{title}2.png')
        img_src3 = url_for('static', filename=f'images/portfolio_screenshots/{title}3.png')
        img_src4 = url_for('static', filename=f'images/portfolio_screenshots/{title}4.png')


    
    return Markup(f"""
            <div id="{elem_id}" class="project">
                <p>
                    <strong>
                        {title_formatted}
                    </strong>
                    <br>
                    <a src='{domain}'> {domain} </a>
                    <br>
                    {text}
                </p>
                <div class="img_ctnr">
                    <img
                        src="{img_src1}"
                        alt="{title} image"
                        data-src_1="{img_src1}"
                        data-src_2="{img_src2}"
                        data-src_3="{img_src3}"
                        loading-lazy
                    >
                    
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