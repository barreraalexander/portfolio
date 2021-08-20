var night_ctnr = document.querySelector('#night_ctnr')
if (night_ctnr){
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth/window.innerHeight,
        0.1,
        1000
        )
    camera.position.z = 8


    var renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    renderer.setClearColor(new THREE.Color('#111'))

    renderer.setSize(window.innerWidth, window.innerHeight)

    document.body.querySelector('#night_ctnr').appendChild(renderer.domElement)
    window.addEventListener('resize', ()=> {
        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix()
    })


    const geometry = new THREE.SphereBufferGeometry(1.5, 20, 20);
    const material = new THREE.MeshStandardMaterial();
    
    const moon_texture_link = night_ctnr.dataset.moon_texture
    const space_bg_link = night_ctnr.dataset.space_bg
    const loader = new THREE.TextureLoader();
    const moon_texture = loader.load(moon_texture_link)    


    material.normalMap = moon_texture
    material.color = new THREE.Color('#c8c8c8')

    const mesh1 = new THREE.Mesh(geometry, material)
    mesh1.position.set(4, 8, -10)
    scene.add(mesh1)

    var light1 = new THREE.PointLight(0xFFFFFF, 1, 1000)
    light1.position.set(0, 0, 0);
    scene.add(light1)

    //star   system
    const particles_geomtery = new THREE.BufferGeometry;
    const particles_count = 10000/3;

    const position_array = new Float32Array(particles_count * 3)

    for (let i = 0; i < particles_count * 3; i++){
        position_array[i] = (Math.random() - 0.5) * 40
    }

    particles_geomtery.setAttribute('position', new THREE.BufferAttribute(position_array, 3))

    const particle_material = new THREE.PointsMaterial({
        size: 0.010,
        color: 'white',
    })


    const particles_mesh = new THREE.Points(particles_geomtery, particle_material)
    scene.add(particles_mesh)


    //star cluster
    document.addEventListener('mousemove', animateParticles)


    let mouse_x = 0
    let mouse_y = 0

    function animateParticles(event){
        mouse_y = event.clientY
        mouse_x = event.clientX
    }

    const clock = new THREE.Clock()
    var render = function (){
        requestAnimationFrame(render)

        let elasped_time = clock.getElapsedTime()   
        mesh1.rotation.y += 0.0008;

        particles_mesh.rotation.y = (.0009 * elasped_time)
        particles_mesh.rotation.x = (.0009 * -mouse_y)
        particles_mesh.rotation.x = (.0009 * -mouse_x)

        renderer.domElement.id = 'globe_canvas';
        renderer.render(scene, camera)

    }
    render();
}