let glassmin_section = document.querySelector('#glassmin_section')

let glass_panels = glassmin_section.querySelectorAll(".panel")

const glassmin_observer_options = {
    root: null,
    threshold: .1
}

const glassmin_observer = new IntersectionObserver(function(entries, glassmin_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            entry.target.style.opacity = 1
            entry.target.style.transform = 'translate(0, -1em)'
            
        } else {
            entry.target.style.opacity = 0
            entry.target.style.transform = 'translate(0, 0em)'
        }
    })
}, glassmin_observer_options)


for (let panel of glass_panels){
    glassmin_observer.observe(panel)
}