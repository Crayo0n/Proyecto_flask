const inputs = {
  email: document.getElementById("email"),
  telefono: document.getElementById("telefono"),
  url: document.getElementById("url"),
};

const messages = {
  email: document.getElementById("emailMsg"),
  telefono: document.getElementById("telefonoMsg"),
  url: document.getElementById("urlMsg"),
};

// Validación en tiempo real
Object.keys(inputs).forEach((field) => {
  inputs[field].addEventListener("input", async function () {
    if (this.value.trim() === "") {
      this.className = "";
      messages[field].textContent = "";
      return;
    }

    const response = await fetch("/validate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        field: field,
        value: this.value,
      }),
    });

    const data = await response.json();

    if (data.valid) {
      this.className = "valid";
      messages[field].className = "message success";
      messages[field].textContent = "✓ " + data.message;
    } else {
      this.className = "invalid";
      messages[field].className = "message error";
      messages[field].textContent = "✗ " + data.message;
    }
  });
});

// Validación al enviar el formulario
document
  .getElementById("validationForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = {
      email: inputs.email.value,
      telefono: inputs.telefono.value,
      url: inputs.url.value,
    };

    const response = await fetch("/validate_all", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    const data = await response.json();

    if (data.all_valid) {
      alert(
        "✓ ¡Todos los campos son válidos!\n\n" +
          JSON.stringify(data.results, null, 2)
      );
    } else {
      alert(
        "✗ Hay errores en el formulario. Por favor, revisa los campos marcados."
      );
    }
  });
