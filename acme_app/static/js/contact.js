/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
} 


// function google map
function myMap() {
  var mapCanvas = document.getElementById("map");
  var myCenter = new google.maps.LatLng(26.8030768,75.7933116);
  var mapOptions = {center: myCenter, zoom: 11};
  var map = new google.maps.Map(mapCanvas,mapOptions);
  var marker = new google.maps.Marker({
    position: myCenter,
    animation: google.maps.Animation.BOUNCE
  });
  
  var infowindow = new google.maps.InfoWindow({
    content: "Acme Services"
  });
  infowindow.open(map,marker);
  marker.setMap(map);
  
  google.maps.event.addListener(marker,'click',function() {
    var pos = map.getZoom();
    map.setZoom(13);
    map.setCenter(marker.getPosition());
    
  });
}

