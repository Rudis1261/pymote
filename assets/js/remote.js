// Lets make it easy to change the filename
var myScript = "index.html";

// Get the current ip address of the server
var currentAddress 	= document.URL;
//var currentAddress  = "http://192.168.1.5:8080/";
var ServerRoot 		= "http://192.168.1.";
var PortString 		= ":8080/";
var QuertString  	= "?alive=true";
var StartIp 		= 0;

console.log("[INFO] Current IP Address: " + currentAddress);
checkCurrentServer();

// This function will check if we are on the correct server or not
function checkCurrentServer()
{
	var URL = currentAddress + QuertString;
	console.log("[INFO] Check current server Url: " + URL);
	$.get(URL, function( data ) {

    	if (data == "1")
    	{
    		console.log("[INFO] IP Still the same, let's leave things alone");
    	}

	}).fail(function(){
		checkServer();
	});
}

// We want to be able to detect an IP Address change and move the server
function checkServer()
{
	console.log("[ERROR] IP Changed, finding server");
	StartIp 	= StartIp + 1;
	var URL 	= ServerRoot + StartIp + PortString + QuertString;
	var Server 	= ServerRoot + StartIp + PortString;

	// Let's see if this is the server?
	if (StartIp < 255)
	{
		$.get(URL).done(function( data ) {

	    	if (data = "1")
	    	{
	    		console.log("[INFO] Server Found: " + Server);
				window.location.replace(Server);
	    	}

		}).fail(function(){

			checkServer();
		});
	}
}

// When the key is pressed, set it in the DB by running the AJAX
$(".remoteKeys").click(function(event) {

    event.preventDefault();
    var keyPressed = $(this).attr('id');

	$.get(myScript, { command: keyPressed }, function(data, status){

		console.log("[INFO] DATA: " + data + ", STATUS: " + status);

		if (data == 1)
		{
			$(".activity").addClass("btn-primary");
			$(".activity-icon").addClass("icon-white");
		} else {
			$(".activity").addClass("btn-danger");
			$(".activity-icon").addClass("icon-white");
		}

		setTimeout(clear, 200);
	});
});

// Clear the activity display
function clear() {
	$(".activity").removeClass("btn-primary btn-danger");
	$(".activity-icon").removeClass("icon-white");
};

// Lets get some shortcuts going
$(document).keypress(function(event) {
	event.preventDefault();
	//alert(event.which); // Keep this to check the keys, just uncomment the first section
	$('[data-keycode="' + event.which + '"]').click();
});