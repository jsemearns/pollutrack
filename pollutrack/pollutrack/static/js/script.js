function initMap() {
    var mapDiv = document.getElementById('map');
    var map = new google.maps.Map(mapDiv, {
        center: {lat: 10.3267959, lng: 123.9108368},
        zoom: 15
    });
}
