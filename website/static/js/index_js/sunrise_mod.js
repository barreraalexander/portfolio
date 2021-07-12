var day_ctnr = document.querySelector('#day_ctnr')
if (day_ctnr){
    var day_scene = new THREE.Scene();
    var day_camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth/window.innerHeight,
        0.1,
        1000
        )
        
    day_camera.position.z = 5


    var day_renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    day_renderer.setClearColor(new THREE.Color('#94fcff'))


    day_renderer.setSize(window.innerWidth, window.innerHeight)

    document.body.querySelector('#day_ctnr').appendChild(day_renderer.domElement)
    window.addEventListener('resize', ()=> {
        day_renderer.setSize(window.innerWidth, window.innerHeight);
        day_camera.aspect = window.innerWidth / window.innerHeight;
        day_camera.updateProjectionMatrix()
    })




    var sun_geometry = new THREE.SphereBufferGeometry(1, 20, 20);
    var sun_material = new THREE.MeshLambertMaterial({color: 0xffdf22});
    var sun_mesh = new THREE.Mesh(sun_geometry, sun_material)

    var sun_light = new THREE.AmbientLight(0xffdf22, 1, 1000);
    sun_light.position.set( 1, 0, 1)
    day_scene.add(sun_light)

    var sun_light2 = new THREE.AmbientLight(0xFFD580, 1, 1000);
    sun_light2.position.set( 2, 2, .8)
    day_scene.add(sun_light2)


    var horizon = new THREE.PointLight(0x000000, 1, 10000);
    horizon.position.set( 1, 0, 2)
    day_scene.add(horizon)



    sun_mesh.position.y = 1;
    sun_mesh.position.x = 1;
    sun_mesh.position.z = .5;
    day_scene.add(sun_mesh)

    var day_light = new THREE.PointLight(0xFFFFFF, 1, 1000)
    day_light.position.set(1, 1, 0);
    day_scene.add(day_light)


    var day_light2 = new THREE.PointLight(0xFFFFFF, 1, 1000)
    day_light2.position.set(-1, -1  , 5); 
    day_scene.add(day_light2)



    
    const day_clock = new THREE.Clock()
    var day_render = function (){


        requestAnimationFrame(day_render)

        let elasped_time = day_clock.getElapsedTime()   
        sun_mesh.rotation.y += 0.01;

        // particles_mesh.rotation.y = (.0009 * elasped_time)
        // particles_mesh.rotation.x = (.0009 * -mouse_y)
        // particles_mesh.rotation.x = (.0009 * -mouse_x)

        day_renderer.domElement.id = 'globe_canvas';
        day_renderer.setClearColor(new THREE.Color('#94fcff'))
        day_renderer.render(day_scene, day_camera)

        //window.requestAnimationFrame()
    }
    day_render();


}