from pydantic import BaseModel, constr
from typing import Optional

class comment(BaseModel):
    elem_id: Optional[str] = ""
    # comment: constr(strip_whitespace=True)
    comment:str
    origin: str
    origin_url: str
    author_name: str

class comments(BaseModel):
    app_generator: comment = comment(
        author_name = 'Adrian',
        comment = """
            Alexander knows very well FastAPI and his work is always focused on quality.
            For sure I will work with Alexander in the future on other Python-related tasks.
            Besides his skills, Alexander has a positive and optimistic approach during the entire task.
        """,
        origin = 'www.app-generator.dev', 
        origin_url = 'https://app-generator.dev/', 
    )

    privacy_playbook: comment = comment(
        author_name = 'Russell Owens',
        comment = """
            I hired Alexander for a small HTML/CSS job.
            His code was well structured and the site looks good.
            He proactively identified issues and either fixed them
            or asked for guidance. He worked effectively with
            github branches, PRs and issue management. He
            was easy to work with and had a positive attitude.
        """,
        origin = 'www.privacyplaybook.com', 
        origin_url = 'https://privacyplaybook.com/', 
    )

    tech_on_demand: comment = comment(
        author_name = 'Adrian Milian',
        comment = """
            He designed, created and launched my website.
            Alexander was a huge help, super friendly and easy
            to work with. I'll turn to him again if I need anything
            for the web.
        """,
        origin = 'www.technicianondemand.com', 
        origin_url = 'https://www.technicianondemand.com/', 
    )

    upwork1: comment = comment(
        author_name = 'Jessica Baldwin',
        comment = """
            Alexander communicated exceptionally
            well and he worked on the task we provided
            expeditiously!
        """,
        origin = 'www.letsbmedia.com', 
        origin_url = 'https://letsbmedia.com/', 
    )

    upwork2: comment = comment(
        author_name = 'Port Vendre',
        comment = """
            Alexander was great to work with.
            Stayed on time, completed work exactly as asked,
            and provided quality coding. We would definitely
            recommend him and hope to work with him again!
        """,
        origin = 'upwork', 
        origin_url = 'https://www.upwork.com/', 
    )
    upwork3: comment = comment(
        author_name = 'Preston Gordon',
        comment = """
        Alexander was great. He completed the
        job promptly and was a pleasure to work with. This
        job really helped me and my business. Thank you.
        """,
        origin = 'www.usindustrial.com',
        origin_url = 'https://www.usindustrial.com/',
    )
    upwork4: comment = comment(
        author_name = 'Ronda Brunson',
        comment = """
        "Thanks for your service. A++"
        """,
        origin = 'www.promostandards.org',
        origin_url = 'https://promostandards.org/',
    )
