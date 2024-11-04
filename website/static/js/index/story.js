const story_section = document.querySelector('#story_section')
const me_img = story_section.querySelector('.me_picture')
// const horizonal_line = story_section.querySelector('hr')

const story_observer_options = {
    root: null,
    threshold: .1,
}

const story_observer = new IntersectionObserver(function(entries, story_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            story_tl.play()
        } else {
            story_tl.reverse()
        }
    })
}, story_observer_options);


story_observer.observe(story_section)


const story_tl = gsap.timeline({
    paused: true,
})

story_tl.to(
    story_section,
    {
        filter: 'grayscale(0%)',
        ease: Sine.easeInOut,
        duration: 2,
    }
), 0


story_tl.to(
    me_img,
    {
        duration: 2,
        filter: 'blur(0px)',
        ease: Sine.easeInOut,
    }
), 0
