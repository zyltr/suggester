/*** Events ***/

document.addEventListener("DOMContentLoaded", () => {
  const decreaseButton = document.getElementById("decrease");
  const increaseButton = document.getElementById("increase");

  [decreaseButton, increaseButton].forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();

      const lengthInput = document.getElementById("length");
      const length = lengthInput.valueAsNumber;

      if (button === decreaseButton) {
        const minimum = lengthInput.min;
        lengthInput.value = Math.max(minimum, length - 1);
      } else {
        const maximum = lengthInput.max;
        lengthInput.value = Math.min(maximum, length + 1);
      }

      post();
    });
  });

  const generateButton = document.getElementById("generate");

  generateButton.addEventListener("click", (event) => {
    event.preventDefault();
    post();
  });

  const identifiers = [
    "digits",
    "length",
    "lowercase",
    "punctuation",
    "uppercase",
  ];

  const elements = identifiers.map((id) => document.getElementById(id));

  elements.forEach((element) => {
    element.addEventListener("change", (_) => {
      post();
    });
  });
});

window.addEventListener("load", () => {
  configureTooltips();
});

/*** Functions ***/

function configureTooltips() {
  const copyButton = document.getElementById("copy");
  const sugegstionTextArea = document.getElementById("suggestion");

  [copyButton, sugegstionTextArea].forEach((element) => {
    const tooltip = new bootstrap.Tooltip(element, {
      placement: "top",
      title: "Copied",
      trigger: "manual",
    });

    element.addEventListener("click", (_) => {
      navigator.clipboard.writeText(sugegstionTextArea.value).then(
        (_) => {
          tooltip.show();
          window.setTimeout(() => {
            tooltip.hide();
            if (element === sugegstionTextArea) {
              sugegstionTextArea.blur();
            }
          }, 500);
        },
        (reason) => {
          console.error(reason);
        },
      );
    });
  });
}

function post() {
  const form = document.getElementById("new");
  const token = document.querySelector("[name=csrfmiddlewaretoken]").value;

  const url = "new/";
  const options = {
    body: new FormData(form),
    method: "POST",
    headers: { "X-CSRFToken": token },
    mode: "same-origin",
  };

  const request = new Request(url, options);

  fetch(request)
    .then((response) => response.json())
    .then((data) => updateUI(data))
    .catch((_) => window.location.reload());
}

function updateUI(data) {
  const lengthInput = document.getElementById("length");
  const length = Math.max(data.suggestion.length, lengthInput.value);

  lengthInput.value = length;

  const decreaseButton = document.getElementById("decrease");
  const increaseButton = document.getElementById("increase");
  decreaseButton.disabled = length <= lengthInput.min;
  increaseButton.disabled = length >= lengthInput.max;

  const suggestionTextArea = document.getElementById("suggestion");
  suggestionTextArea.innerHTML = data.suggestion;
  suggestionTextArea.style.height = "auto";
  suggestionTextArea.style.height = suggestionTextArea.scrollHeight + "px";

  const informational = document.getElementById("informational");
  informational.innerHTML = length.toString();
}
