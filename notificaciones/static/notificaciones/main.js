import axios from 'axios';
function actualizarListaVibraciones(vibraciones) {
    const listaVibraciones = document.getElementById('lista-vibraciones');
    const ul = listaVibraciones.querySelector('ul');

    // Limpiar la lista antes de agregar nuevos elementos
    ul.innerHTML = '';

    // Recorrer las vibraciones y agregarlas a la lista
    vibraciones.forEach(vibracion => {
        const li = document.createElement('li');
        li.textContent = `Intensidad: ${vibracion.intensidad} - Timestamp: ${vibracion.timestamp}`;
        ul.appendChild(li);
    });
}


document.addEventListener('DOMContentLoaded', () => {
    // Obtener datos al cargar la página
    axios.get('http://localhost:8000/notificaciones/api/vibraciones/')
        .then(response => {
            actualizarListaVibraciones(response.data);
        })
        .catch(error => {
            console.error('Error al obtener datos de la API:', error);
        });

    // Manejar el envío del formulario
    const formulario = document.getElementById('formulario-vibracion');
    formulario.addEventListener('submit', function (event) {
        event.preventDefault();

        // Obtener datos del formulario
        const intensidad = document.getElementById('intensidad').value;
        const timestamp = document.getElementById('timestamp').value;

        // Enviar datos al servidor
        axios.post('http://localhost:8000/notificaciones/api/vibraciones/enviar_datos/', {
            intensidad: intensidad,
            timestamp: timestamp
        })
        .then(response => {
            console.log('Datos enviados correctamente:', response.data);
            // Puedes actualizar la lista de vibraciones si lo deseas
        })
        .catch(error => {
            console.error('Error al enviar datos al servidor:', error);
        });
    });
});
