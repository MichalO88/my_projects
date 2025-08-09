# Fascynująca Analiza Danych EDA Irysów

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moje Projekty</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;  /* Pełna wysokość strony */
           /* overflow: hidden;   Usuwa przewijanie strony */
            font-family: Arial, sans-serif;  /* Czcionka na całej stronie */
        }

        .container {
            padding: 20px;
            text-align: center;  /* Centrujemy treść */
        }

        h1 {
            font-size: 2em;
            color: #333;
        }

        p {
            font-size: 1.2em;
            color: #555;
        }

        iframe {
            border: none;  /* Usuwamy obramowanie */
            width: 100%;  /* Szerokość na 100% */
            height: 80vh;  /* Wysokość na 80% wysokości okna */
            display: block;  /* Ustawienie na blokowy typ wyświetlania */
            margin-top: 20px;  /* Odstęp od przycisku */
        }

        .download-button {
            background-color: #6e28a7ff;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 20px;  /* Odstęp poniżej przycisku */
        }

        .download-button:hover {
            background-color: #217388ff;
        }

    </style>
</head>
<body>
    <div class="container">
      
        <!-- Przycisk do pobrania PDF -->
        <button class="download-button">
            <a href="iris.pdf" download style="color: white; text-decoration: none;">Pobierz PDF</a>
        </button>
        
        <!-- Wyświetlanie PDF w iframe -->
        <iframe id="content" src="iris.pdf"></iframe>
    </div>

    <script>
        function resizeIframeToFitContent(iframe) {
            // Spróbuj dostosować wysokość iframe do zawartości PDF
            try {
                iframe.style.height = iframe.contentWindow.document.documentElement.scrollHeight + "px";
            } catch (e) {
                console.log('Błąd podczas dopasowywania rozmiaru iframe');
            }
        }

        window.addEventListener('load', function() {
            var iframe = document.getElementById('content');
            resizeIframeToFitContent(iframe);
        });

        window.addEventListener('resize', function() {
            var iframe = document.getElementById('content');
            resizeIframeToFitContent(iframe);
        });
    </script>
</body>
</html>

