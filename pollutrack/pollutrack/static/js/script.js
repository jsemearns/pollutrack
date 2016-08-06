var MAP;
var marker = {
    position: {lat: 10.3267959, lng: 123.9108368}
};

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
