function scrape() {
  var url = document.getElementById('urlToScrape').value;
  
  fetch('/scrape', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url: url }),
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('result').textContent = JSON.stringify(data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}
