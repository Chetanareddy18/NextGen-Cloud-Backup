document.addEventListener("DOMContentLoaded", () => {
  // Upload History (Bar Chart)
  new Chart(document.getElementById("uploadChart"), {
    type: "bar",
    data: {
      labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
      datasets: [{
        label: "Files Uploaded",
        data: [2, 5, 3, 7, 4, 6, 5],
        backgroundColor: "#2563eb",
        borderRadius: 8
      }]
    },
    options: {
      scales: { y: { beginAtZero: true } },
      plugins: { legend: { display: false } }
    }
  });

  // Cloud Storage (Doughnut)
  new Chart(document.getElementById("storageChart"), {
    type: "doughnut",
    data: {
      labels: ["Azure", "AWS"],
      datasets: [{
        data: [58, 42],
        backgroundColor: ["#2563eb", "#f59e0b"]
      }]
    },
    options: {
      plugins: {
        legend: { position: "bottom" }
      }
    }
  });

  // Ransomware Detection (Line)
  new Chart(document.getElementById("ransomwareChart"), {
    type: "line",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
      datasets: [{
        label: "Detected Threats",
        data: [3, 1, 4, 0, 2, 1, 0],
        borderColor: "#ef4444",
        tension: 0.4,
        fill: false
      }]
    },
    options: {
      plugins: { legend: { display: false } },
      scales: { y: { beginAtZero: true } }
    }
  });
});
