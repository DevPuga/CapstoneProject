function func(){
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}

function displayPopup(popup){
    var popup = document.getElementById(popup.id);
    popup.style.display = "block";
}

function closePopup(popup){
    var popup = document.getElementById(popup.id);
    popup.style.display = "none";
}


function newLine(divID, content){
    var div = document.createElement('div');
      div.innerHTML = content;
      document.getElementById(divID).appendChild(div);
}

function newLinePTRV(formid, content){
    newLine("DeanProject_permittoregister"+formid+"Content", content);
}

function newLineADCV(formid, content){
    newLine("DeanProject_add_dropclass"+formid+"Content", content);
}

function newLineUGGV(formid, content){
    newLine("DeanProject_uggraduation"+formid+"Content", content);
}

function newLineMGV(formid, content){
    newLine("DeanProject_mastergraduation"+formid+"Content", content);
}

function newLineDAARV(formid, content){
    newLine("DeanProject_degreeauditamendmentrequest"+formid+"Content", content);
}

function newLineDAV(formid, content){
    newLine("DeanProject_degreeaudit"+formid+"Content", content);
}

function newLineTRV(formid, content){
    newLine("DeanProject_transcriptrequest"+formid+"Content", content);
}

function print(thing){
    console.log(thing);
}

function getViewContent(formName, formid){
    switch(String(formName)){
        case "DeanProject_permittoregister":
            permitToRegisterView(formid);
            break;
        case "DeanProject_add_dropclass":
            add_dropClassView(formid);
            break;
        case "DeanProject_uggraduation":
            UGGraduationView(formid)
            break;
        case "DeanProject_mastergraduation":
            MasterGraduationView(formid)
            break;
        case "DeanProject_degreeauditamendmentrequest":
            DegreeAuditAmendmentRequestView(formid)
            break;
        case "DeanProject_degreeaudit":
            DegreeAuditView(formid)
            break;
        case "DeanProject_transcriptrequest":
            TranscriptRequestView(formid)
            break;
        default:
        console.log("GetViewContent: " + formName + " was not recognized");
    }
}