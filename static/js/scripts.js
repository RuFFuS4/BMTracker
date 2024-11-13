async function fetchWithAuth(url, options = {}) {
    const user = firebase.auth().currentUser;
    if (user) {
        const idToken = await user.getIdToken();
        options.headers = {
            ...options.headers,
            Authorization: idToken
        };
    }
    return fetch(url, options);
}

async function addMarker() {
    const url = document.getElementById("url").value;
    const title = document.getElementById("title").value;
    const category = document.getElementById("category").value;

    const response = await fetchWithAuth('/markers', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, title, category })
    });

    if (response.ok) {
        alert("Marker added!");
        loadMarkers();
    } else {
        alert("Failed to add marker.");
    }
}

/*async function loadMarkers() {
    const response = await fetch('/markers');
    const markers = await response.json();

    const markerList = document.getElementById("marker-list");
    markerList.innerHTML = "";

    markers.forEach(marker => {
        const item = document.createElement("div");
        item.className = "marker-item";
        item.innerHTML = `
            <strong>${marker.title}</strong> - <a href="${marker.url}" target="_blank">${marker.url}</a>
            <p>Category: ${marker.category}</p>
            <button onclick="deleteMarker('${marker.id}')">Delete</button>
        `;
        markerList.appendChild(item);
    });
}

async function deleteMarker(id) {
    const response = await fetch(`/markers/${id}`, { method: 'DELETE' });
    if (response.ok) {
        alert("Marker deleted!");
        loadMarkers();
    } else {
        alert("Failed to delete marker.");
    }
}

// Cargar los marcadores cuando la página esté lista
document.addEventListener("DOMContentLoaded", loadMarkers);

// Función para registrarse
async function registerUser(email, password) {
    try {
        const userCredential = await firebase.auth().createUserWithEmailAndPassword(email, password);
        alert("User registered!");
        return userCredential.user;
    } catch (error) {
        alert("Error registering user: " + error.message);
    }
}*/

// Función para iniciar sesión
async function loginUser(email, password) {
    try {
        const userCredential = await firebase.auth().signInWithEmailAndPassword(email, password);
        alert("User logged in!");
        return userCredential.user;
    } catch (error) {
        alert("Error logging in: " + error.message);
    }
}

// Función para cerrar sesión
async function logoutUser() {
    try {
        await firebase.auth().signOut();
        alert("User logged out!");
    } catch (error) {
        alert("Error logging out: " + error.message);
    }
}
