// alert('here')

let experience_section = document.querySelector('#experience_section')

if (experience_section){
    const count_wait = (ms) => new Promise(resolve => setTimeout(resolve, ms))
    
    const loop = async () => {
        let experience_divs = experience_section.querySelectorAll('.experience')
        for (let elem of experience_divs) {
            let max_count = elem.dataset.max_count
            let elem_number = elem.querySelector('h3')
            for (let i = 0; i < max_count; i++){
                elem_number.innerHTML = i;
                await count_wait(10)
            }
        }
    }

    
    const experience_canvas = experience_section.querySelector('#skills_chart').getContext("2d")



    const labels = [
        "database management",
        "ui/ux design",
        "frontend",
        "backend",
        "python"
    ]

    const data = {
        labels,
        datasets:[{
            data: [100, 60, 80, 90, 50],
            label: 'Proficiencies',
            backgroundColor: [
                '#f7ff47',
                '#55ff47',
                '#47b4ff',
                '#ca47ff',
                '#ff4763',
            ],
            borderRadius: 10
        }],

    }


    const config = {
        type: 'bar',
        data: data,
        options : {
            animation: {
                tension: {
                    duration: 30000,
                    easing: 'linear',
                    loop: 'true'
                }
            },
            responsive: true,
            scales: {
                y: {
                    ticks: {
                        color: "#fff",
                        callback: function(value){
                            return value + '%'
                        }
                    }
                },
                x: {
                    ticks: {
                        color: "#fff",
                    }
                }
            },
            plugins : {
                legend: {
                    labels : {
                        color: '#fff'
                    },
                }
            }
        },
    };


    const experience_observer_options = {
        root: null,
        threshold: .5,
    }


    const experience_section_observer = new IntersectionObserver(function(entries, experience_section_observer){
        entries.forEach(entry => {
            if (entry.isIntersecting){
                loop()
                var skill_chart = new Chart(experience_canvas, config)                
            } else {
                let experience_h3 = experience_section.querySelectorAll('.experience h3')
                for (let elem of experience_h3){
                    elem.innerHTML = 0
                }                
            }
        })
    }, experience_observer_options)
    
    experience_section_observer.observe(experience_section)





    // const skill_chart = new Chart(experience_canvas, config)

    // skill_chart.defaults.color = "#fff"

    // console.log(experience_canvas)    


}



// loop()



