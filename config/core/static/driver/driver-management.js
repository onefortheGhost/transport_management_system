$(document).ready(function() {
    $.ajax({
        url: '/api/v1/drivers/',
        type: 'GET',
        success: function(data) {
            var driverArea = $('#driver-area');
            data.forEach(function(driver) {
                console.log(driver)
                driverArea.append(`
                    <div class="card mb-3">  <!-- Driver Card -->
                        <div class="card-body d-flex justify-content-between align-items-center">
                            <div class="flex-grow-1">
                                <h5 class="card-title">${driver.First_Name} ${driver.Last_Name}</h5>
                            </div>
                            <div>
                            </div>
                            <div class="flex-grow-1 text-center">
                                <p class="card-text"><strong>Vehicle Assignment</strong></p>
                                <p class="card-text"><strong>Status</strong></p>

                            </div>
                            <div>
                                <button class="btn btn-primary" onclick="viewDriverModal(${driver.id})">View</button>
                                <button class="btn btn-danger" onclick="deleteDriverModal(${driver.id})">Delete</button>
                            </div>
                        </div>

                    </div>
                `);
            });
        },
        error: function(error) {
            console.error('Failed to fetch drivers:', error);
        }
    });
});


function viewVehicleModal(driverID) {
    $.ajax({
        url: '/api/v1/drivers/' + driverId,
        type: 'GET',
        success: function(data) {
            $('#driverDetailModal .modal-body').html(`
                `);
            $('#driverDetailModal').modal('show');
        },
        error: function(error) {
            console.error('Failed to fetch driver:', error);
        }
    });
}

function deleteDriveModal(driverId) {
    $.ajax({
        url: '/api/v1/drivers/' + driverId,
        type: 'DELETE',
        success: function() {
            alert('Driver deleted successfully');
            location.reload();
        },
        error: function(error) {
            console.error('Failed to delete driver:', error);
        }
    })
}