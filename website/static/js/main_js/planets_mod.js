var night_ctnr = document.querySelector('#night_ctnr')
if (night_ctnr){
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth/window.innerHeight,
        0.1,
        1000
        )
        
    camera.position.z = 5


    var renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    renderer.setClearColor(new THREE.Color('#111'))

    // renderer.setClearColor ("#111");

    renderer.setSize(window.innerWidth, window.innerHeight)

    document.body.querySelector('#night_ctnr').appendChild(renderer.domElement)
    window.addEventListener('resize', ()=> {
        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix()
    })


    var geometry = new THREE.SphereBufferGeometry(1, 20, 20);
    var material = new THREE.MeshLambertMaterial({color: 0xF1F1F1});
   
    const textureLoader = new THREE.TextureLoader()
    
    const normal_texture = textureLoader.load('../../images/textures/moon_texture.png')

    material.normalMap = normal_texture;
    material.roughness = 0.7

    var mesh1 = new THREE.Mesh(geometry, material)
    mesh1.position.y = 1;
    mesh1.position.x = 1;
    mesh1.position.z = .5;
    scene.add(mesh1)

    var geometry = new THREE.SphereBufferGeometry(8, 20, 20);
    var material = new THREE.MeshLambertMaterial({color: 0x111111});
    material.metalness = 1
    material.roughness = 1
    var mesh3 = new THREE.Mesh(geometry, material)
    mesh3.position.x = -10;
    mesh3.position.y = 5;
    mesh3.position.z = -20;
    mesh3.opacity = .3;

    // scene.add(mesh3)

    var light1 = new THREE.PointLight(0xFFFFFF, 1, 1000)
    light1.position.set(1, 1, 0);
    scene.add(light1)

    var light2 = new THREE.PointLight(0xFFFFFF, 1, 1000)
    light2.position.set(-1, -1  , 5); 
    scene.add(light2)


    //star   system
    const particles_geomtery = new THREE.BufferGeometry;
    const particles_count = 10000/2;

    const position_array = new Float32Array(particles_count * 3)

    for (let i = 0; i < particles_count * 3; i++){
        position_array[i] = (Math.random() - 0.5) * 8
    }

    particles_geomtery.setAttribute('position', new THREE.BufferAttribute(position_array, 3))

    const particle_material = new THREE.PointsMaterial({
        size: 0.005,
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
        mesh1.rotation.y += 0.01;

        particles_mesh.rotation.y = (.0009 * elasped_time)
        particles_mesh.rotation.x = (.0009 * -mouse_y)
        particles_mesh.rotation.x = (.0009 * -mouse_x)

        renderer.domElement.id = 'globe_canvas';
        // renderer.setClearColor(new THREE.Color('#111'))
        renderer.render(scene, camera)

        //window.requestAnimationFrame()
    }
    render();
}