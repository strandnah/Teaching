document.querySelectorAll(".accordion-button").forEach((button) => {
  button.addEventListener("click", () => {
    const id = button.id.split("-")[0] + "-info";
    const content = document.getElementById(id);
    document.querySelectorAll(".accordion-content").forEach((item) => {
      if (item !== content) {
        item.classList.add("hidden");
      }
    });
    content.classList.toggle("hidden");
  });
});
