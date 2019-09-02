$( document ).ready(function() {
    let sheetContainer = $("#worker-time-line");
    if (sheetContainer) {
        getCompanyWorkingSheetData();
    }
});

function createSheetRows(rowsNumber) {
    let sheetContainer = $("#worker-time-line");
    sheetContainer.css("grid-template-rows", "repeat("+rowsNumber+", 50px)");
}

function getCompanyWorkingSheetData() {
    $.ajax(window.location.href+'/schedules/2019/08/31',
    {
        success: function (data, status, xhr) {
            console.log(data);
            console.log(Object.keys(data).length);
            createSheetRows(Object.keys(data).length)
    }
});
}