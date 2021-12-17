var rain_scape_section = document.querySelector('#rain_scape_ctnr')

if (rain_scape_section){
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(
        60,
        window.innerWidth/window.innerHeight,
        1,
        1000
    )
    
    camera.position.z = 1;
    camera.rotation.x = 1.16;
    camera.rotation.y = -0.12;
    camera.rotation.z =  0.27;


    var renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    renderer.setSize(window.innerWidth, window.innerHeight)
    rain_scape_section.appendChild(renderer.domElement)

    window.addEventListener('resize', ()=> {
        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.aspect  = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix()
    })

    const ambient = new THREE.AmbientLight(0x555555);
    scene.add(ambient);

    const directionalLight = new THREE.DirectionalLight(0xffeedd)
    directionalLight.position.set(0,0,1)
    scene.add(directionalLight)


    const smoke_texture_link = rain_scape_section.dataset.smoke_texture
    const loader = new THREE.TextureLoader();

    var cloudParticles = [];
    const smoke_texture = loader.load(smoke_texture_link, function(texture){
        cloudGeo = new THREE.PlaneBufferGeometry(500,500);
        cloudMaterial = new THREE.MeshLambertMaterial({
            map: texture,
            transparent: true
        });

        for(let p=0; p<40; p++){
            let cloud = new THREE.Mesh(cloudGeo, cloudMaterial);
            cloud.position.set(
                Math.random()*800 -400,
                500,
                Math.random()*500 - 450
            );
            cloud.rotation.x  = 1.16;
            cloud.rotation.y = -0.12;
            cloud.rotation.z = Math.random()*360;
            cloud.material.opacity = 0.6;
            cloudParticles.push(cloud);
            scene.add(cloud);
        }
    })

    var flash = new THREE.PointLight(0x062d89, 30, 500, 1.7)
    flash.position.set (200, 300, 100);
    scene.add(flash)

    const rain_geometry = new THREE.BufferGeometry;

    const rain_count = 100000;
    const position_array = new Float32Array(rain_count * 3)


    for (let i=0; i < rain_count; i++){
        position_array[i] = (Math.random() - 0.5) * 100
    }

    rain_geometry.setAttribute('position', new THREE.BufferAttribute(position_array, 3))

    rain_material = new THREE.PointsMaterial({
        color : 0xaaaaaa,
        size : 0.00001,
        transparent : true
    })


    const rain_mesh = new THREE.Points(rain_geometry, rain_material)
    scene.add(rain_mesh)

    const clock = new THREE.Clock()
    var render = function (){
        requestAnimationFrame(render)

        let elapsed_time = clock.getElapsedTime()

        cloudParticles.forEach(p => {
            p.rotation.z -= 0.0005;
        });


        if(Math.random() > 0.8 || flash.power > 1000){
            if (flash.power < 100)
            flash.position.set(
                Math.random()*400,
                300 + Math.random() * 200,
                100
            );
            flash.power = 50 + Math.random() * 500;
        }


        rain_mesh.rotation.y += 0.00002;

        // console.log(rain_mesh.position.y)
        if (rain_mesh.position.y > -10){
            rain_mesh.position.y -= .3;
        } else {
            rain_mesh.position.y = 0;
        }


        renderer.domElement.id = 'rain_canvas'
        renderer.render(scene, camera)
    }
    render();
}