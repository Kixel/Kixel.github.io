function togglehidden(pid) {
	var element = document.getElementById(pid);
	if(element.classList.contains("spoilered")) {
		element.classList.remove("spoilered");
	} else {
		element.classList.add("spoilered");
	}
}

function refreshframe(pid) {
	document.getElementById(pid).src = document.getElementById(pid).src;
}