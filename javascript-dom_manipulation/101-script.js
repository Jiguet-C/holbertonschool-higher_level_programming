document.addEventListener('DOMContentLoaded', () => {
  const btnTranslate = document.querySelector('#btn_translate');
  const languageCode = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  btnTranslate.addEventListener('click', () => {
    const selectedLanguage = languageCode.value;
    if (selectedLanguage) {
      const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`;
      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          helloDiv.textContent = data.hello;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
          helloDiv.textContent = 'Error fetching translation';
        });
    } else {
      helloDiv.textContent = 'Please select a language';
    }
  });
});
