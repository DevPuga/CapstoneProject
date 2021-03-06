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
    document.getElementById(divID).style.width = "fit-content"
    div.innerHTML = content;
    document.getElementById(divID).appendChild(div);
}

function newTitle(divID, title){
    var div = document.createElement('div');
    document.getElementById(divID).style.width = "fit-content"
    div.innerHTML = title;
    document.getElementById(divID).appendChild(div);
}

function newWideTitle(divID, title){
    var div = document.createElement('div');
    document.getElementById(divID).style.width = "fit-content"
    div.innerHTML = title;
    document.getElementById(divID).appendChild(div);
}

function createTable(divID, tableNum, tableTitle){
    var table = document.createElement('table');
    tableID = divID + tableNum;
    table.setAttribute("id", tableID);
    var title = document.createElement('h5');
    var text = document.createTextNode(tableTitle);
    title.appendChild(text)
    document.getElementById(divID).appendChild(title);
    document.getElementById(divID).appendChild(table);
    document.getElementById(tableID).className = "mb-3";
}

function newCell(rowid, content) {
    var cell = document.createElement("td");
    var text = document.createTextNode(content);
    cell.appendChild(text);
    document.getElementById(rowid).appendChild(cell);
}

function createHeader(tableid, tableNum, content) {
    var cell = document.createElement("th");
    var text = document.createTextNode(content);
    cell.appendChild(text);
    document.getElementById(tableid + tableNum).appendChild(cell);
}

function newRowPTR(formid, tableNum, rowNum, crn, prefix, courseNum, secNo) {
    if (crn != "" && prefix != "" && courseNum != "" && secNo != ""){
      var tableid = "DeanProject_permittoregister" + formid + "Table";
      var rowid = tableid + tableNum + rowNum;
      var row = document.createElement("tr");
      row.setAttribute("id", rowid);
      document.getElementById(tableid + tableNum).appendChild(row);
      newCell(rowid, crn);
      newCell(rowid, prefix);
      newCell(rowid, courseNum);
      newCell(rowid, secNo);
    }
}

function newRowADC(formid, tableNum, rowNum, crn, prefix, courseNum, secNo, attend) {
    if (crn != "" && prefix != "" && courseNum != "" && secNo != ""){
      var tableid = "DeanProject_add_dropclass" + formid + "Table";
      var rowid = tableid + tableNum + rowNum;
      var row = document.createElement("tr");
      row.setAttribute("id", rowid);
      document.getElementById(tableid + tableNum).appendChild(row);
      newCell(rowid, crn);
      newCell(rowid, prefix);
      newCell(rowid, courseNum);
      newCell(rowid, secNo);
      if (attend) {
        newCell(rowid, attend)
      }
    }
}

function newRowDA(formid, tableNum, rowNum, courseA, courseB) {
  if (courseA != "" && courseB != ""){
    var tableid = "DeanProject_degreeaudit" + formid + "Table";
    var rowid = tableid + tableNum + rowNum;
    var row = document.createElement("tr");
    row.setAttribute("id", rowid);
    document.getElementById(tableid + tableNum).appendChild(row);
    newCell(rowid, courseA);
    newCell(rowid, courseB);
  }
}

function newRowDAARTransfer(formid, tableNum, rowNum, institution, courseSubjectA, courseNumA, grade, semTaken, courseSubjectB, courseNumB, courseEQ, courseSub) {
  if (institution != "" && courseSubjectA != "" && courseNumA != "" && grade != "" && semTaken != "" && courseSubjectB != "" && courseNumB != "") {
    var tableid = "DeanProject_degreeauditamendmentrequest" + formid + "Table";
    var rowid = tableid + tableNum + rowNum;
    var row = document.createElement("tr");
    row.setAttribute("id", rowid);
    document.getElementById(tableid + tableNum).appendChild(row);
    newCell(rowid, institution);
    newCell(rowid, courseSubjectA);
    newCell(rowid, courseNumA);
    newCell(rowid, grade);
    newCell(rowid, semTaken);
    newCell(rowid, courseSubjectB);
    newCell(rowid, courseNumB);
    newCell(rowid, courseEQ);
    newCell(rowid, courseSub);
  }
}

function newRowDAARSubA(formid, tableNum, rowNum, coursePrefix, courseNum, semesterTaken) {
  if (coursePrefix != "" && courseNum != "" && semesterTaken != ""){
    var tableid = "DeanProject_degreeauditamendmentrequest" + formid + "Table";
    var rowid = tableid + tableNum + rowNum;
    var row = document.createElement("tr");
    row.setAttribute("id", rowid);
    document.getElementById(tableid + tableNum).appendChild(row);
    newCell(rowid, coursePrefix);
    newCell(rowid, courseNum);
    newCell(rowid, semesterTaken);
  }
}

function newRowDAARSubB(formid, tableNum, rowNum, coursePrefix, courseNum) {
  if (coursePrefix != "" && courseNum != ""){
    var tableid = "DeanProject_degreeauditamendmentrequest" + formid + "Table";
    var rowid = tableid + tableNum + rowNum;
    var row = document.createElement("tr");
    row.setAttribute("id", rowid);
    document.getElementById(tableid + tableNum).appendChild(row);
    newCell(rowid, coursePrefix);
    newCell(rowid, courseNum);
  }
}

function newRowDAARWaive(formid, tableNum, rowNum, coursePrefix, courseNum, comments) {
  if (coursePrefix != "" && courseNum != "" && comments != ""){
    var tableid = "DeanProject_degreeauditamendmentrequest" + formid + "Table";
    var rowid = tableid + tableNum + rowNum;
    var row = document.createElement("tr");
    row.setAttribute("id", rowid);
    document.getElementById(tableid + tableNum).appendChild(row);
    newCell(rowid, coursePrefix);
    newCell(rowid, courseNum);
    newCell(rowid, comments);
  }
}

function newLinePTRV(formid, title, content){
    newTitle("DeanProject_permittoregister"+formid+"Label", "<strong>" + title + "</strong>");
    newContent("DeanProject_permittoregister"+formid+"Content", content);
}

function newLineADCV(formid, title, content){
    newWideTitle("DeanProject_add_dropclass"+formid+"Label", "<strong>" + title + "</strong>");
    newContent("DeanProject_add_dropclass"+formid+"Content", content);
}

function newLineUGGV(formid, title, content){
    newTitle("DeanProject_uggraduation"+formid+"Label", "<strong>" + title + "</strong>");
    newContent("DeanProject_uggraduation"+formid+"Content", content);
}

function newLineMGV(formid, title, content){
    newTitle("DeanProject_mastergraduation"+formid+"Label", "<strong>" + title + "</strong>");
    newContent("DeanProject_mastergraduation"+formid+"Content", content);
}

function newLineDAARV(formid, title, content){
    newTitle("DeanProject_degreeauditamendmentrequest"+formid+"Label", "<strong>" + title + "</strong>");
    newContent("DeanProject_degreeauditamendmentrequest"+formid+"Content", content);
}

function newLineDAV(formid, title, content){
    newTitle("DeanProject_degreeaudit"+formid+"Label", "<strong>" + title + "</strong>");
    newContent("DeanProject_degreeaudit"+formid+"Content", content);
}

function newLineTRV(formid, title, content){
    newWideTitle("DeanProject_transcriptrequest"+formid+"Label", "<strong>" + title + "</strong>");
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
