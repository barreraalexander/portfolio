from pydantic import BaseModel
# from flask import url_for

class skill(BaseModel):
    title: str
    blurb: str
    img_static_location: str
    variant: int

class skills(BaseModel):
    web_dev: skill = skill(
        title = 'From Design to Build',
        blurb = 'If you want to provide the design, the difference between design and product will be nonexistent. I take pride in pixel perfect matching.',
        img_static_location = 'images/assets/icons/skills/web_dev.svg',
        variant = 1
    )

    db_management: skill = skill(
        title = 'Database Management',
        blurb = 'Certified db manager. Choose between mysql or postgres, generally hosted on AWS RDS.',
        img_static_location = 'images/assets/icons/skills/db_management.svg',
        variant = 2
    )

    api_dev: skill = skill(
        title = 'API Development',
        blurb = 'Professional level API development, complete with correct status codes, and infinite scalabilty. The ORM can be pydantic, or graphql.',
        img_static_location = 'images/assets/icons/skills/api_dev.svg',
        variant = 1
    )

    server: skill = skill(
        title = 'Elastic Cloud Server',
        blurb = 'Deployment on the server is so 2014. Take advantage of the seamless scalabaility of elastic servers that grow and shrink with your traffic.',
        img_static_location = 'images/assets/icons/skills/server.svg',
        variant = 2
    )