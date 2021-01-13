const map = L.map('map').setView([40.712, -74.006], 15);
var layer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
});


var newMarkerOrigin
var newMarkerDestination
var nbrClick = 0;
var marker = [];


map.on('click', 
  function(e){
  if (nbrClick%2==0) {

    var newMarkerOrigin = L.marker(e.latlng,{draggable:'true'}).addTo(map)
    marker['origin'] = []
    marker['origin'].push(newMarkerOrigin._latlng)
    console.log(newMarkerOrigin, 'origin')
  } else if(nbrClick>2) {
    // Get reckt le temps de trouver une solution
    document.location.reload()
  }
   else {
    var newMarkerDestination = L.marker(e.latlng,{draggable:'true'}).addTo(map)
    marker['destination'] = []
    marker['destination'].push(newMarkerDestination._latlng) 
    console.log(newMarkerDestination, 'destination')
    const url = '/get_post_json';
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState == XMLHttpRequest.DONE) {
        console.log(xhr,'im xhr')
          response = xhr.response;
          
          response = JSON.parse(response)
          
          long = response.long.split(',');
          lat = response.lat.split(',');
          console.log(long,lat)

          result = []
          for ( var i = 0; i < long.length; i++ ){
            result.push( [lat[i],long[i] ] );
          }
          printWay(result)
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


function printWay(result){

  console.log(result,'any array in here ?')
  const path = L.polyline(result, {
    "delay": 400,
    "weight": 5,
    "color": "#ff00ff",
    "paused": false,
    "reverse": false,
    "hardwareAccelerated": true,
    "smoothFactor":0.1
  });

  L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  
  map.addLayer(path);
  map.fitBounds(path.getBounds())
}