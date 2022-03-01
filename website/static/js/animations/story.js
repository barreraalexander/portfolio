const story_section = document.querySelector('#story_section')
const me_img = story_section.querySelector('img')
const horizonal_line = story_section.querySelector('hr')

const story_observer_options = {
    root: null,
    threshold: .4,
}

const story_observer = new IntersectionObserver(function(entries, mission_observer){
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
    }
), 0


story_tl.to(
    horizonal_line,
    {
        duration: 2,
        width: '6em',
        ease: Sine.easeInOut,

    }
), 0

// if (story_section){

//     // alert('here')    

// }


// // need observer and timeline
// alert('here')
