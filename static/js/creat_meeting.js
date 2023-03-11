const classSelect = document.querySelector("#class_select")
const classList = document.querySelector("#class_list")
let list = []

classSelect.addEventListener("change", function (){
    if (list.indexOf(classSelect.value) === -1){
        list.push(classSelect.value)
        addList(list)
    }
})

function addList(list) {
    classList.replaceChildren()
    let i = 0
    while (i < list.length) {
        classList.innerHTML += "<td>" + list[i] + "<div class='remove_class'>x</div></td>"
        i++
    }
    console.log(list)
}

document.querySelectorAll(".remove_class").forEach(button => {
    button.addEventListener("hover", function (){
        classList.removeChild(classList.firstChild)
        console.log("work")
    }, false)
})

function removeItem() {

}