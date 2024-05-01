$(document).ready(function() {
    $.ajax({
        url: '/api/v1/dispatch-database/',
        type: 'GET',
        success: function(data) {
            var dispatchArea = $('#dispatch-area');
            data.forEach(function(dispatch) {
                dispatchArea.append(`
                    <div class="card mb-3"> <!-- Dispatch Card -->
                        <div class="card-body d-flex justify-content-between align-items-center">
                            <div class="flex-grow-1">
                                <h5 class="card-title">${dispatch.dispatch_date_creation}</h5>
                            </div>
                            <div>
                            </div>
                            <div class="flex-grow-1 text-center">
                                <p class="card-text"><strong>Load Number</strong></p>
                                <p class="card-text"><strong>Status</strong></p>

                            </div>
                            <div>
                                <button class="btn btn-primary" onclick="viewDispatchModal(${dispatch.id})">View</button>
                                <button class="btn btn-danger" onclick="deleteDispatchModal(${dispatch.id})">Delete</button>
                            </div>
                        </div>

                    </div>
                `);
            });
        },
        error: function(error) {
            console.error('Failed to fetch dispatches:', error);
        }
    });
});