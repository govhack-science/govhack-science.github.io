function location_map(locations) {
  $(document).ready(function() {
    var map = L.map('gh-location-map', {minZoom: 4, maxBounds: new L.LatLngBounds([-1,100], [-60, 190]) }).setView([-28.42, 147.129], 3);
    var mapIcons = {
        official: L.icon({ iconUrl: '/resources/images/leaflet/redpin.png', iconSize: [32, 37] }),
        node: L.icon({ iconUrl: '/resources/images/leaflet/bluepin.png', iconSize: [32, 37] }),        
        'maker-node': L.icon({ iconUrl: '/resources/images/leaflet/bluepin.png', iconSize: [32, 37] }),
        'theme-node': L.icon({ iconUrl: '/resources/images/leaflet/bluepin.png', iconSize: [32, 37] }),
        'youth-node': L.icon({ iconUrl: '/resources/images/leaflet/bluepin.png', iconSize: [32, 37] })
    };
    L.tileLayer('https://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
            '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'maxious.gdb67hbh'
    }).addTo(map);
    
    var markers = [];
    for(var i = 0; i < locations.length; i++) {
        markers.push(
            L.marker(locations[i], {
                icon: mapIcons['official'] || mapIcons.node
            }).addTo(map)
        );
    }
    
    var group = new L.featureGroup(markers);
    map.fitBounds(group.getBounds()).zoomOut(2);
  });
};