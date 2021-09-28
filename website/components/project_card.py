from flask import Markup, url_for

def component(title, elem_id=""):
    img_src1 =f"https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/{title}_1_v2.png"
    img_src2 = f"https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/{title}_2_v2.png"
    img_src3 = f"https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/{title}_3_v2.png"
    img_src4 = f"https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/{title}_4_v2.png"


    def unpack_divs():
        divs = ["<div></div>" for i in range(20)]
        divs = "".join(divs)
        return divs

    if (title=="food"):
        title_formatted="The Food"
        text = "This is text about the project. This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project."
        domain = "www.thefood.com"
        domain_name = "www.privacyplaybook.com"

    elif (title=="tod"):
        title_formatted="Technicians on Demand"
        domain = "https://www.technicianondemand.com/"
        domain_name = "www.technicianondemand.com"
        text = Markup(f"""
        <li>
            <p>
                Developed the front-end design using
                <strong> Adobe XD </strong>,
                and made changes based on the tastes of the customer.
                <strong> Features mobile-first responsive design. </strong>
            </p>
        </li>
        <li>
            <p>
                Coded the entire website using the <strong> python
                flask framework , s3 cloud storage </strong> to host
                the static files (images, videos, icons),
                and nginx on <strong> ubuntu to deploy </strong> the website.
            </p>
        </li>
        <li>
            <p>
                Secured the website with <strong>certbot</strong>  and basic <strong> nginx protocols </strong>.
            </p>
        </li>
        
        """)

    elif (title=="browardreseller"):
        title_formatted="Broward Reseller"
        text = "This is text about the project. This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project.This is text about the project."
        domain = "www.browardreseller.com"
        domain_name = "www.privacyplaybook.com"
    

    elif (title=="ppb"):
        title_formatted="Privacy Playbook"
        domain = "https://privacyplaybook.com/"
        domain_name = "www.privacyplaybook.com"
        text = Markup(f"""
        <li>
            <p>
                Built the front-end using vanilla <strong> html,css and js </strong>,
                based on the specifications of a designer.
            </p>
        </li>
        <li>
            <p>
                <strong> Worked closely with a back-end developer </strong>
                to code up some “glue” functions between
                the api and html components.
            </p>
        </li>
        <li>
            <p>
                Controlled different versions of the app using <strong>github</strong>
            </p>
        </li>
        
        """)

    else:
        pass

    
    return Markup(f"""
    <div id="{elem_id}" class="project_card">
        <h3>
            {title_formatted}
        </h3>
        <a
            href='{domain}'
            target='_blank'
        >
            {domain_name}
        </a>
        <div class="images_ctnr">
            <img
                src="{img_src1}"
                alt="{title} image"
                loading=lazy
            >
            <img
                src="{img_src2}"
                alt="{title} image"
                loading=lazy
            >
            <img
                src="{img_src3}"
                alt="{title} image"
                loading=lazy
            >
            <img
                src="{img_src4}"
                alt="{title} image"
                loading=lazy
            >
        </div>
        <ul>
            {text}
        </ul>
    </div>
""")