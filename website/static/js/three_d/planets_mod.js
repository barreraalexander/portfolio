var night_ctnr = document.querySelector('#night_ctnr')
if (night_ctnr){
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth/window.innerHeight,
        0.1,
        1000
        )
    camera.position.z = 30


    var renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    renderer.setClearColor(new THREE.Color('#111'))

    renderer.setSize(window.innerWidth, window.innerHeight)

    night_ctnr.appendChild(renderer.domElement)


    const hemi_light = new THREE.HemisphereLight( 0xFFFFFF, 10 );
    scene.add(hemi_light)


    const point_light = new THREE.PointLight(0xFFFFFF, 1, 2)
    point_light.position.set(-2, 7, -10);
    scene.add(point_light)

    //star system
    const particles_geomtery = new THREE.BufferGeometry;
    const particles_count = 10000/2;

    const position_array = new Float32Array(particles_count * 3)

    for (let i = 0; i < particles_count * 3; i++){
        position_array[i] = (Math.random() - 0.5) * 70
    }

    particles_geomtery.setAttribute('position', new THREE.BufferAttribute(position_array, 3))

    const particle_material = new THREE.PointsMaterial({
        size: 0.010,
        color: 'white',
    })
    const particles_mesh = new THREE.Points(particles_geomtery, particle_material)
    scene.add(particles_mesh)

    const moon_link = night_ctnr.dataset.moon_model

    const moon_loader = new THREE.GLTFLoader();

    moon_loader.load(
        moon_link,
        function ( gltf ) {

                moon = gltf.scene;

                moon.position.set(0, 4, -15)
                scene.add( moon );
        },
    )

    const ship_link = night_ctnr.dataset.ship_model

    const ship_loader = new THREE.GLTFLoader();

    ship_loader.load(
        ship_link,
        function ( gltf ) {

                ship = gltf.scene;
                ship.scale.set(.5, .5, .5)
                ship.position.set(4, 4, 15)
                scene.add( ship );
        },
    )

    const planet_link = night_ctnr.dataset.planet_model

    const planet_loader = new THREE.GLTFLoader();

    planet_loader.load(
        planet_link,
        function ( gltf ) {

                planet = gltf.scene;
                planet.scale.set(8, 8, 8)
                planet.position.set(4, 18, -20)
                scene.add( planet );
        },
    )

    document.addEventListener('mousemove', animateParticles)

    let mouse_x = 0
    let mouse_y = 0

    function animateParticles(event){
        mouse_y = event.clientY
        mouse_x = event.clientX
    }

    window.addEventListener('resize', ()=> {
        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix()

    })

    const clock = new THREE.Clock()
    var render = function (){
        requestAnimationFrame(render)

        let elasped_time = clock.getElapsedTime()
        

        moon.rotation.y += 0.003;

        planet.rotation.y += 0.002;
        planet.rotation.x += 0.001;
        
        ship.rotation.y -= 0.003;
        ship.rotation.x += 0.003;

        particles_mesh.rotation.y = (.05 * elasped_time)
        particles_mesh.rotation.x = (.0009 * -mouse_y)
        particles_mesh.rotation.x = (.0009 * -mouse_x)

        

        if (window.innerWidth > 1400){
            moon.position.z = 16
            point_light.position.z = 16
            planet.position.set(12, 30, -25)
        } else {
            moon.position.z = 5
            point_light.position.z = 5
            planet.position.set(4, 18, -20)

        }

        if (elasped_time > 1 && elasped_time < 40){
            ship.position.y += .01
            ship.position.x -= .01
            ship.position.z -= .01
            
        } else {
            ship.position.y -= .01
            ship.position.x += .01
            ship.position.z += .01
        }

        renderer.domElement.id = 'globe_canvas';
        renderer.render(scene, camera)

    }
    render();
}