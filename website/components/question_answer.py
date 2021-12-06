from flask import Markup


def component(question):
    if question == 'bootstrap':
        q = "Do you use bootstrap?"
        a = """
            I used to, but I have found that
            mixing HTML structure and layout
            becomes a disaster in the long-term.
            At most, I use some bootstrap mixins,
            but for the most part, I write custom CSS.
            """

    elif question == 'react':
        q = "Do you use React? Vue?"
        a = """
            I use neither. The syntax is too messy.
            In general, frameworks that force you to
            mix languages (in this case, HTML and JS)
            is just too stuffy. I prefer the package-oriented
            structure of Flask and Django, where concerns
            tend to be separated.
            """
    elif question == 'flask':
        q = "What framework do you use to build your web apps?"
        a = """
            Flask flask flask. Python's packing structure,
            coupled with post-processors, makes for a squeaky
            clean and well organized code. And it's use of blueprints
            allows for a wonderful separation of concerns.
            """
    elif question == 'host':
        q = "EC2 or Linode?"
        a = """
            Pre-2020 I was all about linode. But ec2
            has epanded so much in the last couple
            of years that I've switched over my web apps
            to be hosted on ec2. The sort of modular-based
            separation of security, keys, instances saves
            a lot of time.
            """

    elif question == 'db':
        q = "EC2 or Linode?"
        a = """
            Pre-2020 I was all about linode. But ec2
            has epanded so much in the last couple
            of years that I've switched over my web apps
            to be hosted on ec2. The sort of modular-based
            separation of security, keys, instances saves
            a lot of time.
            """
    else:
        return Markup(f""" """)


    return Markup(f"""
    <div class="question_ctnr">
        <p>
            <strong>
                Q:
            </strong>
            {q}
        </p>
    </div>
    <div class="answer_ctnr">
        <p>
            <strong>
                A:
            </strong>
            {a}
        </p>
    </div>
    
    """)