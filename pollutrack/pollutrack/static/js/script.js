var MAP;
var marker = {
    position: {lat: 10.3267959, lng: 123.9108368}
};

function initMap() {
    var mapDiv = document.getElementById('map');
    MAP = new google.maps.Map(mapDiv, {
        center: {lat: 10.3267959, lng: 123.9108368},
        disableDefaultUI: true,
        zoom: 12,
    });

    fetchPollutions();
}

function addMarker(source) {
    source.map = MAP;
    var marker = new google.maps.Marker(source);
    marker.addListener('click', function() {
        console.log(this.pk)
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

function fetchPollutions() {
    $.get('/pollution/list/', function(data) {
        var pollutions = JSON.parse(data);
        for (var i=0; i < pollutions.length; i++) {
            var loc = pollutions[i];
            addMarker({position: {lat: loc.lat, lng: loc.long},
                       pk: loc.pk});
        }
    });
}

$('.show-detail').sideNav({
    menuWidth: 320,
    edge: 'left',
    closeOnClick: false,
});
