var rain_scape_section = document.querySelector('#rain_scape_ctnr')

if (rain_scape_section){
    var rain_scene = new THREE.Scene();
    var rain_camera = new THREE.PerspectiveCamera(
        60,
        window.innerWidth/window.innerHeight,
        1,
        1000
    )
    
    rain_camera.position.z = 1;
    rain_camera.rotation.x = 1.16;
    rain_camera.rotation.y = -0.12;
    rain_camera.rotation.z =  0.27;


    var rain_renderer = new THREE.WebGLRenderer({
        antialias: true
    })

    rain_renderer.setSize(window.innerWidth, window.innerHeight)
    rain_scape_section.appendChild(rain_renderer.domElement)

    window.addEventListener('resize', ()=> {
        rain_renderer.setSize(window.innerWidth, window.innerHeight);
        rain_camera.aspect  = window.innerWidth / window.innerHeight;
        rain_camera.updateProjectionMatrix()
    })

    const ambient = new THREE.AmbientLight(0x555555);
    rain_scene.add(ambient);

    const directionalLight = new THREE.DirectionalLight(0xffeedd)
    directionalLight.position.set(0,0,1)
    rain_scene.add(directionalLight)


    const smoke_texture_link = rain_scape_section.dataset.smoke_texture
    const rain_loader = new THREE.TextureLoader();

    var cloudParticles = [];
    const smoke_texture = rain_loader.load(smoke_texture_link, function(texture){
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
            rain_scene.add(cloud);
        }
    })

    var flash = new THREE.PointLight(0x062d89, 30, 500, 1.7)
    flash.position.set (200, 300, 100);
    rain_scene.add(flash)

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
    rain_scene.add(rain_mesh)

    var rain_render = function (){
        requestAnimationFrame(rain_render)

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

        if (rain_mesh.position.y > -10){
            rain_mesh.position.y -= .3;
        } else {
            rain_mesh.position.y = 0;
        }


        rain_renderer.domElement.id = 'rain_canvas'
        rain_renderer.render(rain_scene, rain_camera)
    }
    rain_render();
}