// Initialize and add the map
function initMap() {
    // The location of Uluru
    var dataJson = '{{data.locations|tojson|safe}}'
    console.log(dataJson)
    dataJson.replaceAll("\'", "\"")
    console.log(dataJson)
    var locations = Array.from(JSON.parse(dataJson))

    const london = { lat: 51.52574482485191, lng: -0.12634439219556462 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 2,
        center: london,
    });

    for (var i = 0; i < locations.length; i++) {
        console.log(locations[i].lat, locations[i].long)
        var new_pos = { lat: locations[i].lat, lng: locations[i].long }
        new google.maps.Marker({
            position: new_pos,
            map: map,
        });
    }

}

window.initMap = initMap;