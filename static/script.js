document.getElementById('fileInput').addEventListener('change', function () {
  const file = this.files[0];
  if (!file) return; // Exit if no file is selected

  const formData = new FormData();
  formData.append('file', file); // Append file to FormData object

  // Perform file upload using Fetch API
  fetch('/', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json()) // Parse response as JSON
    .then(data => {
      if (data.error) {
        alert(data.error); // Handle error message from the backend
        return;
      }

      // Clear any previous tables before rendering new data
      const tableContainer = document.getElementById('table1-container');
      tableContainer.innerHTML = '';

      // Create and populate Table 1 with raw data from the server response
      const table1 = document.createElement('table');
      table1.innerHTML = `
        <thead>
          <tr><th>Index #</th><th>Value</th></tr>
        </thead>
        <tbody>
          ${data.table_data.map(row => `<tr><td>${row[0]}</td><td>${row[1]}</td></tr>`).join('')}
        </tbody>`;
      tableContainer.appendChild(table1); // Append the table to the container

      // Handle Table 2 with computed values (Alpha, Beta, Charlie)
      const table2 = document.getElementById('table2');
      if (data.computed) {
        // Show Table 2 with computed results
        document.getElementById('alpha-value').textContent = data.computed.Alpha;
        document.getElementById('beta-value').textContent = data.computed.Beta;
        document.getElementById('charlie-value').textContent = data.computed.Charlie;
        table2.style.display = 'table'; // Display Table 2
      } else {
        // Hide Table 2 if no computed results are available
        table2.style.display = 'none';
      }
    })
    .catch(err => {
      console.error('Error:', err); // Log the error to the console
      alert('Something went wrong while uploading the file. Please try again.'); // Alert user of an error
    });
});
