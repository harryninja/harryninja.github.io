function downloadLocalPdf() {

    fetch("../images/Total.pdf")
        .then(resp => resp.blob())
        .then(blob => {

            const url = window.URL.createObjectURL(blob);

            let a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;

            a.download = 'Total.pdf';

            document.body.appendChild(a);

            a.click();

            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        })
    .catch(() => alert('oh no!'));
}

function downloadFile() {
    const filename = 'CV.pdf'
    const url = 'https://files.fm/u/vjfg4fx39'
    fetch(url)
        .then(resp => resp.blob())
        .then(blob => {
            // Create a blob link
            const url = window.URL.createObjectURL(blob);

            // Create an a tag
            let a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;

            // Set the filename
            a.download = filename;

            // Append to body
            document.body.appendChild(a);

            // Simulate click, start download
            a.click();

            // Cleanup, remove the link
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        })
        .catch(() => alert('An error occurred while downloading the file'));
}