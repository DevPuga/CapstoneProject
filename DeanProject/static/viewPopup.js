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

function newContent(divID, content){
    var div = document.createElement('div');
    document.getElementById(divID).className = "col";
    div.innerHTML = content;
    document.getElementById(divID).appendChild(div);
}

function newTitle(divID, title){
    var div = document.createElement('div');
    document.getElementById(divID).className = "col-4";
    div.innerHTML = title;
    document.getElementById(divID).appendChild(div);
}

function newLinePTRV(formid, title, content){
    newTitle("DeanProject_permittoregister"+formid+"Title", "<strong>" + title + "</strong>");
    newContent("DeanProject_permittoregister"+formid+"Content", content);
}

function newLineADCV(formid, title, content){
    newTitle("DeanProject_add_dropclass"+formid+"Title", "<strong>" + title + "</strong>");
    newContent("DeanProject_add_dropclass"+formid+"Content", content);
}

function newLineUGGV(formid, title, content){
    newTitle("DeanProject_uggraduation"+formid+"Title", "<strong>" + title + "</strong>");
    newContent("DeanProject_uggraduation"+formid+"Content", content);
}

function newLineMGV(formid, title, content){
    newTitle("DeanProject_mastergraduation"+formid+"Title", "<strong>" + title + "</strong>");
    newContent("DeanProject_mastergraduation"+formid+"Content", content);
}

function newLineDAARV(formid, title, content){
    newTitle("DeanProject_degreeauditamendmentrequest"+formid+"Title", "<strong>" + title + "</strong>");
    newContent("DeanProject_degreeauditamendmentrequest"+formid+"Content", content);
}

function newLineDAV(formid, title, content){
    newTitle("DeanProject_degreeaudit"+formid+"Title", "<strong>" + title + "</strong>");
    newContent("DeanProject_degreeaudit"+formid+"Content", content);
}

function newLineTRV(formid, title, content){
    newTitle("DeanProject_transcriptrequest"+formid+"Title", "<strong>" + title + "</strong>");
    newContent("DeanProject_transcriptrequest"+formid+"Content", content);
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
