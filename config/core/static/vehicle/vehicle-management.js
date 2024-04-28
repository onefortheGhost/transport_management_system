$(document).ready(function() {
    $.ajax({
        url: '/api/v1/vehicles/',
        type: 'GET',
        success: function(data) {
            var vehicleArea = $('#vehicle-area');
            data.forEach(function(vehicle) {
                vehicleArea.append(`
                    <div class="card mb-3">
                        <div class="card-body d-flex justify-content-between align-items-center">
                            <div class="flex-grow-1">
                                <h5 class="card-title">${vehicle.make} ${vehicle.model}</h5>
                                <p class="card-text">Year: ${vehicle.year}</p>
                            </div>
                            <div>
                            </div>
                            <div class="flex-grow-1 text-center">
                                <p class="card-text"><strong>Load Number</strong></p>
                                <p class="card-text"><strong>Status</strong></p>

                            </div>
                            <div>
                                <button class="btn btn-primary" onclick="viewVehicleModal(${vehicle.id})">View</button>
                                <button class="btn btn-danger" onclick="deleteVehicleModal(${vehicle.id})">Delete</button>
                            </div>
                        </div>

                    </div>
                `);
            });
        },
        error: function(error) {
            console.error('Failed to fetch vehicles:', error);
        }
    });
});


function viewVehicleModal(vehicleId) {
    $.ajax({
        url: '/api/v1/vehicles/' + vehicleId,
        type: 'GET',
        success: function(data) {
            $('#vehicleDetailModal .modal-body').html(`
                <p>Make: ${data.make}</p>
                <p>Model: ${data.model}</p>
                <p>Year: ${data.year}</p>
                `);
            $('#vehicleDetailModal').modal('show');
        },
        error: function(error) {
            console.error('Failed to fetch vehicle:', error);
        }
    });
}

function deleteVehicleModal(vehicleId) {
    $.ajax({
        url: '/api/v1/vehicles/' + vehicleId,
        type: 'DELETE',
        success: function() {
            alert('Vehicle deleted successfully');
            location.reload();
        },
        error: function(error) {
            console.error('Failed to delete vehicle:', error);
        }
    })
}