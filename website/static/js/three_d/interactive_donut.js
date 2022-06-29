var donut_ctnr = document.querySelector('#donut_ctnr')

if (donut_ctnr){

    

    var donut_scene = new THREE.Scene();
    var donut_camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth/window.innerHeight,
        0.1,
        1000
    )

    donut_camera.position.z = 30

    var donut_renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    donut_renderer.setClearColor(new THREE.Color('#fff'))
    donut_renderer.setSize(window.innerWidth, window.innerHeight)

    donut_ctnr.appendChild(donut_renderer.domElement)

    const donut_hemi_light = new THREE.HemisphereLight (0xFFFFFF, 1, 2)
    donut_scene.add(donut_hemi_light)
    

    const particles_geomtery = new THREE.BufferGeometry;
    const particles_count = 10000/2;

    const position_array = new Float32Array(particles_count * 3)

    for (let i = 0; i < particles_count * 3; i++){
        position_array[i] = (Math.random() - 0.5) * 70
    }

    particles_geomtery.setAttribute('position', new THREE.BufferAttribute(position_array, 3))

    const particle_material = new THREE.PointsMaterial({
        // size: 0.010,
        size: 0.005,
        color: 'white',
    })
    const particles_mesh = new THREE.Points(particles_geomtery, particle_material)
    
    donut_scene.add(particles_mesh)






    var donut_render = function(){
        requestAnimationFrame(donut_render)

        // donut_renderer.domElement.id = 'donut_canvas'
        donut_renderer.render(donut_scene, donut_camera)
    }

    donut_render();
}
