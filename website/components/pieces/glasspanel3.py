from flask import Markup
from random import choice
from website.utils.webdata import unpack_elems
from datetime import datetime, timedelta

def component():
    posts_data = {
        'post1' : {
            'title' : "How Adam and Eve Cooked Eggs in the Iron Age",
            'blurb' : "Commodo sint cupidatat commodo et minim amet non ipsum irure ut pariatur adipisicing non. Qui esse dolor reprehenderit adipisicing sint minim sint. Non commodo do reprehenderit laborum est veniam excepteur incididunt sit ad ullamco laborum Lorem et. Laborum reprehenderit amet culpa duis aute in magna esse voluptate velit quis anim. Minim sit sint dolore sit ipsum commodo duis velit anim Lorem.",
            'posted' : (datetime.now() - timedelta(days=3, hours=5, minutes=5)).strftime("%b %d, %Y | %I:%M %p"),
            'tags' : ['history', 'funny', 'top post']
        }, 
        'post2' : {
            'title' : "Between the Queen and I",
            'blurb' : "Commodo sint cupidatat commodo et minim amet non ipsum irure ut pariatur adipisicing non. Qui esse dolor reprehenderit adipisicing sint minim sint. Non commodo do reprehenderit laborum est veniam excepteur incididunt sit ad ullamco laborum Lorem et. Laborum reprehenderit amet culpa duis aute in magna esse voluptate velit quis anim. Minim sit sint dolore sit ipsum commodo duis velit anim Lorem.",
            'posted' : (datetime.now() - timedelta(days=7, hours=2, minutes=17)).strftime("%b %d, %Y | %I:%M %p"),
            'tags' : ['art', 'sad', 'trending']
        }, 
        'post3' : {
            'title' : "The Twins Miquella and Malenia",
            'blurb' : "Commodo sint cupidatat commodo et minim amet non ipsum irure ut pariatur adipisicing non. Qui esse dolor reprehenderit adipisicing sint minim sint. Non commodo do reprehenderit laborum est veniam excepteur incididunt sit ad ullamco laborum Lorem et. Laborum reprehenderit amet culpa duis aute in magna esse voluptate velit quis anim. Minim sit sint dolore sit ipsum commodo duis velit anim Lorem.",
            'posted' : (datetime.now() - timedelta(days=10, hours=8, minutes=25)).strftime("%b %d, %Y | %I:%M %p"),
            'tags' : ['history', 'funny', 'top post']
        }, 
    }

    def make_post(post_dict):
        return Markup(f""" 
        <div>
            <div class="post">
                <h4>
                    {post_dict.get('title')}
                </h4>
                <p class="posted">
                    {post_dict.get('posted')}
                </p>
                <div class="tags_ctnr">
                    <p>
                        #{post_dict.get('tags')[0]}
                    </p>
                    <p>
                        #{post_dict.get('tags')[1]}
                    </p>
                    <p>
                        #{post_dict.get('tags')[2]}
                    </p>
                </div>
                <p class="blurb">
                    {post_dict.get('blurb')}
                </p>
            </div>
        </div>

        """)

    return Markup(f"""
    <div class="panel glass panel3">
        <h2>
            Structured Information
        </h2>
        <p>
            Works wonderfully at formatting lots of content. Everything is separated and sections are plainly labeled. The typography varies to help draw distinction between different bits of information. The gradient background is simple, beautiful, but not too distracting.
        </p>
        <div class="postlist_ctnr">
            {make_post(posts_data.get('post1'))}
            <hr>
            {make_post(posts_data.get('post2'))}
            <hr>
            {make_post(posts_data.get('post3'))}
        </div>
    </div>
    """)