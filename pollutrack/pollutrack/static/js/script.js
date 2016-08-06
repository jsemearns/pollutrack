var MAP;
var marker = {
    position: {lat: 10.3267959, lng: 123.9108368}
};
var Geocoder = new google.maps.Geocoder();

var templates = {
    pollutionDetail: $('#pollution-detail-template').html(),
    pollutionList: $('#pollution-list-template').html(),
}

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
        showPollutionInfo(this.pk)
    });
}

function addAllMarkers(sources) {
    for (var i = 0; i < sources.length; i++) {
        addMarker(sources[i]);
    }
}

function fetchPollutions() {
    var listContainer = $('.pollution-list');
    $.get('/pollution/list/', function(data) {
        var pollutions = JSON.parse(data);
        for (var i=0; i < pollutions.length; i++) {
            var loc = pollutions[i];
            addMarker({position: {lat: loc.lat, lng: loc.long},
                       pk: loc.pk});
            var t = Mustache.render(templates.pollutionList, loc)
            listContainer.append(t);
        }
    });
}

function showPollutionInfo(id) {
    $.get('/pollution/get/?pk=' + id, function(data) {
        var pollution = JSON.parse(data);
        var t = Mustache.render(templates.pollutionDetail, pollution);
        $('.show-detail').sideNav('hide');
        $('#detail-slide').html(t);
        $('.show-detail').sideNav('show');
    });
}

$('.show-detail').sideNav({
    menuWidth: 320,
    edge: 'left',
    closeOnClick: false,
});

$('.show-list').sideNav({
    menuWidth: 320,
    edge: 'left',
    closeOnClick: true,
});

$('.close-list').sideNav('hide');

$('.pollution-list').on('click', 'li.collection-item', function(e) {
    e.preventDefault();
    var elem = $(this);
    MAP.setCenter(new google.maps.LatLng(elem.data('lat'), elem.data('long')));
    showPollutionInfo(elem.data('pk'));
});

function getUserPosition() {
    var startPos;
    var geoSuccess = function(position) {
        startPos = position;
        return { 'lng': startPos.coords.longitude, 'lat': startPos.coords.latitude }
    };
    var geoError = function(error) {
        console.log('Error occurred. Error code: ' + error.code);
        // error.code can be:
        //   0: unknown error
        //   1: permission denied
        //   2: position unavailable (error response from location provider)
        //   3: timed out
        return false;
    };
    return navigator.geolocation.getCurrentPosition(geoSuccess, geoError);
}

function getCoordinates(address) {
  geocoder.geocode({'address': address}, function(results, status) {
      if (status === 'OK') {
          return results[0].geometry.location;
        } else {
          alert('Geocode was not successful for the following reason: ' + status);
        }
      });
}
