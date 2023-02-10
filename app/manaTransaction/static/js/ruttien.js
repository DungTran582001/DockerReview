get_alert_ele = document.querySelector(".alert")
function Close_Alert() {
     return get_alert_ele.classList.add("hidden");
}

window.setTimeout(Close_Alert, 4000);