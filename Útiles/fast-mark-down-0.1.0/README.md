instala la extensión manualmente y copia esto en tu settings.json:

    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "fmd.bold.fmd",
                "settings": {
                    "foreground": "#94eb52", // Color para texto en negrita
                    "fontStyle": "bold" // Añadir estilo de negrita
                }
            },
            {
                "scope": "fmd.italic.fmd",
                "settings": {
                    "foreground": "#09acb5", // Color para texto en cursiva
                    "fontStyle": "italic" // Añadir estilo de cursiva
                }
            },
            {
                "scope": "fmd.strikethrough.fmd",
                "settings": {
                    "foreground": "#ff3c00", // Color para texto tachado
                    "fontStyle": "strikethrough" // Añadir estilo de tachado
                }
            },
            {
                "scope": "fmd.subscript.fmd",
                "settings": {
                    "foreground": "#ff0000" // Color para subíndices
                }
            },
            {
                "scope": "fmd.superscript.fmd",
                "settings": {
                    "foreground": "#00ff00" // Color para superíndices
                }
            },
            {
                "scope": "fmd.code.fmd",
                "settings": {
                    "foreground": "#9494ff" // Color para bloques de código
                }
            },
            {
                "scope": "fmd.math.fmd",
                "settings": {
                    "foreground": "#f2d253" // Color para bloques de matemáticas
                }
            },
            {
                "scope": "fmd.h1.fmd",
                "settings": {
                    "foreground": "#00ff00" // Color para encabezados de nivel 1
                }
            },
            {
                "scope": "fmd.h2.fmd",
                "settings": {
                    "foreground": "#00ffff" // Color para encabezados de nivel 2
                }
            },
            {
                "scope": "fmd.img.fmd",
                "settings": {
                    "foreground": "#ffff00" // Color para imágenes
                }
            },
            {
                "scope": "fmd.def.fmd",
                "settings": {
                    "foreground": "#aaa" // Color para definiciones
                }
            },
            {
                "scope": "fmd.void.fmd",
                "settings": {
                    "foreground": "#05acb5" // Color para void
                }
            },
            {
                "scope": "fmd.done.fmd",
                "settings": {
                    "foreground": "#02e9f5" // Color para done
                }
            },
            {
                "scope": "fmd.numbered.fmd",
                "settings": {
                    "foreground": "#ffff00" // Color para numerados
                }
            },
            {
                "scope": "fmd.pointed.fmd",
                "settings": {
                    "foreground": "#ffff00" // Color para apuntados
                }
            },
            {
                "scope": "fmd.brochet.fmd", // Color para brochet
                "settings": {
                    "foreground": "#ffff00",
                }
            }
        ]
    }