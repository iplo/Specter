// base.js

// Jquery Window Onload
$(document).ready(function(){
	var parts = window.location.search.substr(1).split("&");
	var $_GET = {};
	for (var i = 0; i < parts.length; i++) {
	    var temp = parts[i].split("=");
    	$_GET[decodeURIComponent(temp[0])] = decodeURIComponent(temp[1]);
	}

	document.title = $_GET['appname'];
});