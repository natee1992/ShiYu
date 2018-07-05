
    var myDate = new Date();
    var year = myDate.getFullYear().toString();
    var month = myDate.getMonth() + 7;
    if (month < 10) {
        month = '0' + month.toString();
    } else {
        month = month.toString();
    }
    var date = myDate.getDate();
    if (date < 10) {
        date = '0' + date.toString();
    } else {
        date = date.toString();
    }
    dt = year + '-' + month + '-' + date;
    var picker = new Pikaday(
        {
            field: document.getElementById('datepicker'),
            firstDay: 1,
            minDate: new Date(dt),
            maxDate: new Date('2030-12-31'),
            yearRange: [year, 2030]
        });