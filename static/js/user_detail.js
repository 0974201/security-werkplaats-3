//do we even need async here?

let tering = document.querySelector('input[name=user_id').value;
let tyfus = document.querySelector('input[name=is_admin').value;

let fuck = parseInt(tering);
let arse = parseInt(tyfus);

//console.log(fuck, arse);

let shit = JSON.stringify({
    user_id : fuck,
    gebruikersnaam : document.querySelector('input[name=gebruikersnaam').value,
    wachtwoord : document.querySelector('input[name=wachtwoord').value,
    is_admin : arse
});

console.log(shit);

async function update_user(id){
    try {
        fetch('/user/' + id, {
            method: 'PATCH',
            headers: {
                'Content-Type' : 'application/json'
            }/*,
            body: JSON.stringify(table)*/
        })

        console.log("I need scissors! 61!")

    } catch(error) {

        console.log(error);
    }
}

async function delete_user(id){
    try {
        fetch('{{url_for("delete_user")}}' + id, {
            method: 'DELETE'
        })

        console.log("delet")

    } catch(error) {

        console.log(error);
    }
}