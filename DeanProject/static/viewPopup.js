function func(){
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}

function displayPopup(){
    var popup = document.getElementById("popup");
    popup.style.display = "block";
}

function closePopup(){
    var popup = document.getElementById("popup");
    popup.style.display = "none";
}

function getViewContent(formName){
    switch(formName){
        case "permitToRegister":
            permitToRegisterView();
            break;
        case "add_dropClass":
            add_dropClassView();
            break;
        case "UGGraduation":
            UGGraduationView()
            break;
        case "MasterGraduation":
            MasterGraduationView()
            break;
        case "DegreeAuditAmendment":
            DegreeAuditAmendmentView()
            break;
        case "TranscriptRequest":
            TranscriptRequestView()
            break;
        default:
        console.log("GetViewContent: " + formName + " was not recognized");
    }
}

function permitToRegisterView(){
    document.getElementById("popupContent").innerHTML = "Your mom";

    var div = document.createElement('div');
    div.innerHTML = 'is';
    document.getElementById("popupContent").appendChild(div);
    var div2 = document.createElement('div');
    div2.innerHTML = 'beautiful';
    document.getElementById("popupContent").appendChild(div2);
}

function add_dropClassView(){

    document.getElementById("popupContent").innerHTML = "This one is add_dropClassForm";
}

function UGGraduationView(){

    document.getElementById("popupContent").innerHTML = "This one is UGGraduationForm";
}

function MasterGraduationView(){

    document.getElementById("popupContent").innerHTML = "This one is MasterGraduationForm";
}

function DegreeAuditAmendmentView(){

    document.getElementById("popupContent").innerHTML = "This one is DegreeAuditAmendmentForm";
}

function TranscriptRequestView(){

    document.getElementById("popupContent").innerHTML = "This one is TranscriptRequestForm";
}