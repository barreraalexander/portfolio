var donut_section = document.querySelector('#interactive_donut_section')
var donut_ctnr = document.querySelector('#donut_ctnr')

if (donut_ctnr){
    let texture_path = donut_ctnr.dataset.texture1
    const donut_textureLoader = new THREE.TextureLoader()
    const bubbleTexture = donut_textureLoader.load(texture_path)




    var donut_scene = new THREE.Scene();
    var donut_camera = new THREE.PerspectiveCamera(
        75,
        // window.innerWidth/window.innerHeight,
        donut_ctnr.offsetWidth/donut_ctnr.offsetHeight,
        // donut_ctnr.innerWidth,
        0.1,
        1000
    )
    donut_camera.position.z = 10

    var donut_renderer = new THREE.WebGLRenderer({
        antialias: true
    })


    donut_renderer.setSize(donut_ctnr.offsetWidth, donut_ctnr.offsetHeight)

    donut_ctnr.appendChild(donut_renderer.domElement)

    const donut_hemi_light = new THREE.HemisphereLight (0xFFFFFF, 1, 2)
    donut_scene.add(donut_hemi_light)

    // const donut_geo = new THREE.TorusGeometry(10, 1, 100, 200);
    const donut_geo = new THREE.TorusGeometry(10, 3, 16, 100);
    const sphere_geo = new THREE.SphereBufferGeometry(5, 64, 64);
    
    const donut_mat = new THREE.MeshStandardMaterial({
        color: new THREE.Color('#DEB887'),
        // wireframe: true,
    });

    const sphere_mat = new THREE.MeshNormalMaterial({
        // color: new THREE.Color('#DEB887'),
        // wireframe: true,
    });


    donut_mat.normalMap = bubbleTexture;
    sphere_mat.normalMap = bubbleTexture;
    // donut_mat.metalness = 0.1
    // donut_mat.roughtness = 0.3


    const donut_mesh = new THREE.Mesh(donut_geo, donut_mat)
    const sphere_mesh = new THREE.Mesh(sphere_geo, sphere_mat)


    donut_mesh.position.set(0, 0, -30)
    sphere_mesh.position.set(0, 0, -60)



    // console.log(texture_path)




    // donut_scene.add(donut_mesh);
    // donut_scene.add(sphere_mesh);

    

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
        // var max_z = 0

        


        if (direction=='forward'){
            donut_camera.position.z -= 1
            return     
        }
        
        if (direction=='backward'){
            if (donut_camera.position.z < max_z){
                donut_camera.position.z += 1
            } 
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
    function handleChanger(event){
        let command = event.target.id
        if (command=="change_mesh"){
            // alert('mesh')
            // donut_mesh.
            donut_mesh.material.color.setHex( 0xffffff )
            
            return
        }
        if (command=="change_color"){
            // alert('color')
            
            donut_mesh.material.color.setHex( 0xffffff )


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



    var donut_render = function(){
        requestAnimationFrame(donut_render)


        sphere_mesh.rotation.x += .002;
        sphere_mesh.rotation.y += .008;
        
        
        try {
            if (moon){
                moon.rotation.x += .002;
                moon.rotation.y += .005;
            }
            if (ship){
                ship.rotation.y += .002
            }
        } catch (error) {
            
        }

        donut_renderer.render(donut_scene, donut_camera)
    }

    donut_render();
}
