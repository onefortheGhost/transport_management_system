$(document).ready(function() {
    $.ajax({
        url: '/api/v1/dispatch-database/',
        type: 'GET',
        success: function(data) {
            var dispatchArea = $('#dispatch-area');
            data.forEach(function(dispatch) {
                // TODO Consider putting this into the handleDispatchCardOrder function
                dispatchArea.append(`
                    <div class="card-group" "card mb-3"> <!-- Dispatch Card -->
                            <div class="card-body d-flex justify-content-between align-items-center"> 
                                ` + handleDispatchCardOrder(dispatch) + `

                    </div>
                `);
            });
        },
        error: function(error) {
            console.error('Failed to fetch dispatches:', error);
        }
    });
});


function handleDispatchCardOrder(dispatch, cardOrder = ['pickup', 'dropoff', 'vehicle', 'driver', 'status', 'customer']){
     // TODO change default cardOrder to a getOrder function from the user's settings
    var cardCollection= '' // Create a string to hold all the cards
    for (var i = 0; i < cardOrder.length; i++){
        var card = cardOrder[i]
        if (card == 'pickup'){
            cardCollection += createPickupCard(dispatch)
        }
        else if (card == 'dropoff'){
            cardCollection += createDropoffCard(dispatch)
        }
        else if (card == 'vehicle'){
            cardCollection += createVehicleCard(dispatch)
        }
        else if (card == 'driver'){
            cardCollection += createDriverCard(dispatch)
        }
        else if (card == 'status'){
            cardCollection += createStatusCard(dispatch)
        }
        else if (card == 'customer'){
            cardCollection += createCustomerCard(dispatch)
        }
    }
    return cardCollection
}

//  Create the cards

function createPickupCard(dispatch){
    var pickupCard = `
        <div class="flex-grow-1 mr-2 text-center"> <!-- Pickup Card -->
            <p class="card-title mb-0"> <strong>Pickup Period</strong> </p>
            <p class="mb-0">${dispatch.pickup_date_start} to ${dispatch.pickup_date_end}</p>
            <p class="mb-0">${dispatch.pickup_time_start} to ${dispatch.pickup_time_end}</p>
        </div>`
    return pickupCard;
}

function createDropoffCard(dispatch){
    var dropoffCard = `
        <div class="flex-grow-1 mr-2 text-center"> <!-- Dropoff Card -->
            <p class="card-text mb-0"> <strong>Dropoff Period</strong> </p>
            <p class="mb-0">${dispatch.dropoff_date_start} to ${dispatch.dropoff_date_end}</p>
            <p class="mb-0">${dispatch.dropoff_time_start} to ${dispatch.dropoff_time_end}</p>
        </div>`
    return dropoffCard
}

function createVehicleCard(dispatch){
    var vehicleCard = `
        <div class="flex-grow-1 mr-2 text-center mb-0"> <!-- Vehicle Card -->
            <p class="card-text mb-0"><strong>Vehicle Assignment</strong></p>
            <p class="mb-0">${dispatch.vehicle}</p>
        </div>`
    return vehicleCard
}

function createDriverCard(dispatch){
    var driverCard = `
        <div class="flex-grow-1 mr-2 text-center mb-0"> <!-- Driver Card -->
            <p class="card-text mb-0"><strong>Driver Assignment</strong></p>
            <p class="mb-0">${dispatch.driver}</p>
        </div>`
    return driverCard
}

function createStatusCard(dispatch){
    var statusCard = `
        <div class="flex-grow-1 mr-2 text-center mb-0"> <!-- Status Card -->
            <p class="card-text mb-0"><strong>Status</strong></p>
            <p class="mb-0">${dispatch.status}</p>
        </div>`
    return statusCard
}

function createCustomerCard(dispatch){
    var customerCard = `
        <div class="flex-grow-1 mr-2 text-center mb-0"> <!-- Customer Card -->
            <p class="card-text mb-0"><strong>Customer</strong></p>
            <p class="mb-0">${dispatch.customer}</p>
        </div>`
    return customerCard
}

// End create the cards