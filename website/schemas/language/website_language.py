from pydantic import BaseModel, constr
from datetime import datetime, timedelta
from typing import List

class websiteLanguage(BaseModel):
    variant: int = 2


class contactAttribute(BaseModel):
    text: str

class contactLanguage(BaseModel):
    phone: contactAttribute = contactAttribute(text='+19548828507')
    email: contactAttribute = contactAttribute(text='barreraalexander93@gmail.com')
    

class metaAttribute(BaseModel):
    text: constr(strip_whitespace=True)


class metaLanguage(BaseModel):
    description: metaAttribute = metaAttribute(text=
        """
        Barrera Portfolio is a website used to
        showcase the web development experience
        of Alexander Barrera. He is a freelancing
        fullstack web developer from south Florida.        
        """
    )
    keywords: metaAttribute = metaAttribute(text=
        """
        fullstack engineer, web developer, programmer, web freelancer, web developer south florida, python engineer, database manager, coder, python flask, API manager, web designer 
        """
    )
    domain: metaAttribute = metaAttribute(text=
        "www.barrera-port.co"
    )
    domain_name: metaAttribute = metaAttribute(text=
        "Barrera Portfolio"
    )
    


class socialMediaAttribute(BaseModel):
    link: str

class socialMediaLinks(BaseModel):
    github: socialMediaAttribute = socialMediaAttribute(
        link='https://github.com/barreraalexander'
    )
    linkedin: socialMediaAttribute = socialMediaAttribute(
        link='https://www.linkedin.com/in/abarrera-tech/'
    )
    
    upwork: socialMediaAttribute = socialMediaAttribute(
        link='https://www.upwork.com/freelancers/~0120837e444852e684'
    )



class demoPost(BaseModel):
    title: str
    blurb: str = "Commodo sint cupidatat commodo et minim amet non ipsum irure ut pariatur adipisicing non. Qui esse dolor reprehenderit adipisicing sint minim sint. Non commodo do reprehenderit laborum est veniam excepteur incididunt sit ad ullamco laborum Lorem et. Laborum reprehenderit amet culpa duis aute in magna esse voluptate velit quis anim. Minim sit sint dolore sit ipsum commodo duis velit anim Lorem."

    posted: datetime
    tags: List[str]

    @property
    def posted_as_str(self) -> str:
        return self.posted.strftime("%b %d, %Y | %I:%M %p")


class demoPosts(BaseModel):
    demo_posts : List[demoPost] = [
        demoPost(
            title='How Adam and Eve Cooked Eggs in the Iron Age',
            posted=datetime.utcnow() - timedelta(days=3, hours=5, minutes=5),
            tags=[
                'history',
                'funny',
                'top post',
            ],
        ),
    
        demoPost(
            title='Between the Queen and I',
            posted=datetime.utcnow() - timedelta(days=7, hours=2, minutes=17),
            tags=[
                'art',
                'sad',
                'trending',
            ],
        ),

        demoPost(
            title='How to Make Components in Python Flask',
            posted=datetime.utcnow() - timedelta(days=10, hours=8, minutes=25),
            tags=[
                'technology',
                'informative',
                'top post'
            ],
        ),
    ]
