import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

export function loadShip(ship, ship_link, scene){
    const ship_loader = new GLTFLoader();
    ship_loader.load(
        ship_link,
        function ( gltf ) {
            ship = gltf.scene;
            ship.scale.set(.5, .5, .5)
            ship.position.set(4, 4, 15)
            scene.add( ship );
        },
    )
}
