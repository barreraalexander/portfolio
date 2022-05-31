from flask import Markup

def component():
    return Markup(f"""
    <div class="panel glass panel2">
        <h2>
            Nonessential Information
        </h2>
        <p>
            This section is often pushed off to the right on desktop, and at the bottom of the stack on mobile, or hidden completely. This would often include the archive section of a news website or blog. On social media sites, the nonessential section would store advertisements, suggested friends and groups.
        </p>
        <ul>
            <li>
                March 2022
            </li>
            <li>
                February 2022
            </li>
            <li>
                January 2022
            </li>
            <li>
                December 2021
            </li>
            <li>
                November 2021
            </li>
            <li>
                October 2021
            </li>
            <li>
                September 2021
            </li>
            <li>
                August 2021
            </li>
            <li>
                July 2021
            </li>
        </ul>
    </div>
    
    """)