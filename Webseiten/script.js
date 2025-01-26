document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".accordion-button").forEach((button) => {
    button.addEventListener("click", () => {
        const content = button.nextElementSibling;
        // wechsel von show zu hidden class 
        content.classList.toggle("hidden");
        // restliche code war unnötig und hat Fehler verursacht
    });
  });
});
