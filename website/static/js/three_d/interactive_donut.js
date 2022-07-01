var donut_section = document.querySelector('#interactive_donut_section')
var donut_ctnr = document.querySelector('#donut_ctnr')

if (donut_ctnr){
    var donut_scene = new THREE.Scene();
    var donut_camera = new THREE.PerspectiveCamera(
        75,
        donut_ctnr.offsetWidth/donut_ctnr.offsetHeight,
        0.1,
        1000
    )
    donut_camera.position.z = 10

    var donut_renderer = new THREE.WebGLRenderer({
        antialias: true
    })


    donut_renderer.setSize(donut_ctnr.offsetWidth, donut_ctnr.offsetHeight)

    donut_ctnr.appendChild(donut_renderer.domElement)

    const donut_hemi_light = new THREE.HemisphereLight (new THREE.Color('#fff'), 1, 2)
    donut_scene.add(donut_hemi_light)

    const particles_geomtery = new THREE.BufferGeometry;
    const particles_count = 10000/8;
    const position_array = new Float32Array(particles_count * 3)

    for (let i = 0; i < particles_count * 3; i++){
        position_array[i] = (Math.random() - 0.5) * 70
    }

    particles_geomtery.setAttribute('position', new THREE.BufferAttribute(position_array, 3))

    const particle_material = new THREE.PointsMaterial({
        // size: 0.010,
        size: 0.0001,
        color: 'white',
    })
    const particles_mesh = new THREE.Points(particles_geomtery, particle_material)
    donut_scene.add(particles_mesh)



    const camera_light = new THREE.PointLight( new THREE.Color('#fff'), 100, 0 );
    donut_scene.add( camera_light );


    window.addEventListener('resize', ()=>{
        donut_renderer.setSize(donut_ctnr.offsetWidth, donut_ctnr.offsetHeight);
        donut_camera.aspect = donut_ctnr.offsetWidth / donut_ctnr.offsetHeight;
        donut_camera.updateProjectionMatrix()

    })


    let arrow_controls = donut_section.querySelectorAll('.control')
    for (let control of arrow_controls){
        control.addEventListener('click', handleMovement, false)
    }


    let changer_controls = donut_section.querySelectorAll('.changer')
    for (let control of changer_controls){
        control.addEventListener('click', handleChanger, false)
    }

    function handleMovement(event){
        let direction = event.target.id
        
        var max_z = 30
        var min_z = -12

        if (direction=='zoom_in'){
            donut_camera.position.z -= .5
            
        }        

        if (direction=='zoom_out'){
            if (donut_camera.position.z < max_z){
                donut_camera.position.z += .5
            } 
            return
        }        


        if (direction=='forward'){
            donut_camera.position.y += 1
            return     
        }
        
        if (direction=='backward'){
            donut_camera.position.y -= 1
            return     
        }
        
        if (direction=='left'){
            donut_camera.position.x -= 1       
            return     
        }
        
        if (direction=='right'){
            donut_camera.position.x += 1       
            return     
        }
    }

    var color_selector = 0
    var mesh_selector = true
    function handleChanger(event){
        let command = event.target.id
        if (command=="change_mesh"){
            if (mesh_selector){
                donut_ctnr.style.mixBlendMode = 'color-burn'
                mesh_selector = false
                return
            }
            donut_ctnr.style.mixBlendMode = ''
            mesh_selector = true
            return
        }
        if (command=="change_color"){
            let colors = ['f7dc6f', 'ff0000', '00c9ff', 'b200ff', 'd8ff00', '00ffc1']
            donut_hemi_light.color = new THREE.Color(`#${colors[color_selector]}`)
            color_selector += 1
            if (color_selector==5){
                color_selector = 0
            }

            return
        }
    }


    function load_moon(){
        const moon_link = donut_ctnr.dataset.model1
        const moon_loader = new THREE.GLTFLoader();
        moon_loader.load(
            moon_link,
            function ( gltf ) {
                moon = gltf.scene;
                // moon.wireframe = true
                moon.position.set(0, 0, 6);
                donut_scene.add( moon );
            },
        )
    }
    load_moon()


    function load_ship(){
        const ship_link = donut_ctnr.dataset.model2
        const ship_loader = new THREE.GLTFLoader();
        ship_loader.load(
            ship_link,
            function ( gltf ) {
                ship = gltf.scene;
                ship.scale.set(.25, .25, .25)
                ship.position.set(1, 4, 1)
                donut_scene.add( ship );
            },
        )
    }
    load_ship()


    function load_stork(){
        const stork_link = donut_ctnr.dataset.model3
        const stork_loader = new THREE.GLTFLoader();
        stork_loader.load(
            stork_link,
            function ( gltf ) {
                stork = gltf.scene;
                stork.scale.set(.25, .25, .25)
                stork.position.set(-8, 8, -30)
                donut_scene.add( stork );
            },
        )
    }
    load_stork()



    var donut_render = function(){
        requestAnimationFrame(donut_render)

        camera_light.position.set(donut_camera.position)

        try {
            if (moon){
                moon.rotation.x += .002;
                moon.rotation.y += .005;
            }
            if (ship){
                ship.rotation.y += .002
            }
            if (stork){
                stork.rotation.z -= .001
                stork.rotation.x -= .00001

            }
        } catch (error) {
            
        }

        donut_renderer.render(donut_scene, donut_camera)
    }

    donut_render();
}
