var MAP;
var marker = {
    position: {lat: 10.3267959, lng: 123.9108368}
};

function initMap() {
    var mapDiv = document.getElementById('map');
    MAP = new google.maps.Map(mapDiv, {
        center: {lat: 10.3267959, lng: 123.9108368},
        zoom: 10
    });

    addAllMarkers([marker]);
}

function addMarker(source) {
    var marker = new google.maps.Marker({
        position: source.position,
        map: MAP
    });
}

function addAllMarkers(sources) {
    for (var i = 0; i < sources.length; i++) {
        addMarker(sources[i]);
    }
}
