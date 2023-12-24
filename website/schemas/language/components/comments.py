from pydantic import BaseModel, constr
from typing import Optional

class comment(BaseModel):
    elem_id: Optional[str]
    comment: constr(strip_whitespace=True)
    origin: str
    origin_url: str
    author_name: str

class comments(BaseModel):
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
        origin = 'upwork', 
        origin_url = 'https://www.upwork.com/', 
    )

    upwork2: comment = comment(
        author_name = 'Russell Owens',
        comment = "I hired Alexander for a small HTML/CSS job. His code was well structured and the site looks good. He proactively identified issues and either fixed them or asked for guidance. He worked effectively with github branches, PRs and issue management. He was easy to work with and had a positive attitude.",
        origin = 'www.privacyplaybook.com', 
        origin_url = 'https://privacyplaybook.com/', 
    )

    upwork3: comment = comment(
        author_name = 'Russell Owens',
        comment = "I hired Alexander for a small HTML/CSS job. His code was well structured and the site looks good. He proactively identified issues and either fixed them or asked for guidance. He worked effectively with github branches, PRs and issue management. He was easy to work with and had a positive attitude.",
        origin = 'www.privacyplaybook.com', 
        origin_url = 'https://privacyplaybook.com/', 
    )