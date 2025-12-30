let latitude = null;
let longitude = null;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("GPS not supported by browser");
    }
}

function showPosition(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;

    document.getElementById("location").innerText =
        "Using GPS → Latitude: " + latitude.toFixed(4) +
        ", Longitude: " + longitude.toFixed(4);

    // Clear manual location if GPS is used
    document.getElementById("manualLocation").value = "";
}

function predict() {
    const timeWindow = document.getElementById("timeWindow").value;
    const manualLocation = document.getElementById("manualLocation").value;

    let payload = {
        time_window: timeWindow
    };

    if (manualLocation.trim() !== "") {
        payload.location_name = manualLocation;

        document.getElementById("location").innerText =
            "Using manual location → " + manualLocation;

    } else if (latitude !== null && longitude !== null) {
        payload.latitude = latitude;
        payload.longitude = longitude;

    } else {
        alert("Please use GPS or enter a location");
        return;
    }

    // Show loading message
    document.getElementById("result").innerHTML =
        "<p>⏳ Fetching latest weather data...</p>";

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
    if (data.error) {
        document.getElementById("result").innerHTML =
            `<p style="color:red;">${data.error}</p>`;
        return;
    }

    document.getElementById("result").innerHTML = `
        <p><b>Location:</b> ${data.location}</p>
        <p style="font-size:13px;">(${data.coordinates})</p>

        <p><b>Prediction Time:</b> ${data.prediction_time}</p>

        <p style="color:#1e88e5; font-weight:600;">
            ⏱ Last Updated: ${data.last_updated}
        </p>

        <p><b>Predicted Visibility:</b> ${data.predicted_visibility_km} km</p>
        <p><b>Risk Level:</b> ${data.risk_level}</p>
        <p><b>Advisory:</b> ${data.advisory}</p>
    `;
})


    };

