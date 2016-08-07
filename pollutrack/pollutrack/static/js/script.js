var MAP;
var Geocoder;
var marker = {
    position: {lat: 10.3267959, lng: 123.9108368}
};

var userLocation = null;
var Geocoder = null;

var templates = {
    pollutionDetail: $('#pollution-detail-template').html(),
    pollutionList: $('#pollution-list-template').html(),
    createForm: $('#create-pollution').html(),
    imagesCarousel: $('#pollution-images-template').html(),
};

function initMap() {
    var mapDiv = document.getElementById('map');
    MAP = new google.maps.Map(mapDiv, {
        center: {lat: 10.3267959, lng: 123.9108368},
        disableDefaultUI: true,
        zoom: 12,
    });
    Geocoder = new google.maps.Geocoder();
    fetchPollutions();
}

function addMarker(source) {
    source.map = MAP;
    var marker = new google.maps.Marker(source);
    marker.addListener('click', function() {
        showPollutionInfo(this.pk);
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
            var t = Mustache.render(templates.pollutionList, loc);
            listContainer.append(t);
        }
    });
}

function showPollutionInfo(id) {
    $.get('/pollution/get/?pk=' + id, function(data) {
        var pollution = JSON.parse(data);
        var t = Mustache.render(templates.pollutionDetail, pollution);
        var rendered = Mustache.render(templates.imagesCarousel, pollution);
        $('#images-modal-list').html(rendered);
        $('.show-detail').sideNav('hide');
        $('#detail-slide').html(t);
        $('.show-detail').sideNav('show');
    });
}

function createPollution(position) {
    var imageIds = [];
    $('#create-pollution').html(templates.createForm);
    var mainForm = $('#pollution-form');
    mainForm.find('input[name="long"]').val(position.lng)
    mainForm.find('input[name="lat"]').val(position.lat)
    mainForm.find('input[name="address"]').val(position.address);
    $('#create-pollution').openModal();
    $('#create-pollution input[name="image_file"]').on('change', function(e) {
        var form = $(this).closest('form');
        var formData = new FormData(form[0]);
        formData.append('file', this.files[0]);
        $.ajax({
            url: form.attr('action'),  //server script to process data
            type: 'POST',
            success: function(data) {
                var data = JSON.parse(data);
                imageIds.push(data.pk);
                $('#create-pollution .uploaded-images').append(
                    '<img src="' + data.url + '">')
                mainForm.find('input[name="image_pks"]').val(imageIds);
            },
            error: function(xhr) {
                alert("Something went wrong!");
            },
            // Form data
            data: formData,
            processData: false,
            contentType: false,
        });
    });

    mainForm.on('submit', function(e) {
        e.preventDefault();
        $.ajax({
           type: "POST",
           url: this.action,
           data: $(this).serialize(), // serializes the form's elements.
           success: function(data) {
                $('#create-pollution').closeModal();
                Materialize.toast(
                    'We received your report and currently verifying it. Thank you!', 4000)
           }
         });
    });

    $('#create-pollution .submit').on('click', function(e) {
        mainForm.trigger('submit');
    });
}

$('.show-detail').sideNav({
    menuWidth: 320,
    edge: 'left',
    closeOnClick: true,
});

$('.close-detail').sideNav('hide');

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

$('.add-button').on('click', function(e) {
    e.preventDefault();
    getUserPosition(function(loc) {
        getCoordinates(
            {lng: loc.coords.longitude, lat: loc.coords.latitude},
            createPollution);
    }, function(e) {
        Materialize.toast('Sorry, we cannot get your current location. :(',
            4000);
    });
    // createPollution();
});

function getUserPosition(success, error) {
    return navigator.geolocation.getCurrentPosition(success, error);
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).on('click', '.approve-btn', function(e) {
    e.preventDefault();
    var elem = $(this);
    $.ajax({
        beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        type: 'POST',
        url: elem.data('url'),
        data: {'pk': elem.data('id')},
        success: function(response) {
            response = JSON.parse(response);
            if (response.update) {
                $('#approve-count').text(response.count.toString().concat(' people verified this.'));
            }
            elem.addClass('hidden');
        },
        error: function(xhr, type) {
            console.log('an unexpected error occured while approving');
        }
    });
});

function getCoordinates(location, callback) {
    Geocoder.geocode({'location': location}, function(results, status) {
      if (status === 'OK') {
            location.address = results[1].formatted_address;
            return callback(location);
        } else {
            Materialize.toast('Sorry, the geocoder failed. :(', 4000)
        }
    });
}

// FOR THE IMAGES MODAL-CAROUSEL
$('#detail-slide').on('click', '.detail-image', function() {
    $('#images-modal').openModal();
    $('.materialboxed').materialbox();
});
