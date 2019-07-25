
let addObjectiveButton = document.querySelector('#add_objective');
let objectiveForm = document.querySelector('#objectives>form');
addObjectiveButton.addEventListener('click',addObjective);


function addObjective(){

	objectiveContainer = document.createElement('div');
 	objectiveForm.appendChild(objectiveContainer);

	objective = document.createElement('input');
	objective.setAttribute('type','text');
 	objective.setAttribute('name','objective');
 	objective.setAttribute('placeholder','Enter your daily objective.');
	objectiveContainer.appendChild(objective);

}


let addEventButton = document.querySelector('#add_event');
let eventList = document.querySelector('#day>ul');
addEventButton.addEventListener('click',addEvent);

function addEvent(){
	eventContainer = document.createElement('li');
	eventList.appendChild(eventContainer);

	event = document.createElement('input');
	event.setAttribute('type','text');
 	event.setAttribute('name','event');
 	event.setAttribute('placeholder','Enter your event.');
	eventContainer.appendChild(event)
	deleteEventButton = document.createElement('button');
	deleteEventButton.appendChild(document.createTextNode('Delete Event'));
	eventContainer.appendChild(deleteEventButton);
	deleteEventButton.addEventListener('click',deleteEvent);
	function deleteEvent(){
	 	eventList.removeChild(eventContainer);
	}
