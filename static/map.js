var map = L.map('map').setView([40.712, -74.006], 11);
var layer = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
});


var newMarkerOrigin
var newMarkerDestination
var nbrClick = 0;
var marker = [];


map.on('click', 
  function(e){
  if (nbrClick%2==0) {
    var markerRed = L.icon({iconUrl:'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png', 
                            markerColor:'red', 
                            prefix: 'fa', 
                            icon:'school'})
    var newMarkerOrigin = L.marker(e.latlng,{icon:markerRed} ,{draggable:'true'}).addTo(map)
    marker['origin'] = []
    marker['origin'].push(newMarkerOrigin._latlng)
    console.log(newMarkerOrigin, 'origin')
  } else if(nbrClick>2) {
    // Get reckt le temps de trouver une solution
    document.location.reload()
  }
   else {
    
    var markerRed = L.icon({iconUrl:'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png', 
                            markerColor:'red', 
                            prefix: 'fa', 
                            icon:'school'})
    var newMarkerDestination = L.marker(e.latlng, {icon:markerRed}, {draggable:'true'}).addTo(map)
    marker['destination'] = []
    marker['destination'].push(newMarkerDestination._latlng) 
    console.log(newMarkerDestination, 'destination')
    const url = '/get_post_json';
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState == XMLHttpRequest.DONE) {
        console.log(xhr,'im xhr')
          result = xhr.response;
          result = result.split(',');
          console.log(result,'coucou');
      }
  }
    xhr.open('POST','/get_post_json',true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    data  = JSON.stringify([marker['destination'],marker['origin']])
    console.log(data,'data')
    xhr.send(data)

  }
  nbrClick ++;
});
// Now add the layer onto the map
map.addLayer(layer);
