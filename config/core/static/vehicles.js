$(document).ready(function() {
    $('#load-vehicles').click(function() {
        $.ajax({
            url: '/api/v1/vehicles/',
            method: 'GET',
            success: function(data) {
                $('#vehicle-area').empty(); // Clear previous entries
                data.forEach(function(vehicle) {
                    $('#vehicle-area').append(`
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">${vehicle.make} ${vehicle.model}</h5>
                                <p class="card-text">${vehicle.year}</p>
                            </div>
                        </div>
                    `);
                });
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
