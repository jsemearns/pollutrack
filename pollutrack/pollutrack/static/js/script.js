var MAP;
var marker = {
    position: {lat: 10.3267959, lng: 123.9108368}
};

function initMap() {
    var mapDiv = document.getElementById('map');
    MAP = new google.maps.Map(mapDiv, {
        center: {lat: 10.3267959, lng: 123.9108368},
        disableDefaultUI: true,
        zoom: 10,
    });

    addAllMarkers([marker]);
}

function addMarker(source) {
    var marker = new google.maps.Marker({
        position: source.position,
        map: MAP
    });
    marker.addListener('click', function() {
        $('.show-detail').sideNav('hide');
        // render then callback show
        $('.show-detail').sideNav('show');
    });
}

function addAllMarkers(sources) {
    for (var i = 0; i < sources.length; i++) {
        addMarker(sources[i]);
    }
}

$('.show-detail').sideNav({
    menuWidth: 320,
    edge: 'left',
    closeOnClick: false,
});
