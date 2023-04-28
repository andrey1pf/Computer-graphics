function showInputs(numInputs) {
	var inputsContainer = document.getElementById("inputs-container");
	inputsContainer.innerHTML = "";

	for (var i = 0; i < numInputs; i++) {
		var input = document.createElement("input");
		input.type = "text";
		input.name = "input" + (i + 1);
		input.placeholder = "Введите значение " + (i + 1);
		inputsContainer.appendChild(input);
	}
}
