function updateSoilFields(soilType) {
    $(".clay-sand, .clay, .sand, .bearing-c").hide(); // Hide all initially

    if (soilType === "clay" || soilType === "sand") {
        $(".clay-sand").show();
    }
    if (soilType === "clay") {
        $(".clay").show();
    }
    if (soilType === "sand") {
        $(".sand").show();
    }
    if (soilType === "bearing_c") {
        $(".bearing-c").show(); 
    }
}

// Access the soil type passed from Flask
var soilType = "{{ soil_type }}";

// Call the function to update fields based on soil type
updateSoilFields(soilType)

// function to format displayed soil type
// function formatSoilType(soilType) {
//     soilType = soilType.charAt(0).toUpperCase() + soilType.slice(1); // Capitalize first letter
    
//     if (soilType === "Bearing_c") {
//       soilType = "Bearing Capacity Provided"; // Replace for "Bearing_c"
//     }
    
//     return soilType;
//   }
