from pydantic import BaseModel
from flask import url_for



class websiteLanguage(BaseModel):
    variant: int = 2


class contactAttribute(BaseModel):
    pass

class contactLanguage(BaseModel):
    variant: int = 2



class metaAttribute(BaseModel):
    text: str


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
    
