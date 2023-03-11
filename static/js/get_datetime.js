window.addEventListener("load", () => {
   let dateForm = document.querySelector("#meeting_date")
   let newDate = new Date().toISOString().slice(0,new Date().toISOString().lastIndexOf(":"));
   dateForm.min = new Date().toISOString().slice(0,new Date().toISOString().lastIndexOf(":"));
   console.log(newDate)
});