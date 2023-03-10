const numberButtons = document.querySelectorAll('[data-bookMe]')
const dateTitle = document.querySelector('[data-date]')
const nextButton = document.querySelector('[data-next-button]')
const backButton = document.querySelector('[data-back-button]')
const bookedTimesArray = []

let dateOn = new Date()
console.log(dateOn)
dateTitle.innerText = dateOn.toDateString()

//initiate dataPull(dateOn.toDateString()) on load

numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        console.log( `${dateTitle.innerText} ${button.innerText}`)
        button.style.backgroundColor = '#FB4D3D' 
        bookedTimesArray.push(`${dateTitle.innerText} ${button.innerText}`)// adds time and date booked so that this can be processed by json at later date
        console.log(bookedTimesArray)
    })
})

nextButton.addEventListener('click', () => {
    //initiate dataPull(dateOn.toDateString()) in dbRequest.py
    numberButtons.forEach(button => { 
        button.style.backgroundColor = '#60A561'
    })
    console.log("button works");
    dateOn.setDate(dateOn.getDate()+1)
    dateTitle.innerText = dateOn.toDateString()
    console.log(dateOn)
    
    bookedTimesArray.forEach(booking => {
        let bookingDate = booking.substring(0, 15)
        if(dateOn.toDateString() === bookingDate) {
            let bookingTime = booking.substring(16,21)
            console.log(bookingTime)
            numberButtons.forEach(button => { 
                if(button.innerText === bookingTime){
                    // console.log("They Equal")
                    button.style.backgroundColor = '#FB4D3D'
                }
            })
        }
    })

    const dbReqJSON = JSON.stringify(dateTitle.innerText)
    console.log(dbReqJSON) // send to server side and pull all times booked from db where dateTitle = PK of bookTBL

})

backButton.addEventListener('click', () => {
    numberButtons.forEach(button => {
        button.style.backgroundColor = '#60A561'
     })
    dateOn.setDate(dateOn.getDate()-1)
    dateTitle.innerText = dateOn.toDateString()
    console.log(dateOn)
    bookedTimesArray.forEach(booking => {
        let bookingDate = booking.substring(0, 15)
        if(dateOn.toDateString() === bookingDate) {
            let bookingTime = booking.substring(16,21)
            console.log(bookingTime)
            numberButtons.forEach(button => { 
                if(button.innerText === bookingTime){
                    // console.log("They Equal")
                    button.style.backgroundColor = '#FB4D3D'
                }
            })
        }

    })
})

window.onbeforeunload = confirmExit;
function confirmExit(){
    const jsonString = JSON.stringify(bookedTimesArray)
    console.log(jsonString)
    // initate the send2DB() function in dbRequest.py
    return false;
}