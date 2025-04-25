function setHeaderTime(){
    const date = new Date()
        
    const formatted_date = date.toLocaleString(
        {
            hour: '2-digit',
            hour12: false,
            timeZone: 'America/New_York'
        },
        {
            hour: '2-digit',
            minute: '2-digit'
        }
    )


    const $header_time = $('#header_time')

    $header_time.text(`(${formatted_date})` )

    setTimeout(function () {
        setHeaderTime()
    }, 1000*45)

}

setHeaderTime()